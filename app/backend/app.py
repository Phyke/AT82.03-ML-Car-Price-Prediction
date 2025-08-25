from typing import Any

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

loaded_pipeline = joblib.load("./model/car_price_pipeline.joblib")


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"message": "Hello, FastAPI!"}


class RequestPredictModel(BaseModel):
    brand: str | None = None
    year: int | None = None
    km_driven: int | None = None
    fuel: str | None = None
    seller_type: str | None = None
    transmission: str | None = None
    owner: str | None = None
    mileage: float | None = None
    engine: int | None = None
    max_power: float | None = None
    seats: int | None = None


@app.post("/predict")
def predict(data: RequestPredictModel) -> dict[str, Any]:
    # Prepare input as DataFrame with correct column names
    input_df = pd.DataFrame([data.model_dump()])
    prediction = loaded_pipeline.predict(input_df)
    selling_price = np.round(np.exp(prediction[0]), 2)
    return {"selling_price": selling_price}
