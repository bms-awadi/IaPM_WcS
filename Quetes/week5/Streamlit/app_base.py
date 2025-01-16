import streamlit as st
import seaborn as sns
from PIL import Image
import os


# Titre de l'application
PRENOM = "Awadi"
st.title(f"Bienvenue sur le site web de {PRENOM}")

# Charger le dataset taxis
taxis = sns.load_dataset('taxis')

# Obtenir la liste des zones de récupération
zones = taxis["pickup_zone"].unique()

# Sélection de la zone de récupération
option = st.selectbox("Indiquez votre arrondissement de récupération", zones)

# Afficher la zone de récupération choisie
st.write(f"Tu as choisi : {option}")

image_dict = {
    "Lenox Hill West": "Lenox Hill West.jpg",
    "Upper West Side South": "Upper West Side South.jpg",
    "Alphabet City": "Alphabet City.jpg",
    "Hudson Sq": "Hudson Sq.jpg",
    "Midtown East": "Midtown East.jpg",
}

if option in image_dict:
    image_path = os.path.join("./imgs", image_dict[option])
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=option, use_container_width=True)
    else:
        st.write("Image non trouvée")
else:
    st.write("Aucune image disponible pour cette zone")
