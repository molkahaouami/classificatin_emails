
import pandas as pd

# Charger uniquement les données d'entraînement
df = pd.read_csv("data_fr/train.csv")

# Nouveaux exemples pour mieux distinguer les catégories
new_examples = [
    # Urgence
    {
        "email_text": "La date limite de dépôt de mon dossier est demain. Merci de traiter ma demande au plus vite.",
        "category": "Urgence"
    },
    {
        "email_text": "Ma procédure sera clôturée dans quelques heures si je ne reçois pas votre validation.",
        "category": "Urgence"
    },
    {
        "email_text": "Je dois obtenir une réponse aujourd'hui pour éviter le rejet définitif de mon dossier.",
        "category": "Urgence"
    },
    {
        "email_text": "Mon inscription risque d'être annulée car le délai de confirmation expire ce soir.",
        "category": "Urgence"
    },
    {
        "email_text": "Merci d'intervenir rapidement, mon dossier est bloqué et la date limite approche.",
        "category": "Urgence"
    },

    # Demande administrative
    {
        "email_text": "Je souhaite régulariser ma situation administrative et connaître les documents nécessaires.",
        "category": "Demande administrative"
    },
    {
        "email_text": "Pourriez-vous m'indiquer la procédure à suivre afin de mettre à jour mon dossier administratif ?",
        "category": "Demande administrative"
    },
    {
        "email_text": "Je vous adresse une demande de mise à jour de mes informations personnelles dans votre système.",
        "category": "Demande administrative"
    },
    {
        "email_text": "Je souhaite obtenir une attestation officielle pour compléter mon dossier.",
        "category": "Demande administrative"
    },
    {
        "email_text": "Merci de m'aider à régulariser mon inscription et à compléter les formalités administratives.",
        "category": "Demande administrative"
    }
]

# Ajouter les exemples
new_df = pd.DataFrame(new_examples)
df = pd.concat([df, new_df], ignore_index=True)

# Éliminer les éventuels doublons
df = df.drop_duplicates(subset=["email_text"])

# Sauvegarder les données d'entraînement
df.to_csv(
    "data_fr/train.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Amélioration terminée !")
print("Nombre d'exemples :", len(df))
print("\nRépartition des catégories :")
print(df["category"].value_counts())
