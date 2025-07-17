#!/bin/bash

# Supprimer conteneur et volume s'ils existent
docker rm -f mon_nginx 2>/dev/null
docker volume rm nginx_volume 2>/dev/null

# Créer un volume Docker
docker volume create nginx_volume

# Ajouter index.html dans le volume
docker run --rm -v nginx_volume:/mnt busybox sh -c 'echo "<h1>Bienvenue sur mon serveur Nginx !</h1>" > /mnt/index.html'

# Lancer le conteneur Nginx avec montage du volume
docker run -d \
  --name mon_nginx \
  -p 8080:80 \
  -v nginx_volume:/usr/share/nginx/html \
  nginx
