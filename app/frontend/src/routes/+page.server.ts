import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const getOrNull = (key: string) => {
			const v = formData.get(key);
			return v === '' || v === null ? null : v;
		};
		const payload = {
			brand: getOrNull('brand'),
			year: getOrNull('year') !== null ? Number(getOrNull('year')) : null,
			km_driven: getOrNull('km_driven') !== null ? Number(getOrNull('km_driven')) : null,
			fuel: getOrNull('fuel'),
			seller_type: getOrNull('seller_type'),
			transmission: getOrNull('transmission'),
			owner: getOrNull('owner'),
			mileage: getOrNull('mileage') !== null ? Number(getOrNull('mileage')) : null,
			engine: getOrNull('engine') !== null ? Number(getOrNull('engine')) : null,
			max_power: getOrNull('max_power') !== null ? Number(getOrNull('max_power')) : null,
			seats: getOrNull('seats') !== null ? Number(getOrNull('seats')) : null
		};

		const missingFields = Object.entries(payload)
			.filter(([_, v]) => v === null)
			.map(([k]) => k);
		if (missingFields.length > 1) {
			return {
				success: false,
				error: `You can leave only one field empty.`
			};
		}

		const response = await fetch('http://backend:8000/predict', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		});
		const data = await response.json();
		return {
			success: true,
			selling_price: data.selling_price
		};
	}
};
