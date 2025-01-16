import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Manipulation de données et création de graphiques")

# Sélection du dataset
dataset_name = st.selectbox("Quel dataset voulez-vous visualiser ?", sns.get_dataset_names())

# Chargement du dataset sélectionné
data = sns.load_dataset(dataset_name)

# Sélection des colonnes
col_x = st.selectbox("Choisissez la colonne X", data.columns)
col_y = st.selectbox("Choisissez la colonne Y", data.columns)

# Sélection du type de graphique
graph_type = st.selectbox("Quel graphique voulez-vous afficher ?", ["scatter_chart", "bar_chart", "line_chart"])

# Affichage du graphique
if graph_type == "scatter_chart":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=col_x, y=col_y)
    st.pyplot(plt)
elif graph_type == "bar_chart":
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=col_x, y=col_y)
    st.pyplot(plt)
elif graph_type == "line_chart":
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=col_x, y=col_y)
    st.pyplot(plt)

# Bouton pour afficher la matrice de corrélation
if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Ma matrice de corrélation")
    
    # Sélection des colonnes numériques
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Calcul de la matrice de corrélation
    corr = numeric_data.corr()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot(plt)
