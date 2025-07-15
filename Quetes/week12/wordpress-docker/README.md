# 📦 WordPress + MySQL en Docker

Ce projet exécute une instance WordPress et une base de données MySQL en conteneurs Docker.

## Structure
```
wordpress-docker/
├── docker-compose.yml
├── .env
└── README.md
```

## Lancer l'application

1. Cloner le projet :
   ```bash
   git clone <lien-du-repo>
   cd wordpress-docker
   ```

2. Lancer :
   ```bash
   docker-compose up -d
   ```

## Variables d'environnement

Les variables sont stockées dans le fichier `.env` :

- `MYSQL_ROOT_PASSWORD`
- `MYSQL_DATABASE`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `WORDPRESS_DB_*`


## Arrêter

```bash
docker-compose down
```
