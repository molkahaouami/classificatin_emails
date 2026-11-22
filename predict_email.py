
import joblib

# Charger le modèle entraîné
model = joblib.load("email_classifier.pkl")

print("=== CLASSIFICATION AUTOMATIQUE DES EMAILS ===")

# Saisir un email
email = input("\nSaisir le contenu de l'email : ")

# Prédire la catégorie
prediction = model.predict([email])

# Afficher le résultat
print("\nCatégorie prédite :", prediction[0])
