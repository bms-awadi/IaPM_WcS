import streamlit as st

# Titre de l'application
st.title("Bienvenue sur le site web d'Awadi")

# Sous-titre
st.write("Indiquez votre arrondissement de récupération")

# Liste des arrondissements
arrondissements = ["Manhattan", "Queens", "Bronx", "Brooklyn", "nan"]

# Sélecteur d'arrondissement
selected_arrondissement = st.selectbox("Tu as choisis:", arrondissements)

# Affichage conditionnel des images en fonction de l'arrondissement sélectionné
if selected_arrondissement == "Manhattan":
    st.image("imgs/manhattan.jpg", caption="Tu as choisis: Manhattan")
elif selected_arrondissement == "Queens":
    st.image("imgs/queens.jpg", caption="Tu as choisis: Queens")
elif selected_arrondissement == "Bronx":
    st.image("imgs/bronx.jpg", caption="Tu as choisis: Bronx")
elif selected_arrondissement == "Brooklyn":
    st.image("imgs/brooklyn.jpg", caption="Tu as choisis: Brooklyn")
elif selected_arrondissement == "nan":
    st.image("imgs/question_mark.jpg", caption="Tu as choisis: nan")

# Instructions supplémentaires
st.write("Les images peuvent être différentes.")
st.write("Vous changez la variable PRENOM du titre par votre prénom à vous.")
st.write("Vous utiliserez le dataset task du module seaborn. L'utilisateur pourra choisir un arrondissement de récupération. En fonction du choix de l'arrondissement l'image se modifia.")
st.write("Vous mettrez le code dans un notebook et partagerez le lien en lecture.")

# Critères d'acceptation
st.write("## Critères d'acceptation")
st.write("N'oubliez pas de soumettre aussi lien à la quête une fois que tu as terminé !")
