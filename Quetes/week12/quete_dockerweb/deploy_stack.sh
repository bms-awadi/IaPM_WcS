#!/bin/bash

docker rm -f web db 2>/dev/null
docker network rm web db 2>/dev/null
# Suppression les conteneurs et réseaux existants
docker network create web
docker network create db

# Lancer le conteneur mariadb (db) sur le réseau db uniquement
docker run -d --name db --network db mariadb

# Lancer le conteneur nginx (web) sur les réseaux db + web
docker run -d --name web --network db -p 8080:80 nginx
docker network connect web web

# Attendre quelques secondes pour que les conteneurs démarrent
sleep 3

# Afficher les adresses IPv4
echo "📡 Adresse IP de web :"
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web

echo "📡 Adresse IP de db :"
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db
