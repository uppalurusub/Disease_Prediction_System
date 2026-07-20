import mlflow
import mlflow.sklearn

def log_model(model, accuracy, model_name):

    with mlflow.start_run():

        mlflow.log_param("model_name", model_name)

        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(
            model,
            artifact_path="model"
        )