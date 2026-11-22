
import pandas as pd
import joblib

# Charger les données de test et le modèle
test_df = pd.read_csv("data_fr/test.csv")
model = joblib.load("email_classifier.pkl")

# Faire les prédictions
X_test = test_df["email_text"]
y_test = test_df["category"]
predictions = model.predict(X_test)

# Construire un tableau des résultats
results = pd.DataFrame({
    "Email": X_test,
    "Vraie catégorie": y_test,
    "Catégorie prédite": predictions
})

# Garder uniquement les erreurs
errors = results[
    results["Vraie catégorie"] != results["Catégorie prédite"]
]

print("Nombre d'erreurs :", len(errors))
print("\nDétail des emails mal classés :\n")

for index, row in errors.iterrows():
    print("----------------------------------------")
    print("Email :", row["Email"])
    print("Vraie catégorie :", row["Vraie catégorie"])
    print("Catégorie prédite :", row["Catégorie prédite"])
