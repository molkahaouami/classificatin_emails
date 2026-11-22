import pandas as pd

# Charger le dataset français
df = pd.read_csv("data_fr/emails_fr.csv")

print("Dimensions :", df.shape)

print("\nColonnes :")
print(df.columns.tolist())

print("\nRépartition des catégories :")
print(df["category"].value_counts())

print("\nEmails dupliqués :")
print(df.duplicated(subset=["email_text"]).sum())

print("\nEmails vides :")
print(df["email_text"].isna().sum())

print("\nCatégories présentes :")
print(df["category"].unique())