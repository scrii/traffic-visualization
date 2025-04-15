<script lang="ts">
  import { goto } from "$app/navigation";

  type Props = {
    text: string;
    route: string;
  };
  let props: Props = $props();
</script>

<button
  class="w-64 rounded-lg bg-gray-200 p-4 font-semibold hover:bg-gray-300 active:bg-gray-400"
  onclick={() => goto(props.route)}
>
  {props.text}
</button>
