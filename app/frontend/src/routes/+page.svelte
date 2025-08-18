<script>
	let { form } = $props();
</script>

<div class="text-center text-2xl">
	<h1>Car Price Prediction</h1>
	<form method="POST">
		<input type="number" name="feature1" placeholder="Enter feature 1" />
		<input type="number" name="feature2" placeholder="Enter feature 2" />
		<button
			class="rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-700"
			type="submit">Predict Price</button
		>
	</form>
	{#if form?.prediction}
		<p>Predicted Price: {JSON.stringify(form.prediction)}</p>
	{/if}
</div>
