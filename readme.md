# 📧 Classification automatique des emails

## 1. Présentation du projet

Ce projet consiste à développer une application intelligente capable de classifier automatiquement des emails en différentes catégories à l'aide de techniques de traitement automatique du langage naturel (NLP) et de Machine Learning.

L'objectif est de faciliter le traitement des emails en identifiant automatiquement leur nature afin de mieux les organiser et de faciliter leur gestion.

L'application dispose d'une interface graphique développée avec Streamlit. L'utilisateur peut saisir le contenu d'un email et obtenir sa catégorie prédite ainsi que les probabilités associées aux différentes catégories.

## 2. Objectifs du projet

Les principaux objectifs sont :

- Automatiser la classification des emails.
- Identifier la catégorie à laquelle appartient un email.
- Utiliser des techniques de traitement du langage naturel.
- Appliquer un algorithme de Machine Learning supervisé.
- Développer une interface simple et interactive.
- Évaluer les performances du modèle de classification.

## 3. Technologies et bibliothèques utilisées

Le projet utilise les technologies suivantes :

| Technologie | Utilisation |
|---|---|
| Python | Langage de programmation |
| Pandas | Manipulation et analyse des données |
| NumPy | Calcul et traitement numérique |
| Scikit-learn | Prétraitement du texte, entraînement et évaluation du modèle |
| TF-IDF | Transformation des textes en représentations numériques |
| Régression logistique | Algorithme de classification |
| Joblib | Sauvegarde et chargement du modèle |
| Streamlit | Création de l'interface utilisateur |

## 4. Description des catégories

Le système permet de classifier les emails en cinq catégories :

1. **Réclamation :** emails exprimant une insatisfaction ou signalant un problème.
2. **Demande d'information :** emails dans lesquels l'expéditeur demande des renseignements.
3. **Demande de rendez-vous :** emails visant à organiser une rencontre ou un rendez-vous.
4. **Demande administrative :** emails concernant des documents ou des démarches administratives.
5. **Urgence :** emails nécessitant une attention rapide.

## 5. Organisation du projet

Voici l'organisation des fichiers et des dossiers :

```text
classification_emails/
│
├── app.py
├── train_model.py
├── predict_email.py
├── email_classifier.pkl
├── requirements.txt
├── README.md
│
├── check_dataset.py
├── explore_enron.py
├── explore_folders.py
├── inspect_emails.py
├── extract_emails.py
├── prepare_data.py
├── select_emails.py
├── analyze_candidates.py
├── extract_test.py
├── analyze_errors.py
├── create_dataset_fr.py
├── generate_examples.py
├── add_examples.py
├── improve_training_data.py
├── verify_dataset_fr.py
│
├── data/
│   ├── emails.csv
│   └── candidates.csv
│
├── data_fr/
│   ├── emails_fr.csv
│   ├── train.csv
│   └── test.csv
│
└── venv/
```

## 6. Explication détaillée des fichiers

### A. Fichiers principaux de l'application

#### `app.py`

C'est le fichier principal de l'application.

Il permet de lancer l'interface graphique avec Streamlit.

Ses fonctionnalités sont :

- Afficher une interface utilisateur.
- Permettre à l'utilisateur de saisir un email.
- Charger le modèle de classification sauvegardé.
- Prédire la catégorie de l'email.
- Afficher la confiance estimée de la prédiction.
- Présenter les probabilités des différentes catégories sous forme de graphique.

#### `train_model.py`

Ce fichier est responsable de l'entraînement du modèle de Machine Learning.

Il effectue principalement les opérations suivantes :

1. Charger les données d'entraînement.
2. Préparer les textes pour la classification.
3. Transformer les textes en vecteurs numériques avec TF-IDF.
4. Entraîner le modèle de régression logistique.
5. Évaluer les performances sur les données de test.
6. Sauvegarder le modèle entraîné.

#### `predict_email.py`

Ce fichier permet de tester le modèle directement depuis le terminal.

L'utilisateur saisit un email et le modèle prédit automatiquement sa catégorie.

#### `email_classifier.pkl`

