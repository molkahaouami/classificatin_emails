
import streamlit as st
import joblib
import pandas as pd

# ----------------------------------
# CONFIGURATION
# ----------------------------------
st.set_page_config(
    page_title="Email Classifier | AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------
# STYLE CSS
# ----------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F4F7FC;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        background: linear-gradient(120deg, #142B52, #2864A5);
        padding: 35px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white;
        font-size: 36px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #E0EAF8;
        font-size: 16px;
        margin-bottom: 0;
    }

    .section-title {
        color: #142B52;
        font-size: 23px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .category-card {
        background: white;
        border: 1px solid #E3EAF3;
        border-radius: 14px;
        padding: 17px 10px;
        text-align: center;
        min-height: 100px;
        box-shadow: 0 3px 12px rgba(20, 43, 82, 0.04);
    }

    .category-card .emoji {
        font-size: 25px;
    }

    .category-card p {
        color: #263B59;
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
        margin-bottom: 0;
    }

    .result-card {
        background: white;
        border: 1px solid #DCE6F2;
        border-radius: 18px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 4px 18px rgba(20, 43, 82, 0.06);
    }

    .result-label {
        color: #64748B;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .result-category {
        color: #1D4E89;
        font-size: 27px;
        font-weight: 750;
    }

    .footer {
        text-align: center;
        color: #8795A8;
        font-size: 12px;
        margin-top: 45px;
    }

    div.stButton > button {
        background: #2463A6;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-weight: 650;
        width: 100%;
        min-height: 48px;
    }

    div.stButton > button:hover {
        background: #174B83;
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# CHARGEMENT DU MODELE
# ----------------------------------
@st.cache_resource
def load_model():
    return joblib.load("email_classifier.pkl")

model = load_model()

# ----------------------------------
# EN-TETE
# ----------------------------------
st.markdown("""
<div class="hero">
    <h1>📧 Email Classifier</h1>
    <p>Classification intelligente des courriers électroniques grâce au Machine Learning.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# PRESENTATION DES CATEGORIES
# ----------------------------------
st.markdown(
    '<div class="section-title">Les catégories disponibles</div>',
    unsafe_allow_html=True
)

categories = [
    ("📢", "Réclamation"),
    ("ℹ️", "Demande d'information"),
    ("📅", "Demande de rendez-vous"),
    ("📄", "Demande administrative"),
    ("🚨", "Urgence")
]

columns = st.columns(5)

for column, (emoji, name) in zip(columns, categories):
    with column:
        st.markdown(f"""
        <div class="category-card">
            <div class="emoji">{emoji}</div>
            <p>{name}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------------
# ZONE DE SAISIE
# ----------------------------------
st.markdown(
    '<div class="section-title">Analyser un email</div>',
    unsafe_allow_html=True
)

st.write("Collez le contenu de votre email ci-dessous pour identifier automatiquement sa catégorie.")

email = st.text_area(
    "Contenu de l'email",
    height=180,
    placeholder="Exemple : Bonjour, je souhaite obtenir des informations concernant mon dossier...",
    label_visibility="collapsed"
)

classify = st.button("🔍 Analyser l'email")

# ----------------------------------
# CLASSIFICATION
# ----------------------------------
if classify:

    if email.strip():

        prediction = model.predict([email])[0]
        probabilities = model.predict_proba([email])[0]
        confidence = max(probabilities) * 100

        emoji_map = {
            "Réclamation": "📢",
            "Demande d'information": "ℹ️",
            "Demande de rendez-vous": "📅",
            "Demande administrative": "📄",
            "Urgence": "🚨"
        }

        emoji = emoji_map.get(prediction, "📧")

        st.markdown("---")
        st.markdown(
            '<div class="section-title">Résultat de l’analyse</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">Catégorie identifiée</div>
            <div class="result-category">{emoji} {prediction}</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Confiance du modèle", f"{confidence:.2f} %")
            st.progress(float(confidence / 100))

        with col2:
            st.metric("Nombre de catégories", len(model.classes_))
            st.caption("Le modèle compare les cinq catégories disponibles.")

        st.markdown("#### Probabilités par catégorie")

        results = pd.DataFrame({
            "Catégorie": model.classes_,
            "Probabilité (%)": probabilities * 100
        }).sort_values(
            by="Probabilité (%)",
            ascending=True
        )

        st.bar_chart(
            results.set_index("Catégorie"),
            x_label="Catégorie",
            y_label="Probabilité (%)",
            horizontal=True
        )

        st.caption(
            "Remarque : le niveau de confiance représente la probabilité estimée "
            "par le modèle, et non une garantie que la classification est correcte."
        )

    else:
        st.warning("Veuillez saisir le contenu d'un email avant de lancer l'analyse.")

# ----------------------------------
# PIED DE PAGE
# ----------------------------------
st.markdown("""
<div class="footer">
    Projet académique — Intelligence Artificielle & Machine Learning<br>
    Classification automatique des emails
</div>
""", unsafe_allow_html=True)
