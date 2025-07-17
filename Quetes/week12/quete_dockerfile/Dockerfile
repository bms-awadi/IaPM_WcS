# Étape 1 : choisir une image de base légère
FROM alpine:latest

# Étape 2 : copier le script dans l'image
COPY hello_wilder.sh /hello_wilder.sh

# Étape 3 : rendre le script exécutable
RUN chmod +x /hello_wilder.sh

# Étape 4 : définir le script comme commande par défaut
CMD ["/hello_wilder.sh"]
