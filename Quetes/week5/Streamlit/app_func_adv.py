import streamlit as st
import pandas as pd

# Fonction pour vérifier les informations d'identification
def check_credentials(username, password, df):
    user = df[(df['name'] == username) & (df['password'] == password)]
    if not user.empty:
        return user.iloc[0]
    return None

# Fonction pour mettre à jour les tentatives de connexion échouées
def update_failed_attempts(username, df):
    df.loc[df['name'] == username, 'failed_login_attemps'] += 1
    df.to_csv('main/Quetes/week5/Streamlit/users.csv', index=False)

# Charger les données des utilisateurs
df = pd.read_csv('main/Quetes/week5/Streamlit/users.csv')

# Initialiser la session state si elle n'existe pas
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'login'

# Page de connexion
if not st.session_state['logged_in']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = check_credentials(username, password, df)
        if user is not None:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['role'] = user['role']
            df.loc[df['name'] == username, 'logged_in'] = True
            df.to_csv('users.csv', index=False)
            st.session_state['current_page'] = 'accueil'  # Rediriger vers la page d'accueil
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")
            update_failed_attempts(username, df)
else:
    if st.sidebar.button("🔒 Déconnexion"):
        st.session_state['logged_in'] = False
        st.session_state['current_page'] = 'login'  # Rediriger vers la page de connexion
    
    st.sidebar.write(f"Bienvenue {st.session_state['username']}")
    
    if st.sidebar.button("🏠 Accueil"):
        st.session_state['current_page'] = 'accueil'
    if st.sidebar.button("🐱 Les photos de mon chat"):
        st.session_state['current_page'] = 'photos'

    # Afficher la page d'accueil
    if st.session_state['current_page'] == 'accueil':
        st.title("Bienvenue sur ma page")
        st.image("./imgs/bravo.jpg")

    # Afficher la page des photos du chat
    if st.session_state['current_page'] == 'photos':
        st.title("Bienvenue dans l'album de mon chat")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("./imgs/chat1.jpg")

        with col2:
            st.image("./imgs/chat2.jpg")

        with col3:
            st.image("./imgs/chat3.jpg")
