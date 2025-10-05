import os

import mlflow
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
model_uri_staging = os.getenv("MLFLOW_MODEL_URI")


assert tracking_uri is not None
assert model_uri_staging is not None

mlflow.set_tracking_uri(tracking_uri)
pipeline_a3 = mlflow.sklearn.load_model(model_uri=model_uri_staging)


def test_model_a3() -> None:
    sample_input = {
        "brand": "Maruti",
        "year": 2014.0,
        "km_driven": 27000.0,
        "fuel": "Petrol",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner",
        "mileage": 18.15,
        "engine": 1197.0,
        "max_power": 82.0,
        "seats": 5.0,
    }
    input_df = pd.DataFrame([sample_input])
    assert input_df.shape == (1, len(sample_input))
    print("==== Passing input shape test ====")
    prediction = pipeline_a3.predict(input_df)
    assert prediction.shape[0] == 1
    print("==== Passing prediction shape test ====")
    print("==============================")
    print("======== Test passed! ========")
    print("==============================")


if __name__ == "__main__":
    test_model_a3()
