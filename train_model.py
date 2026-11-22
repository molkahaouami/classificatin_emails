
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Charger les données
train_df = pd.read_csv("data_fr/train.csv")
test_df = pd.read_csv("data_fr/test.csv")

X_train = train_df["email_text"]
y_train = train_df["category"]

X_test = test_df["email_text"]
y_test = test_df["category"]

# Créer le modèle
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

# Entraîner
model.fit(X_train, y_train)

# Prédire
y_pred = model.predict(X_test)

# Évaluer
print("Nouvelle Accuracy :", accuracy_score(y_test, y_pred))

print("\nRapport de classification :")
print(classification_report(y_test, y_pred))

print("\nMatrice de confusion :")
print(confusion_matrix(y_test, y_pred))

# Sauvegarder
joblib.dump(model, "email_classifier.pkl")

print("\nNouveau modèle sauvegardé avec succès !")
