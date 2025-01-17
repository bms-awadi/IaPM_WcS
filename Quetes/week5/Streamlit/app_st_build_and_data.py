import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset
@st.cache_data
def load_data():
    # Remplacez 'cars.csv' par le chemin de votre dataset
    data = pd.read_csv('cars.csv')
    # Nettoyer la colonne 'continent'
    data['continent'] = data['continent'].str.strip()
    return data

data = load_data()

# Vérifier les noms des colonnes
# Interface utilisateur
st.title('Analyse des Voitures')

# Filtrer par région
region = st.sidebar.selectbox('Sélectionnez une région', ['US', 'Europe', 'Japan'])

# Vérifier si la colonne 'continent' existe
if 'continent' in data.columns:
    filtered_data = data[data['continent'] == region]
else:
    st.error("La colonne 'continent' n'existe pas dans le dataset.")
    filtered_data = data  # Utiliser tout le dataset si la colonne 'continent' n'existe pas

# Analyse de corrélation
st.subheader('Matrice de corrélation')
corr = filtered_data.corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Analyse de distribution
st.subheader('Distribution de la consommation de carburant (mpg)')

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data['mpg'], kde=True, ax=ax)
st.pyplot(fig)

st.subheader('Distribution de la puissance (hp)')

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_data['hp'], kde=True, ax=ax)
st.pyplot(fig)

# Commentaires explicatifs
st.subheader('Commentaires')
st.write("La matrice de corrélation montre les relations linéaires entre les différentes variables du dataset.")
st.write("Le graphique de distribution de la consommation de carburant (mpg) montre comment les valeurs de consommation de carburant sont réparties dans la région sélectionnée.")
st.write("Le graphique de distribution de la puissance (hp) montre comment les valeurs de puissance sont réparties dans la région sélectionnée.")

# Publier l'application sur Streamlit Sharing
# Remplacez 'wilder/streamlit_app/my_streamlit_app.py' par votre propre chemin
