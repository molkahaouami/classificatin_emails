import pandas as pd
from pathlib import Path

data = [
    # Réclamation (10)
    ("Je vous contacte car ma commande n'a toujours pas été livrée malgré le délai annoncé.", "Réclamation"),
    ("Je suis déçu par la qualité du service reçu et je souhaite signaler ce problème.", "Réclamation"),
    ("Le montant prélevé sur mon compte est incorrect. Merci de vérifier cette erreur.", "Réclamation"),
    ("Cela fait trois semaines que j'attends une réponse à ma réclamation.", "Réclamation"),
    ("Le produit reçu est endommagé et ne correspond pas à ce que j'ai commandé.", "Réclamation"),
    ("Je conteste les frais supplémentaires figurant sur ma facture.", "Réclamation"),
    ("Votre service a annulé mon dossier sans m'avertir. Je souhaite comprendre.", "Réclamation"),
    ("Je ne suis pas satisfait de la prise en charge de ma demande.", "Réclamation"),
    ("J'ai constaté une erreur dans le traitement de mon inscription.", "Réclamation"),
    ("Je souhaite signaler un problème concernant le fonctionnement de votre plateforme.", "Réclamation"),

    # Demande d'information (10)
    ("Pourriez-vous m'indiquer les horaires d'ouverture de votre service ?", "Demande d'information"),
    ("Je souhaiterais obtenir davantage d'informations sur les conditions d'inscription.", "Demande d'information"),
    ("Pouvez-vous me préciser les documents nécessaires pour cette procédure ?", "Demande d'information"),
    ("Je voudrais savoir si le service est accessible aux étudiants.", "Demande d'information"),
    ("Merci de m'expliquer les étapes à suivre pour effectuer cette démarche.", "Demande d'information"),
    ("Pourriez-vous me communiquer le tarif de cette prestation ?", "Demande d'information"),
    ("Je souhaite connaître la date limite de dépôt des dossiers.", "Demande d'information"),
    ("Auriez-vous plus de détails concernant le programme proposé ?", "Demande d'information"),
    ("Pouvez-vous confirmer si cette information est toujours valable ?", "Demande d'information"),
    ("Je voudrais savoir où trouver le formulaire correspondant à ma demande.", "Demande d'information"),

    # Demande de rendez-vous (10)
    ("Serait-il possible de fixer un rendez-vous avec votre responsable ?", "Demande de rendez-vous"),
    ("Je souhaiterais prendre rendez-vous la semaine prochaine.", "Demande de rendez-vous"),
    ("Êtes-vous disponible jeudi matin pour une rencontre ?", "Demande de rendez-vous"),
    ("Merci de me proposer une date pour discuter de mon dossier.", "Demande de rendez-vous"),
    ("Je voudrais réserver un créneau pour un entretien.", "Demande de rendez-vous"),
    ("Pourrions-nous organiser une réunion demain après-midi ?", "Demande de rendez-vous"),
    ("Je souhaite rencontrer un conseiller afin de discuter de ma situation.", "Demande de rendez-vous"),
    ("Merci de me communiquer vos disponibilités pour un rendez-vous.", "Demande de rendez-vous"),
    ("Je vous propose une rencontre mardi à 10 heures.", "Demande de rendez-vous"),
    ("Pourriez-vous confirmer notre rendez-vous prévu pour vendredi ?", "Demande de rendez-vous"),

    # Demande administrative (10)
    ("Je souhaiterais obtenir une attestation de scolarité.", "Demande administrative"),
    ("Merci de m'envoyer une copie de mon relevé de notes.", "Demande administrative"),
    ("Je vous adresse mon dossier d'inscription pour traitement.", "Demande administrative"),
    ("Pouvez-vous renouveler ma carte d'étudiant ?", "Demande administrative"),
    ("Je souhaite demander un certificat de présence.", "Demande administrative"),
    ("Merci de valider mon formulaire de demande de bourse.", "Demande administrative"),
    ("Je voudrais récupérer mon diplôme auprès de votre administration.", "Demande administrative"),
    ("Veuillez trouver ci-joint les documents nécessaires à la mise à jour de mon dossier.", "Demande administrative"),
    ("Je sollicite une copie officielle de mon certificat.", "Demande administrative"),
    ("Pourriez-vous m'aider à compléter ma procédure de transfert de dossier ?", "Demande administrative"),

    # Urgence (10)
    ("URGENT : mon dossier doit être traité avant la fin de la journée.", "Urgence"),
    ("J'ai besoin d'une réponse immédiate car la date limite est demain.", "Urgence"),
    ("Merci de traiter ce problème en priorité, il bloque toute mon activité.", "Urgence"),
    ("Une erreur critique empêche actuellement l'accès à mon compte.", "Urgence"),
    ("Je vous prie d'intervenir rapidement car la situation est urgente.", "Urgence"),
    ("Mon inscription expire aujourd'hui et je n'arrive pas à valider le paiement.", "Urgence"),
    ("Nous devons résoudre ce problème immédiatement pour respecter le délai.", "Urgence"),
    ("Merci de me contacter dès que possible, mon dossier est bloqué.", "Urgence"),
    ("Une intervention rapide est nécessaire avant la fermeture du service.", "Urgence"),
    ("Je signale une situation urgente qui nécessite votre attention aujourd'hui.", "Urgence"),
]

# Créer le DataFrame
df = pd.DataFrame(data, columns=["email_text", "category"])

# Créer le dossier s'il n'existe pas
Path("data_fr").mkdir(exist_ok=True)

# Enregistrer les emails
df.to_csv("data_fr/emails_fr.csv", index=False, encoding="utf-8-sig")

print("Dataset créé avec succès !")
print("Nombre d'emails :", len(df))
print("\nRépartition des catégories :")
print(df["category"].value_counts())