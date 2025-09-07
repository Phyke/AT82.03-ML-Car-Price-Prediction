import mlflow

loaded_model = mlflow.pyfunc.load_model(
    model_uri="./model/artifacts/",
)
