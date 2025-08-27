<script>
// @ts-nocheck

	const brands = [
		'Tata', 'Honda', 'Hyundai', 'Maruti', 'Mahindra', 'Volkswagen', 'Toyota', 'Force', 'Skoda', 'BMW', 'Fiat', 'Ford', 'Jaguar', 'Renault', 'Jeep', 'Nissan', 'Chevrolet', 'Datsun', 'Mercedes-Benz', 'Lexus', 'Mitsubishi', 'Volvo', 'Audi', 'Ashok', 'Peugeot', 'Land', 'Ambassador', 'Isuzu', 'MG', 'Opel', 'Daewoo', 'Kia'
	];
	const fuels = ['Petrol', 'Diesel'];
	const seller_types = ['Individual', 'Dealer', 'Trustmark Dealer'];
	const transmissions = ['Automatic', 'Manual'];
	const owners = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'];
	let { form } = $props();

	const default_brand = 'Honda';
	const default_year = 2004;
	const default_km_driven = 110000;
	const default_fuel = 'Petrol';
	const default_seller_type = 'Individual';
	const default_transmission = 'Manual';
	const default_owner = 'Third Owner';
	const default_mileage = 12.8;
	const default_engine = 1493.0;
	const default_max_power = 100.0;
	const default_seats = 5.0;

	let brand = $state(null);
	let year = $state(null);
	let km_driven = $state(null);
	let fuel = $state(null);
	let seller_type = $state(null);
	let transmission = $state(null);
	let owner = $state(null);
	let mileage = $state(null);
	let engine = $state(null);
	let max_power = $state(null);
	let seats = $state(null);

	const clearForm = () => {
		// Set every input to empty
		brand = null;
		year = null;
		km_driven = null;
		fuel = null;
		seller_type = null;
		transmission = null;
		owner = null;
		mileage = null;
		engine = null;
		max_power = null;
		seats = null;
	};

	const resetForm = () => {
		brand = default_brand;
		year = default_year;
		km_driven = default_km_driven;
		fuel = default_fuel;
		seller_type = default_seller_type;
		transmission = default_transmission;
		owner = default_owner;
		mileage = default_mileage;
		engine = default_engine;
		max_power = default_max_power;
		seats = default_seats;
	};
</script>

<div class="mx-auto max-w-3xl">
	<h1 class="m-6 text-center text-2xl font-bold">Car Price Prediction</h1>
	<div class="mb-4 text-center text-gray-700">
		<p class="mb-1">Put your car details below to get an estimated price.</p>
		<p class="text-sm text-gray-500">You may leave one field blank.</p>
	</div>
	<form method="POST" class="grid grid-cols-1 gap-4 md:grid-cols-3">
		<div>
			<label for="brand" class="mb-1 block text-sm font-medium">Brand</label>
			<select id="brand" name="brand" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={brand}>
				<option value="">Not Specified</option>
				{#each brands as b}
					<option value={b}>{b}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="year" class="mb-1 block text-sm font-medium">Year</label>
			<input min=0 id="year" type="number" name="year" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={year} />
		</div>

		<div>
			<label for="km_driven" class="mb-1 block text-sm font-medium">KM Driven</label>
			<input min=0 step="any" id="km_driven" type="number" name="km_driven" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={km_driven} />
		</div>

		<div>
			<label for="fuel" class="mb-1 block text-sm font-medium">Fuel</label>
			<select id="fuel" name="fuel" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={fuel}>
				<option value="">Not Specified</option>
				{#each fuels as f}
					<option value={f}>{f}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="seller_type" class="mb-1 block text-sm font-medium">Seller Type</label>
			<select id="seller_type" name="seller_type" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={seller_type}>
				<option value="">Not Specified</option>
				{#each seller_types as s}
					<option value={s}>{s}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="transmission" class="mb-1 block text-sm font-medium">Transmission</label>
			<select id="transmission" name="transmission" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={transmission}>
				<option value="">Not Specified</option>
				{#each transmissions as t}
					<option value={t}>{t}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="owner" class="mb-1 block text-sm font-medium">Owner</label>
			<select id="owner" name="owner" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={owner}>
				<option value="">Not Specified</option>
				{#each owners as o}
					<option value={o}>{o}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="mileage" class="mb-1 block text-sm font-medium">Mileage</label>
			<input min=0 step="any" id="mileage" type="number" name="mileage" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={mileage} />
		</div>

		<div>
			<label for="engine" class="mb-1 block text-sm font-medium">Engine</label>
			<input min=0 step="any" id="engine" type="number" name="engine" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={engine} />
		</div>

		<div>
			<label for="max_power" class="mb-1 block text-sm font-medium">Max Power</label>
			<input min=0 step="any" id="max_power" type="number" name="max_power" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={max_power} />
		</div>

		<div>
			<label for="seats" class="mb-1 block text-sm font-medium">Seats</label>
			<input min=0 id="seats" type="number" name="seats" class="w-full rounded border border-gray-300 px-3 py-2" bind:value={seats} />
		</div>

		<div class="col-span-2">
			<button class="rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-700" type="submit">
				Predict Price
			</button>
			<button class="rounded bg-gray-500 px-4 py-2 font-bold text-white hover:bg-gray-700" type="button" onclick={resetForm}>
				Sample Values
			</button>
			<button class="rounded bg-red-500 px-4 py-2 font-bold text-white hover:bg-red-700" type="button" onclick={clearForm}>
				Clear Form
			</button>
		</div>
		<div class="col-span-1">
			{#if !form?.success}
				<p class="mt-2 font-medium">{form?.error || 'Please predict'}</p>
			{/if}
			{#if form?.selling_price}
				<p class="mt-2 font-medium">Predicted Price: {form.selling_price}</p>
			{/if}
		</div>
	</form>
</div>