Ce fichier contient le modèle entraîné sauvegardé avec Joblib.

Il contient le pipeline de classification, notamment le vectoriseur TF-IDF et le classificateur de régression logistique.

Il est chargé par l'application pour effectuer les prédictions sans devoir réentraîner le modèle à chaque lancement.

#### `requirements.txt`

Ce fichier contient la liste des bibliothèques Python nécessaires au fonctionnement du projet.

Il permet d'installer les dépendances avec une seule commande.

### B. Fichiers d'exploration et de préparation des données

#### `check_dataset.py`

Permet de vérifier le dataset initial.

Il affiche notamment :
- Les dimensions du dataset.
- Les noms des colonnes.
- Quelques exemples d'emails.
- Les informations générales sur les données.

#### `explore_enron.py`

Permet d'explorer le corpus Enron afin de comprendre sa structure et son contenu.

#### `explore_folders.py`

Permet d'examiner les différents dossiers et catégories présents dans le corpus initial.

#### `inspect_emails.py`

Permet d'inspecter des exemples d'emails afin de mieux comprendre leur contenu.

#### `extract_emails.py`

Permet d'extraire les emails du corpus initial et de les organiser dans un fichier exploitable.

#### `prepare_data.py`

Permet de préparer les données extraites afin de faciliter leur utilisation dans les étapes suivantes du projet.

#### `select_emails.py`

Permet de sélectionner des emails candidats à partir du corpus initial.

#### `analyze_candidates.py`

Permet d'analyser les emails candidats sélectionnés et d'examiner leur contenu.

#### `extract_test.py`

Permet d'extraire ou de préparer des exemples destinés aux tests du projet.

#### `analyze_errors.py`

Permet d'examiner les erreurs de classification afin de comprendre les difficultés rencontrées par le modèle.

### C. Fichiers de création et d'amélioration du dataset français

#### `create_dataset_fr.py`

Permet de créer le dataset français utilisé dans notre projet.

#### `generate_examples.py`

Permet de générer des exemples d'emails en français pour enrichir les données disponibles.

#### `add_examples.py`

Contient des exemples supplémentaires pouvant être ajoutés au dataset afin d'enrichir les données d'entraînement.

#### `improve_training_data.py`

Permet d'améliorer les données d'entraînement en ajoutant des exemples supplémentaires pour certaines catégories.

#### `verify_dataset_fr.py`

Permet de vérifier le dataset français, notamment :
- Ses dimensions.
- Les noms de ses colonnes.
- La répartition des catégories.
- La structure générale des données.

### D. Dossiers de données

#### `data/`

Ce dossier contient les données issues du corpus Enron utilisées pendant la phase d'exploration.

- `emails.csv` : contient les emails extraits du corpus initial.
- `candidates.csv` : contient les emails sélectionnés comme candidats pour une analyse plus approfondie.

Ces données ont servi principalement à explorer et comprendre les emails. Elles ne constituent pas directement les données françaises étiquetées utilisées pour entraîner le classificateur final.

#### `data_fr/`

Ce dossier contient les données françaises utilisées pour construire et évaluer le modèle.

- `emails_fr.csv` : dataset français contenant initialement 500 exemples générés.
- `train.csv` : données utilisées pour entraîner le modèle. Il contient 410 exemples après l'ajout de 10 exemples supplémentaires.
- `test.csv` : données utilisées pour évaluer le modèle. Il contient 100 exemples.

Les fichiers d'entraînement et de test sont organisés avec deux colonnes principales :

- `email_text` : le contenu de l'email.
- `category` : la catégorie correspondante.

### E. Dossier `venv/`

Ce dossier contient l'environnement virtuel Python du projet.

Il permet d'isoler les bibliothèques utilisées par cette application de celles installées globalement sur l'ordinateur.

Il ne doit pas être inclus dans une distribution du projet.

## 7. Méthodologie utilisée

Le projet repose sur l'apprentissage supervisé et le traitement automatique du langage naturel.

### 7.1. Préparation des données

Les données françaises sont organisées sous forme de tableau contenant le texte de chaque email et sa catégorie.

