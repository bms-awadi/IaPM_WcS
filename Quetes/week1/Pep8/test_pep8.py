# test_pep8.py

# Fonction pour calculer la somme de deux nombres
def calculerSomme(nombreUn,nombreDeux):
    """Retourne la somme de deux nombres."""
    return nombreUn + nombreDeux


# Fonction pour vérifier si un nombre est pair
def est_pair(nombre):
    """Retourne True si le nombre est pair, sinon False."""
    return nombre % 2 == 0


# Fonction pour calculer la moyenne d'une liste de nombres
def calculer_moyenne(listeNombres):
    """Retourne la moyenne d'une liste de nombres."""
    total = sum(listeNombres)
    return total / len(listeNombres)


# Test des fonctions
if __name__ == "__main__":
    # Exemple d'utilisation des fonctions
    somme = calculerSomme(3, 5)
    print(f"La somme de 3 et 5 est : {somme}")

    nombre = 4
    print(f"{nombre} est pair : {est_pair(nombre)}")

    nombres = [10, 20, 30, 40]
    moyenne = calculer_moyenne(nombres)
    print(f"La moyenne des nombres {nombres} est : {moyenne}")
