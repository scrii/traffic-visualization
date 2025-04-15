<script lang="ts">
  import { onMount } from "svelte";
  import * as THREE from "three";
  import { OrbitControls } from "three/addons/controls/OrbitControls.js";

  type Props = {
    coordinates: {
      lat: number;
      lng: number;
    }[];
  };

  let { coordinates }: Props = $props();

  let container: HTMLDivElement;

  onMount(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000,
    );
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);
    // eslint-disable-next-line
    camera.position.z = 2;

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;

    const geometry = new THREE.SphereGeometry(1, 64, 64);
    const textureLoader = new THREE.TextureLoader();
    const texture = textureLoader.load(
      "https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/earth_atmos_2048.jpg",
    );
    const material = new THREE.MeshPhongMaterial({
      map: texture,
      bumpScale: 0.05,
      specular: new THREE.Color("grey"),
      shininess: 5,
    });
    const earth = new THREE.Mesh(geometry, material);
    scene.add(earth);

    const pointsGeometry = new THREE.BufferGeometry();
    const pointsMaterial = new THREE.PointsMaterial({
      color: 0xff0000,
      size: 0.02,
    });

    const positions = new Float32Array(coordinates.length * 3);
    coordinates.forEach(({ lat, lng }, i) => {
      const phi = (90 - lat) * (Math.PI / 180);
      const theta = (lng + 180) * (Math.PI / 180);

      positions[i * 3] = -Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = Math.cos(phi);
      positions[i * 3 + 2] = Math.sin(phi) * Math.sin(theta);
    });

    pointsGeometry.setAttribute(
      "position",
      new THREE.BufferAttribute(positions, 3),
    );
    const points = new THREE.Points(pointsGeometry, pointsMaterial);
    earth.add(points);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(5, 3, 5);
    scene.add(pointLight);

    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      earth.rotation.y += 0.0005;
      renderer.render(scene, camera);
    };
    animate();

    const onWindowResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };
    window.addEventListener("resize", onWindowResize);

    return () => {
      window.removeEventListener("resize", onWindowResize);
      // eslint-disable-next-line
      container.removeChild(renderer.domElement);
    };
  });
</script>

<div bind:this={container}></div>
