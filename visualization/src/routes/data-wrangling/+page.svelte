<script lang="ts">
  import { onMount } from "svelte";

  import { getPackages, type Package } from "$lib/backend";
  import Button from "$lib/components/Button.svelte";

  let packages = $state<Promise<Package[]>>();
  onMount(() => {
    packages = getPackages();
  });
</script>

<main class="flex flex-col gap-2 p-3">
  <Button text="Go back" route="/" />

  {#if packages !== undefined}
    {#await packages}
      Loading&hellip;
    {:then packages}
      <ul class="flex flex-col gap-2">
        {#each packages as p, i (i)}
          <li
            class="flex h-12 w-240 flex-row items-center justify-center gap-12 rounded-md bg-gray-100 px-4"
          >
            <span class="w-8">{i}</span>

            <span class="w-48 font-mono">{p.ipAddress}</span>

            <span class="w-64">{p.timestamp.toISOString()}</span>

            <div class="flex w-48 flex-row">
              <span>{p.latitude}</span>
              <span class="text-gray-400">/</span>
              <span>{p.longitude}</span>
            </div>

            <span class="w-64">
              {#if p.isSuspicious}Suspicious{:else}Not suspicious{/if}
            </span>
          </li>
        {/each}
      </ul>
    {:catch err}
      {err}
    {/await}
  {/if}
</main>
