import streamlit as st
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Connexion à la base de données
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Création de la table utilisateur si elle n'existe pas
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    avatar TEXT,
    classe TEXT,
    daily_challenges_completed INTEGER DEFAULT 0,
    badges_earned INTEGER DEFAULT 0,
    first_login INTEGER DEFAULT 1
)
''')
conn.commit()

# Fonction pour hacher les mots de passe
def hash_password(password):
    return generate_password_hash(password)

# Fonction pour vérifier les mots de passe
def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

# Fonction pour enregistrer un nouvel utilisateur
def register_user(username, full_name, email, password, avatar, classe):
    hashed_password = hash_password(password)
    c.execute('INSERT INTO users (username, full_name, email, password_hash, avatar, classe) VALUES (?, ?, ?, ?, ?, ?)',
              (username, full_name, email, hashed_password, avatar, classe))
    conn.commit()

# Fonction pour vérifier les identifiants de connexion
def login_user(identifier, password):
    c.execute('SELECT * FROM users WHERE email = ? OR username = ?', (identifier, identifier))
    user = c.fetchone()
    if user and check_password(user[4], password):
        return user
    return None

# Interface utilisateur
st.title("GenaiMath")

menu = ["Accueil", "Inscription", "Connexion", "Dashboard", "Profil"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Accueil":
    st.write("Bienvenue sur notre Plateforme de tutorat Mathématique")

elif choice == "Inscription":
    st.subheader("Inscription")
    username = st.text_input("Nom d'utilisateur")
    full_name = st.text_input("Nom complet")
    email = st.text_input("Email")
    password = st.text_input("Mot de passe", type="password")
    confirm_password = st.text_input("Confirmer le mot de passe", type="password")
    avatar = st.selectbox("Avatar", ["avatar1", "avatar2", "avatar3"])
    classe = st.selectbox("Classe", ["CP", "CE1", "CE2", "CM1", "CM2", "6ème", "5ème", "4ème", "3ème", "2nde", "1ère", "Terminale"])

    if st.button("S'inscrire"):
        if password == confirm_password:
            register_user(username, full_name, email, password, avatar, classe)
            st.success("Inscription réussie !")
        else:
            st.error("Les mots de passe ne correspondent pas.")

elif choice == "Connexion":
    st.subheader("Connexion")
    identifier = st.text_input("Email ou Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = login_user(identifier, password)
        if user:
            st.session_state.user = user
            st.success("Connexion réussie !")
        else:
            st.error("Identifiants incorrects.")

elif choice == "Dashboard":
    if 'user' in st.session_state:
        user = st.session_state.user
        st.subheader(f"Bienvenue, {user[1]}")
        st.write(f"Classe: {user[6]}")
        st.write(f"Nombre de défis quotidiens relevés: {user[7]}")
        st.write(f"Nombre de badges: {user[8]}")
        if st.button("Faire un bilan de connaissances"):
            st.write("Redirigé vers le bilan de connaissances...")
    else:
        st.error("Veuillez vous connecter.")

elif choice == "Profil":
    if 'user' in st.session_state:
        user = st.session_state.user
        st.subheader("Gérer mon profil")
        new_username = st.text_input("Nom d'utilisateur", value=user[1])
        new_full_name = st.text_input("Nom complet", value=user[2])
        new_email = st.text_input("Email", value=user[3])
        new_avatar = st.selectbox("Avatar", ["avatar1", "avatar2", "avatar3"], index=["avatar1", "avatar2", "avatar3"].index(user[5]))
        new_classe = st.selectbox("Classe", ["CP", "CE1", "CE2", "CM1", "CM2", "6ème", "5ème", "4ème", "3ème", "2nde", "1ère", "Terminale"], index=["CP", "CE1", "CE2", "CM1", "CM2", "6ème", "5ème", "4ème", "3ème", "2nde", "1ère", "Terminale"].index(user[6]))
        new_password = st.text_input("Nouveau mot de passe", type="password")

        if st.button("Mettre à jour"):
            if new_password:
                hashed_password = hash_password(new_password)
                c.execute('UPDATE users SET username = ?, full_name = ?, email = ?, password_hash = ?, avatar = ?, classe = ? WHERE id = ?',
                          (new_username, new_full_name, new_email, hashed_password, new_avatar, new_classe, user[0]))
            else:
                c.execute('UPDATE users SET username = ?, full_name = ?, email = ?, avatar = ?, classe = ? WHERE id = ?',
                          (new_username, new_full_name, new_email, new_avatar, new_classe, user[0]))
            conn.commit()
            st.success("Profil mis à jour avec succès !")
    else:
        st.error("Veuillez vous connecter.")
