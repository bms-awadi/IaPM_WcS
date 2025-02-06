import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Nettoyer les données
    df['continent'] = df['continent'].str.strip()
    return df

# Interface pour télécharger le fichier CSV
uploaded_file = st.file_uploader("Charger votre fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Charger les données
    df = load_data(uploaded_file)

    # Titre de l'application
    st.title("Analyse des données des voitures")

    # Filtrer les données par région
    regions = df["continent"].unique()
    selected_region = st.sidebar.selectbox("Sélectionnez une région", regions)
    filtered_df = df[df["continent"] == selected_region]

    # Afficher les données filtrées
    st.write(f"Données pour la région : {selected_region}")
    st.write(filtered_df)

    # Analyse de corrélation
    st.subheader("Matrice de corrélation")
    numeric_df = filtered_df.select_dtypes(include=["float64", "int64"])
    corr = numeric_df.corr()

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Distribution des variables
    st.subheader("Distribution des variables")
    for column in numeric_df.columns:
        fig, ax = plt.subplots()
        sns.histplot(numeric_df[column], kde=True, ax=ax)
        plt.title(f"Distribution de {column}")
        st.pyplot(fig)

    # Commentaires
    st.subheader("Commentaires")
    st.write("La matrice de corrélation montre les relations linéaires entre les différentes variables.")
    st.write("Les graphiques de distribution permettent de visualiser la répartition des valeurs pour chaque variable.")
else:
    st.write("Veuillez charger un fichier CSV pour commencer l'analyse.")
