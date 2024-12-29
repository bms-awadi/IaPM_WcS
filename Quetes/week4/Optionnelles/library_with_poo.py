from datetime import datetime

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.__titre = titre
        self.__auteur = auteur
        self.__isbn = isbn
        self.__emprunte_par = None
        self.__date_emprunt = None

    def est_disponible(self):
        return self.__emprunte_par is None

    def emprunter(self, membre):
        if self.est_disponible():
            self.__emprunte_par = membre
            self.__date_emprunt = datetime.now()
            return True
        return False

    def retourner(self):
        self.__emprunte_par = None
        self.__date_emprunt = None

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_statut(self):
        return "Disponible" if self.est_disponible() else f"Emprunté par {self.__emprunte_par.get_nom()} depuis {self.__date_emprunt.strftime('%d-%m-%Y %H:%M:%S')}"

    def get_isbn(self):
        return self.__isbn

    def get_date_emprunt(self):
        return self.__date_emprunt


class Membre:
    def __init__(self, nom, id_membre):
        self.__nom = nom
        self.__id_membre = id_membre
        self.__livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.est_disponible():
            if livre.emprunter(self):
                self.__livres_empruntes.append(livre)
                return True
        return False

    def retourner_livre(self, livre):
        if livre in self.__livres_empruntes:
            livre.retourner()
            self.__livres_empruntes.remove(livre)
            return True
        return False

    def get_nom(self):
        return self.__nom

    def get_id(self):
        return self.__id_membre

    def get_livres_empruntes(self):
        return [
            {
                "titre": livre.get_titre(),
                "date_emprunt": livre.get_date_emprunt().strftime('%d-%m-%Y %H:%M:%S')
            } for livre in self.__livres_empruntes
        ]


class Bibliotheque:
    def __init__(self):
        self.__livres = []
        self.__membres = []

    def ajouter_livre(self, livre):
        self.__livres.append(livre)

    def supprimer_livre(self, isbn):
        self.__livres = [livre for livre in self.__livres if livre.get_isbn() != isbn]

    def enregistrer_membre(self, membre):
        self.__membres.append(membre)

    def emprunter_livre(self, id_membre, isbn):
        membre = self.__trouver_membre_par_id(id_membre)
        livre = self.__trouver_livre_par_isbn(isbn)
        if membre and livre:
            return membre.emprunter_livre(livre)
        return False

    def retourner_livre(self, id_membre, isbn):
        membre = self.__trouver_membre_par_id(id_membre)
        livre = self.__trouver_livre_par_isbn(isbn)
        if membre and livre:
            return membre.retourner_livre(livre)
        return False

    def afficher_livres_disponibles(self):
        return [livre.get_titre() for livre in self.__livres if livre.est_disponible()]

    def afficher_livres_empruntes_par_membre(self, id_membre):
        membre = self.__trouver_membre_par_id(id_membre)
        if membre:
            return membre.get_livres_empruntes()
        return []

    def rechercher_livre(self, critere):
        return [
            livre.get_titre() for livre in self.__livres
            if critere.lower() in livre.get_titre().lower() or critere.lower() in livre.get_auteur().lower()
        ]

    def __trouver_livre_par_isbn(self, isbn):
        for livre in self.__livres:
            if livre.get_isbn() == isbn:
                return livre
        return None

    def __trouver_membre_par_id(self, id_membre):
        for membre in self.__membres:
            if membre.get_id() == id_membre:
                return membre
        return None


bibliotheque = Bibliotheque()

# Ajouter des livres
bibliotheque.ajouter_livre(Livre("Captain Tsubasa", "Yōichi Takahashi", "123"))
bibliotheque.ajouter_livre(Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "456"))
bibliotheque.ajouter_livre(Livre("Data Science for Business", "Foster Provost", "789"))
bibliotheque.ajouter_livre(Livre("Artificial Intelligence: A Modern Approach", "Stuart Russell", "101112"))

# Enregistrer des membres
membre1 = Membre("Paul", "001")
membre2 = Membre("Eliana", "002")
membre3 = Membre("Marcus", "003")
bibliotheque.enregistrer_membre(membre1)
bibliotheque.enregistrer_membre(membre2)
bibliotheque.enregistrer_membre(membre3)

# Emprunter des livres
bibliotheque.emprunter_livre("001", "123")
bibliotheque.emprunter_livre("002", "456")

# Afficher les livres disponibles
print("Livres disponibles:", bibliotheque.afficher_livres_disponibles())

# Afficher les livres empruntés par un membre
print("Livres empruntés par Paul:", bibliotheque.afficher_livres_empruntes_par_membre("001"))
print("Livres empruntés par Eliana:", bibliotheque.afficher_livres_empruntes_par_membre("002"))

# Rechercher un livre
print("Recherche de 'Data':", bibliotheque.rechercher_livre("Data"))

# Retourner un livre
bibliotheque.retourner_livre("001", "123")
print("Livres disponibles après retour:", bibliotheque.afficher_livres_disponibles())
print("Livres empruntés par Paul après retour:", bibliotheque.afficher_livres_empruntes_par_membre("001"))


########################################################## Sortie ###############################################################

""" 
Livres disponibles: ['Data Science for Business', 'Artificial Intelligence: A Modern Approach']
Livres empruntés par Paul: [{'titre': 'Captain Tsubasa', 'date_emprunt': '29-12-2024 15:55:07'}]
Livres empruntés par Eliana: [{'titre': 'Le Petit Prince', 'date_emprunt': '29-12-2024 15:55:07'}]
Recherche de 'Data': ['Data Science for Business']
Livres disponibles après retour: ['Captain Tsubasa', 'Data Science for Business', 'Artificial Intelligence: A Modern Approach']
Livres empruntés par Paul après retour: []
"""

##################################################################################################################################