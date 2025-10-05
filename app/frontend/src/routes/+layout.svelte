<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '../app.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<nav class="mb-2 bg-gray-800 py-4 text-white">
	<div class="container mx-auto flex justify-center space-x-8">
		<a href="/" class="font-semibold hover:text-blue-300">Homepage</a>
		<a href="/model1" class="font-semibold hover:text-blue-300">Model 1</a>
		<a href="/model2" class="font-semibold hover:text-blue-300">Model 2 (New)</a>
		<a href="/model3" class="font-semibold hover:text-blue-300">Model 3 (Even Newer)</a>
	</div>
</nav>

{@render children?.()}
