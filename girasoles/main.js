let scene, camera, renderer, controls, composer;
let galaxyParticles, galaxyGeometry, galaxyMaterial;
let starfieldParticles;
let animationId;

// State
let isFlying = false;
let clock = new THREE.Clock();

// Animation parameters
let galaxyScale = 0;
let explosionActive = false;

const parameters = {
    count: 80000, // Menos cantidad pero más grandes para que se distingan bien
    size: 0.035, // ¡Girasoles mucho más grandes!
    radius: 9,
    branches: 5,
    spin: 1.5,
    randomness: 0.4,
    randomnessPower: 3.5,
    insideColor: '#8B3A00',
    outsideColor: '#FFD700'
};

const vertexShader = `
    uniform float uTime;
    attribute float aScale;
    attribute vec3 aRandomness;
    varying vec3 vColor;
    void main() {
        vec4 modelPosition = modelMatrix * vec4(position, 1.0);
        
        // Rotate slowly over time (Galaxia entera gira más rápido)
        float angle = atan(modelPosition.x, modelPosition.z);
        float distanceToCenter = length(modelPosition.xz);
        float angleOffset = (1.0 / distanceToCenter) * uTime * 0.5; // Aumentada la velocidad de giro
        angle += angleOffset;
        modelPosition.x = cos(angle) * distanceToCenter;
        modelPosition.z = sin(angle) * distanceToCenter;
        
        modelPosition.xyz += aRandomness;
        
        vec4 viewPosition = viewMatrix * modelPosition;
        vec4 projectedPosition = projectionMatrix * viewPosition;
        gl_Position = projectedPosition;
        
        // Twinkling effect based on time, position, and scale
        float twinkle = (sin(uTime * 2.0 + modelPosition.x * 100.0) + 1.0) * 0.5;
        
        gl_PointSize = uTime < 0.1 ? aScale * 50.0 : aScale * (150.0 + twinkle * 50.0) * (1.0 / - viewPosition.z);
        vColor = color;
    }
`;

const fragmentShader = `
    uniform float uTime;
    varying vec3 vColor;
    void main() {
        vec2 pt = gl_PointCoord - vec2(0.5);
        
        // Hacer que cada girasol gire sobre su propio eje
        float s = sin(uTime * 2.0);
        float c = cos(uTime * 2.0);
        mat2 rot = mat2(c, -s, s, c);
        pt = rot * pt;
        
        float r = length(pt);
        float angle = atan(pt.y, pt.x);
        
        // Crear patrón de pétalos (8 pétalos)
        float petal = 0.5 + 0.15 * sin(angle * 8.0);
        float strength = 1.0 - smoothstep(0.0, petal * 0.5, r);
        
        // Agregar un centro más oscuro
        if (r < 0.15) {
            gl_FragColor = vec4(vColor * 0.4, strength * 0.9);
        } else {
            gl_FragColor = vec4(vColor, strength);
        }
    }
`;

function init() {
    const container = document.getElementById('canvas-container');

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x000000, 0.02);

    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    // Start very close to center for explosion effect
    camera.position.set(0, 0.5, 2);
    scene.add(camera);

    renderer = new THREE.WebGLRenderer({ antialias: false, powerPreference: "high-performance" });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000);
    container.appendChild(renderer.domElement);

    // Post-processing (Bloom)
    const renderScene = new THREE.RenderPass(scene, camera);
    const bloomPass = new THREE.UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.5, 0.4, 0.85);
    bloomPass.threshold = 0;
    bloomPass.strength = 1.8;
    bloomPass.radius = 0.5;

    composer = new THREE.EffectComposer(renderer);
    composer.addPass(renderScene);
    composer.addPass(bloomPass);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.enablePan = false;
    controls.minDistance = 2;
    controls.maxDistance = 20;
    controls.enabled = false;

    createStarfield();
    generateGalaxy();
    
    // Hide galaxy initially
    galaxyParticles.scale.set(0, 0, 0);

    window.addEventListener('resize', onWindowResize);

    document.getElementById('start-btn').addEventListener('click', startExperience);

    animate();
}

function createStarfield() {
    const starCount = 10000;
    const starGeo = new THREE.BufferGeometry();
    const starPos = new Float32Array(starCount * 3);
    const starColors = new Float32Array(starCount * 3);

    for(let i=0; i<starCount; i++) {
        const i3 = i * 3;
        starPos[i3] = (Math.random() - 0.5) * 200;
        starPos[i3+1] = (Math.random() - 0.5) * 200;
        starPos[i3+2] = (Math.random() - 0.5) * 200;
        
        if (Math.abs(starPos[i3]) < 10 && Math.abs(starPos[i3+2]) < 10 && Math.abs(starPos[i3+1]) < 10) {
            starPos[i3] += 20 * Math.sign(starPos[i3]);
        }

        const color = new THREE.Color();
        color.setHSL(Math.random(), 0.5, Math.random() * 0.5 + 0.5);
        starColors[i3] = color.r;
        starColors[i3+1] = color.g;
        starColors[i3+2] = color.b;
    }
    
    starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));
    
    const starMat = new THREE.PointsMaterial({
        size: 0.05,
        vertexColors: true,
        transparent: true,
        opacity: 0.5,
        sizeAttenuation: true
    });
    
    starfieldParticles = new THREE.Points(starGeo, starMat);
    scene.add(starfieldParticles);
}

