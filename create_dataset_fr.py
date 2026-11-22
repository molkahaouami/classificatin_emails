import pandas as pd
from pathlib import Path

# Définir les catégories de notre projet
categories = [
    "Réclamation",
    "Demande d'information",
    "Demande de rendez-vous",
    "Demande administrative",
    "Urgence"
]

# Créer le dossier s'il n'existe pas
output_dir = Path("data_fr")
output_dir.mkdir(exist_ok=True)

# Créer un dataset vide avec les bonnes colonnes
df = pd.DataFrame(columns=["email_text", "category"])

# Enregistrer le fichier
output_file = output_dir / "emails_fr.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Structure du dataset créée !")
print("Catégories prévues :")

for category in categories:
    print("-", category)

print("\nFichier créé :", output_file)
print("Nombre d'emails :", len(df))