<script>
	const brands = [
		'Tata', 'Honda', 'Hyundai', 'Maruti', 'Mahindra', 'Volkswagen', 'Toyota', 'Force', 'Skoda', 'BMW', 'Fiat', 'Ford', 'Jaguar', 'Renault', 'Jeep', 'Nissan', 'Chevrolet', 'Datsun', 'Mercedes-Benz', 'Lexus', 'Mitsubishi', 'Volvo', 'Audi', 'Ashok', 'Peugeot', 'Land', 'Ambassador', 'Isuzu', 'MG', 'Opel', 'Daewoo', 'Kia'
	];
	const fuels = ['Petrol', 'Diesel'];
	const seller_types = ['Individual', 'Dealer', 'Trustmark Dealer'];
	const transmissions = ['Automatic', 'Manual'];
	const owners = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'];
	let { form } = $props();

	const defaults = {
		brand: 'Tata',
		year: 2019,
		km_driven: 2560,
		fuel: 'Petrol',
		seller_type: 'Individual',
		transmission: 'Automatic',
		owner: 'First Owner',
		mileage: 24.00,
		engine: 1199.0,
		max_power: 83.81,
		seats: 5.0
	};

	// Helper to prefer submitted value (form?.data) and otherwise use defaults
	function getValue(field) {
		// form?.data may contain strings from the POST; return as-is so the server sees the same
		if (form && form.data && typeof form.data[field] !== 'undefined' && form.data[field] !== null && form.data[field] !== '') {
			return form.data[field];
		}
		return defaults[field] ?? '';
	}
</script>

<div class="mx-auto max-w-3xl">
	<h1 class="mb-6 text-center text-2xl">Car Price Prediction</h1>
	<form method="POST" class="grid grid-cols-1 gap-4 md:grid-cols-2">
		<div>
			<label for="brand" class="mb-1 block text-sm font-medium">Brand</label>
			<select id="brand" name="brand" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('brand')}>
				<option value="">Brand (optional)</option>
				{#each brands as b}
					<option value={b}>{b}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="year" class="mb-1 block text-sm font-medium">Year</label>
			<input id="year" type="number" name="year" placeholder="Year (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('year')} />
		</div>

		<div>
			<label for="km_driven" class="mb-1 block text-sm font-medium">KM Driven</label>
			<input id="km_driven" type="number" name="km_driven" placeholder="KM Driven (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('km_driven')} />
		</div>

		<div>
			<label for="fuel" class="mb-1 block text-sm font-medium">Fuel</label>
			<select id="fuel" name="fuel" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('fuel')}>
				<option value="">Fuel (optional)</option>
				{#each fuels as f}
					<option value={f}>{f}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="seller_type" class="mb-1 block text-sm font-medium">Seller Type</label>
			<select id="seller_type" name="seller_type" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('seller_type')}>
				<option value="">Seller Type (optional)</option>
				{#each seller_types as s}
					<option value={s}>{s}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="transmission" class="mb-1 block text-sm font-medium">Transmission</label>
			<select id="transmission" name="transmission" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('transmission')}>
				<option value="">Transmission (optional)</option>
				{#each transmissions as t}
					<option value={t}>{t}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="owner" class="mb-1 block text-sm font-medium">Owner</label>
			<select id="owner" name="owner" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('owner')}>
				<option value="">Owner (optional)</option>
				{#each owners as o}
					<option value={o}>{o}</option>
				{/each}
			</select>
		</div>

		<div>
			<label for="mileage" class="mb-1 block text-sm font-medium">Mileage</label>
			<input id="mileage" type="number" step="any" name="mileage" placeholder="Mileage (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('mileage')} />
		</div>

		<div>
			<label for="engine" class="mb-1 block text-sm font-medium">Engine</label>
			<input id="engine" type="number" name="engine" placeholder="Engine (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('engine')} />
		</div>

		<div>
			<label for="max_power" class="mb-1 block text-sm font-medium">Max Power</label>
			<input id="max_power" type="number" step="any" name="max_power" placeholder="Max Power (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('max_power')} />
		</div>

		<div>
			<label for="seats" class="mb-1 block text-sm font-medium">Seats</label>
			<input id="seats" type="number" name="seats" placeholder="Seats (optional)" class="w-full rounded border border-gray-300 px-3 py-2" value={getValue('seats')} />
		</div>

		<div>
			<button class="rounded bg-blue-500 px-4 py-2 font-bold text-white hover:bg-blue-700" type="submit">
				Predict Price
			</button>
			{#if form?.error}
				<p class="mt-4 text-red-500">{form.error}</p>
			{/if}
			{#if form?.selling_price}
				<p class="mt-2 font-medium">Predicted Price: {form.selling_price}</p>
			{/if}
		</div>
	</form>
</div>
