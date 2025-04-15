<script lang="ts">
  import Button from "$lib/components/Button.svelte";
</script>

<main class="flex h-screen w-screen flex-col items-center justify-center gap-4">
  <p class="text-center">
    Unfortunately, I didn&CloseCurlyQuote;t manage to connect these two parts.<br
    />
    However, you can still see them separately.
  </p>

  <Button text="Data Wrangling" route="data-wrangling" />
  <Button text="Visualization" route="visualization" />
</main>
