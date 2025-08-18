import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const feature1 = formData.get('feature1');
		const feature2 = formData.get('feature2');
		// fetch to fastapi
		const response = await fetch('http://backend:8000/predict', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ feature1, feature2 })
		});
		const data = await response.json();
		return { success: true, prediction: data.prediction };
	}
};