function generateGalaxy() {
    galaxyGeometry = new THREE.BufferGeometry();
    const positions = new Float32Array(parameters.count * 3);
    const colors = new Float32Array(parameters.count * 3);
    const scales = new Float32Array(parameters.count);
    const randomness = new Float32Array(parameters.count * 3);

    const colorInside = new THREE.Color(parameters.insideColor);
    const colorOutside = new THREE.Color(parameters.outsideColor);

    for (let i = 0; i < parameters.count; i++) {
        const i3 = i * 3;

        const radius = Math.random() * parameters.radius;
        const spinAngle = radius * parameters.spin;
        const branchAngle = (i % parameters.branches) / parameters.branches * Math.PI * 2;

        positions[i3] = Math.cos(branchAngle + spinAngle) * radius;
        positions[i3 + 1] = 0;
        positions[i3 + 2] = Math.sin(branchAngle + spinAngle) * radius;

        const randomX = Math.pow(Math.random(), parameters.randomnessPower) * (Math.random() < 0.5 ? 1 : -1) * parameters.randomness * radius;
        const randomY = Math.pow(Math.random(), parameters.randomnessPower) * (Math.random() < 0.5 ? 1 : -1) * parameters.randomness * radius;
        const randomZ = Math.pow(Math.random(), parameters.randomnessPower) * (Math.random() < 0.5 ? 1 : -1) * parameters.randomness * radius;
        
        randomness[i3] = randomX;
        randomness[i3 + 1] = randomY;
        randomness[i3 + 2] = randomZ;

        const mixedColor = colorInside.clone();
        mixedColor.lerp(colorOutside, radius / parameters.radius);

        colors[i3] = mixedColor.r;
        colors[i3 + 1] = mixedColor.g;
        colors[i3 + 2] = mixedColor.b;

        scales[i] = Math.random() * 0.5 + 0.1;
        
        if(radius < 0.5) {
            scales[i] *= 4;
            colors[i3] = 1; colors[i3+1]=1; colors[i3+2]=1;
        }
    }

    galaxyGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    galaxyGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    galaxyGeometry.setAttribute('aScale', new THREE.BufferAttribute(scales, 1));
    galaxyGeometry.setAttribute('aRandomness', new THREE.BufferAttribute(randomness, 3));

    galaxyMaterial = new THREE.ShaderMaterial({
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        vertexColors: true,
        vertexShader: vertexShader,
        fragmentShader: fragmentShader,
        uniforms: {
            uTime: { value: 0 }
        },
        transparent: true
    });

    galaxyParticles = new THREE.Points(galaxyGeometry, galaxyMaterial);
    scene.add(galaxyParticles);
}

function startExperience() {
    document.getElementById('overlay').classList.add('hidden');
    explosionActive = true;
    
    // Start camera a bit close, then pull back dynamically
    isFlying = true;
    
    // Show UI text after explosion effect finishes
    setTimeout(() => {
        document.getElementById('ui-layer').classList.add('visible');
    }, 2000);
    
    // Enable controls shortly after
    setTimeout(() => {
        isFlying = false;
        controls.enabled = true;
    }, 4500);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    composer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
    animationId = requestAnimationFrame(animate);

    const elapsedTime = clock.getElapsedTime();

    if (galaxyMaterial) {
        galaxyMaterial.uniforms.uTime.value = elapsedTime;
    }
    
    if (starfieldParticles) {
        starfieldParticles.rotation.y = elapsedTime * 0.02;
    }

    // Explosion Effect Popcorn Style
    if (explosionActive) {
        // Popcorn effect: Scale goes up quickly, overshoots slightly, then settles
        // Using a spring-like ease
        galaxyScale += (1.0 - galaxyScale) * 0.05;
        // Overshoot manually by multiplying by a bump function, or just rely on simple lerp
        // For a true popcorn, let's make it pop fast:
        if (galaxyScale < 0.99) {
            galaxyParticles.scale.set(galaxyScale, galaxyScale, galaxyScale);
        } else {
            galaxyParticles.scale.set(1, 1, 1);
        }
    }

    if (isFlying) {
        // Fly backwards to reveal the whole galaxy
        camera.position.lerp(new THREE.Vector3(3, 4, 7), 0.03);
        camera.lookAt(0, 0, 0);
    } else {
        controls.update();
    }

    composer.render();
}

init();
