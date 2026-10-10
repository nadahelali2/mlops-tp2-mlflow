
import mlflow
import mlflow.sklearn
import pandas as pd

# Connexion au serveur MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Charger le modèle champion
modele = mlflow.sklearn.load_model(
    "models:/fraude-tp2@champion"
)

# Exemple d'une transaction
transaction = pd.DataFrame([{
    "montant": 2500.0,
    "anciennete": 2,
    "freq_24h": 8,
    "nuit": 1
}])

# Effectuer une prédiction
prediction = modele.predict(transaction)

print("Prédiction :", prediction[0])

if prediction[0] == 1:
    print("Transaction potentiellement frauduleuse")
else:
    print("Transaction considérée comme normale")
