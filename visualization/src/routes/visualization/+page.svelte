<script lang="ts">
  import { onMount } from "svelte";

  import { getPackages, type Package } from "$lib/backend";
  import Button from "$lib/components/Button.svelte";
  import Globe from "$lib/components/Globe.svelte";

  let packages = $state<Promise<Package[]>>();
  onMount(() => {
    packages = getPackages();
  });
</script>

<main class="bg-black">
  <Button text="Go back" route="/" />

  {#if packages !== undefined}
    {#await packages}
      Loading&hellip;
    {:then packages}
      <Globe
        coordinates={packages.map((it) => ({
          lat: it.latitude,
          lng: it.longitude,
        }))}
      />
    {:catch err}
      {err}
    {/await}
  {/if}
</main>