Les données sont séparées en deux ensembles :

- Ensemble d'entraînement : 410 exemples.
- Ensemble de test : 100 exemples.

### 7.2. Transformation du texte avec TF-IDF

Les algorithmes de Machine Learning ne peuvent pas directement comprendre les textes comme les humains.

Nous utilisons donc TF-IDF (*Term Frequency – Inverse Document Frequency*) pour transformer les emails en représentations numériques.

Cette méthode attribue une importance aux mots en fonction de leur fréquence dans un email et dans l'ensemble des documents.

Nous utilisons également les unigrammes et les bigrammes afin de prendre en compte les mots seuls et certaines associations de deux mots.

### 7.3. Classification avec la régression logistique

Après la transformation des textes, nous utilisons la régression logistique pour prédire la catégorie de chaque email.

Il s'agit d'un algorithme de classification supervisée qui apprend à partir des exemples déjà étiquetés.

Le pipeline utilisé combine la transformation TF-IDF et la régression logistique.

### 7.4. Évaluation du modèle

Le modèle est évalué à l'aide de plusieurs indicateurs :

- Accuracy : proportion de prédictions correctes.
- Precision : proportion de prédictions correctes parmi les emails attribués à une catégorie.
- Recall : proportion d'emails d'une catégorie correctement retrouvés.
- F1-score : moyenne harmonique de la précision et du rappel.

## 8. Résultats obtenus

Lors des tests réalisés, le modèle a obtenu :

- Une accuracy initiale de 97 %.
- Une accuracy de 100 % après l'ajout d'exemples supplémentaires dans les données d'entraînement et les ajustements effectués.

**Remarque importante :** les erreurs du jeu de test ont été examinées pendant l'amélioration du modèle. Les résultats de 100 % ne constituent donc pas une évaluation indépendante et impartiale. Il faudra utiliser un nouveau jeu de test indépendant pour mesurer plus rigoureusement les performances sur des emails jamais utilisés pendant le développement.

De plus, les données françaises utilisées sont principalement synthétiques. Les résultats ne garantissent donc pas les mêmes performances sur de véritables emails reçus dans un environnement professionnel.

## 9. Installation et exécution du projet

### Étape 1 : Créer un environnement virtuel

```bash
python -m venv venv
```

### Étape 2 : Activer l'environnement virtuel

Sous Windows PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

### Étape 3 : Installer les bibliothèques

```bash
pip install -r requirements.txt
```

### Étape 4 : Entraîner le modèle

```bash
python train_model.py
```

Cette commande entraîne le modèle et génère le fichier `email_classifier.pkl`.

### Étape 5 : Tester une prédiction dans le terminal

```bash
python predict_email.py
```

### Étape 6 : Lancer l'application

```bash
python -m streamlit run app.py
```

L'application s'ouvre dans le navigateur et permet de tester la classification automatique des emails.

## 10. Limites du projet

Le projet présente certaines limites :

- Le dataset français est relativement petit.
- Les exemples sont principalement synthétiques.
- Certaines formulations réelles peuvent être différentes de celles présentes dans les données d'entraînement.
- Les performances doivent être vérifiées sur un nouveau jeu de données indépendant.
- Le modèle peut parfois confondre deux catégories lorsque le contenu d'un email est ambigu.

## 11. Perspectives d'amélioration

Plusieurs améliorations peuvent être envisagées :

- Enrichir le dataset avec de véritables emails français anonymisés et correctement étiquetés.
- Ajouter de nouvelles catégories.
- Tester d'autres algorithmes de classification.
- Améliorer la préparation et le nettoyage des textes.
- Évaluer le modèle sur un jeu de test indépendant.
- Ajouter de nouvelles fonctionnalités à l'interface.

## 12. Conclusion

Ce projet nous a permis de mettre en pratique plusieurs notions du traitement automatique du langage naturel et du Machine Learning.

Il montre comment transformer des textes en données numériques, entraîner un modèle de classification supervisée et développer une application interactive permettant de classifier automatiquement des emails.

L'objectif final est de proposer un outil simple qui facilite l'organisation et le traitement des emails.