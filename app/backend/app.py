from typing import Any

import joblib
import mlflow
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pipeline_a1 = joblib.load("./model/car_price_pipeline.joblib")
pipeline_a2 = mlflow.sklearn.load_model(model_uri="model/A2_model/")


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"message": "Hello, FastAPI!"}


class RequestPredictModel(BaseModel):
    brand: str | None = None
    year: float | None = None
    km_driven: float | None = None
    fuel: str | None = None
    seller_type: str | None = None
    transmission: str | None = None
    owner: str | None = None
    mileage: float | None = None
    engine: float | None = None
    max_power: float | None = None
    seats: float | None = None


@app.post("/predict/a1")
def predict(data: RequestPredictModel) -> dict[str, Any]:
    # Prepare input as DataFrame with correct column names
    input_df = (
        pd.DataFrame([data.model_dump()])
        .replace({None: np.nan})
        .astype(
            {
                "year": "float64",
                "km_driven": "float64",
                "mileage": "float64",
                "engine": "float64",
                "max_power": "float64",
                "seats": "float64",
            },
        )
    )
    prediction = pipeline_a1.predict(input_df)
    selling_price = np.round(np.exp(prediction[0]), 2)
    return {"selling_price": selling_price}


@app.post("/predict/a2")
def predict_a2(data: RequestPredictModel) -> dict[str, Any]:
    # Prepare input as DataFrame with correct column names
    input_df = (
        pd.DataFrame([data.model_dump()])
        .replace({None: np.nan})
        .astype(
            {
                "year": "int64",
                "km_driven": "float64",
                "mileage": "float64",
                "engine": "float64",
                "max_power": "float64",
                "seats": "float64",
            },
        )
    )
    prediction = pipeline_a2.predict(input_df)
    selling_price = np.round(np.exp(prediction[0]), 2)
    return {"selling_price": selling_price}
