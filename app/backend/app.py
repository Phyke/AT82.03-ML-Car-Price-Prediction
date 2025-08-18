from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"message": "Hello, FastAPI!"}


@app.post("/predict")
def predict(data: dict[str, Any]) -> dict[str, Any]:
    # Dummy prediction logic
    return {"prediction": data}
