<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<nav class="bg-gray-800 text-white py-4 mb-2">
	<div class="container mx-auto flex justify-center space-x-8">
		<a href="/" class="hover:text-blue-300 font-semibold">Homepage</a>
		<a href="/model1" class="hover:text-blue-300 font-semibold">Model 1</a>
		<a href="/model2" class="hover:text-blue-300 font-semibold">Model 2 (New)</a>
	</div>
</nav>

{@render children?.()}
