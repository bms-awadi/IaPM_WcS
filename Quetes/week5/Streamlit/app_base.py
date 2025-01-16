import streamlit as st
import seaborn as sns
from PIL import Image
import os

# Définir votre prénom en variable
PRENOM = "VOTRE_PRENOM"

# Charger le dataset taxis de seaborn (non utilisé ici mais pour respecter la demande)
taxis = sns.load_dataset('taxis')

# Définir les arrondissements fictifs et les images correspondantes
arrondissements = { 'Brooklyn': 'imgs/brooklyn.jpg', 
                   'Manhattan': 'imgs/manhattan.jpg', 
                   'Bronx': 'imgs/bronx.jpg', 
                   'Queens': 'imgs/queens.jpg', 
                   'nan': 'imgs/default.jpg' }

# Fonction pour obtenir l'image en fonction de l'arrondissement
def get_image_path(arrondissement):
    return arrondissements.get(arrondissement, 'imgs/default.jpg')

# Titre de l'application
st.title(f"Bienvenue sur le site web de {PRENOM}")

# Sélection de l'arrondissement
arrondissement = st.selectbox("Indiquez votre arrondissement de récupération", options=list(arrondissements.keys()))

# Afficher l'arrondissement choisi
st.write(f"Tu as choisis: {arrondissement}")

# Afficher l'image correspondante
image_path = get_image_path(arrondissement)
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption=arrondissement, use_container_width=True)
else:
    st.write("Image non trouvée")
