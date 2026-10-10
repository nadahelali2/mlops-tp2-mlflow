
import sys
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

nom_modele = "fraude-tp2"
version = sys.argv[1]
alias = sys.argv[2]

client = MlflowClient()

client.set_registered_model_alias(
    name=nom_modele,
    alias=alias,
    version=version
)

print(f"Alias '{alias}' attribue a la version {version}")
