# Projet DBT - Quête 1.2 ETL/ELT

Ce projet a été réalisé dans le cadre de la quête **1.2 ETL/ELT - DBT Introduction** de la Wild Code School.  
Il montre comment utiliser **DBT Core** en local avec une base de données **SQLite**, dans un processus ELT.

---

## 🎯 Objectifs pédagogiques

- Comprendre l’utilité de DBT dans le cadre de la transformation de données
- Installer et configurer DBT Core en local
- Initialiser un projet DBT
- Créer des modèles SQL
- Exécuter les transformations avec `dbt run`
- Visualiser les résultats dans SQLite

---

## ⚙️ Prérequis techniques

- Vscode avec Python
- Python ≥ 3.8
- DBT Core (`dbt-sqlite`)
- DB Browser for SQLite (ou équivalent)
- Git / GitHub

---

## 🛠️ Étapes réalisées

### 1. Création de l’environnement

```bash
mkdir DBT_DEMO
cd DBT_DEMO
python3 -m venv venv
source venv/bin/activate
```

### 2. Installation de DBT avec SQLite

```bash
pip install dbt-sqlite
```

### 3. Initialisation du projet DBT

```bash
dbt init dbt_quest
```

Sélectionner l'adaptateur :
```csharp
[1] sqlite
```

### 4. Configuration du fichier profiles.yml

Remplace tout le contenu actuel de ~/.dbt/profiles.yml par ceci :

```yaml
dbt_quest:
  outputs:
    dev:
      type: sqlite
      threads: 1
      database: ./dbt_quest.db
      schema: 'main'
      schemas_and_paths:
        main: './dbt_quest.db'
      schema_directory: './dbt_quest'

    prod:
      type: sqlite
      threads: 1
      database: ./dbt_quest.db
      schema: 'main'
      schemas_and_paths:
        main: './dbt_quest.db'
      schema_directory: './dbt_quest'

  target: dev
```

---

### ✅ Création d’un modèle simple

Dans le fichier models/hello_world.sql
```sql
select 'Coucou tout le monde 👋' as message
```

### 5. Exécution des modèles

```bash
cd dbt_quest
dbt run
```

---

## Initialisation de la base de données avec sqlalchemy

La suite projet utilise une base de données SQLite pour stocker les données nécessaires. 
Suivez les étapes ci-dessous pour initialiser la base de données et importer les données.

### - Étapes pour initialiser la base de données
Assurez-vous d'avoir installé les dépendances nécessaires :

```bash
pip install pandas sqlalchemy
```

### - Exécutez le script init_db.py pour créer la base de données et importer les données :

```bash
python init_db.py
```

Une fois le script exécuté, un fichier dbt_quest.db sera créé dans le répertoire du projet. Ce fichier contient les tables suivantes :

* raw_customers
* raw_items
* raw_orders
* raw_products
* raw_stores
* raw_supplies