
import sys
import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

run_id = sys.argv[1]
nom_modele = "fraude-tp2"

client = MlflowClient()

modeles = client.search_logged_models(
    experiment_ids=["2"],
    filter_string=f"source_run_id = '{run_id}'"
)

if not modeles:
    raise ValueError("Aucun modele trouve pour ce run.")

model_id = modeles[0].model_id

version = mlflow.register_model(
    model_uri=f"models:/{model_id}",
    name=nom_modele
)

print(f"Modele enregistre : {nom_modele}")
print(f"Version : {version.version}")
