import os

import mlflow
from dotenv import load_dotenv

load_dotenv()

tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
model_uri_staging = os.getenv("MLFLOW_MODEL_URI")
registered_model_name = os.getenv("MLFLOW_REGISTERED_MODEL_NAME")

assert tracking_uri is not None
assert model_uri_staging is not None


def transition_model_to_production() -> None:
    client = mlflow.MlflowClient()
    version = client.get_model_version_by_alias(registered_model_name, "staging").version
    client.set_registered_model_alias(registered_model_name, "production", version)
    print(f"Promoted {registered_model_name} version {version} to production.")
    mlflow.set_tracking_uri(tracking_uri)


if __name__ == "__main__":
    transition_model_to_production()
