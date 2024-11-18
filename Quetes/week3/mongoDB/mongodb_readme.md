# Tuto MongoDB

## Qu'est-ce que MongoDB ?
MongoDB est une base de données NoSQL très populaire, connue pour sa flexibilité et sa capacité à gérer de grandes quantités de données non structurées. Contrairement aux bases de données relationnelles traditionnelles qui utilisent des tables, MongoDB stocke les données sous forme de documents au format JSON (ou plus précisément, BSON, qui est une version binaire de JSON).

### Concepts clés :
- **Base de données** : Un conteneur pour les collections.
- **Collection** : Un groupe de documents MongoDB, similaire à une table dans une base de données relationnelle.
- **Document** : Une paire clé-valeur, similaire à une ligne dans une table, mais plus flexible.

---

## Étape 1 : Installer MongoDB
1. **Téléchargez MongoDB** : Rendez-vous sur le [site officiel de MongoDB](https://www.mongodb.com/try/download/community) pour télécharger l'édition communautaire.
2. **Installez MongoDB** : Suivez les instructions d'installation spécifiques à votre système d'exploitation.
3. **Démarrez le serveur MongoDB** :
   - Sur Windows : Lancez `mongod` dans l'invite de commande.
   - Sur macOS/Linux : Vous devrez peut-être exécuter `sudo mongod`.

## Étape 2 : Commandes de base MongoDB
1. **Lancer le shell MongoDB** : Ouvrez votre terminal et tapez `mongo`.
2. **Lister toutes les bases de données** :
   ```bash
   show dbs
   ```
3. **Créer ou basculer vers une base de données** :
   ```bash
   use maBaseDeDonnées
   ```
   - Si `maBaseDeDonnées` n'existe pas, elle sera créée.

4. **Créer une collection** :
   ```bash
   db.createCollection("maCollection")
   ```

5. **Insérer des données dans une collection** :
   ```bash
   db.maCollection.insert({ nom: "Jean", âge: 30, ville: "Paris" })
   ```

6. **Rechercher des données** :
   - **Trouver tous les documents** :
     ```bash
     db.maCollection.find()
     ```
   - **Trouver des documents avec une condition** :
     ```bash
     db.maCollection.find({ nom: "Jean" })
     ```

7. **Mettre à jour des données** :
   ```bash
   db.maCollection.update(
     { nom: "Jean" }, // filtre
     { $set: { âge: 31 } } // mise à jour
   )
   ```

8. **Supprimer des données** :
   - **Supprimer un document** :
     ```bash
     db.maCollection.remove({ nom: "Jean" })
     ```
   - **Supprimer tous les documents** :
     ```bash
     db.maCollection.remove({})
     ```

---

## Étape 3 : Comprendre les requêtes
1. **Opérateurs de comparaison** :
   - `$eq` : Égal
   - `$ne` : Différent
   - `$gt` : Supérieur
   - `$lt` : Inférieur
   - `$gte` : Supérieur ou égal
   - `$lte` : Inférieur ou égal
   ```bash
   db.maCollection.find({ âge: { $gt: 25 } })
   ```

2. **Opérateurs logiques** :
   - `$or` : OU logique
   - `$and` : ET logique
   - `$not` : NON logique
   ```bash
   db.maCollection.find({ $or: [ { âge: 30 }, { ville: "Paris" } ] })
   ```

3. **Projection** : Spécifier les champs à inclure ou exclure dans les résultats.
   ```bash
   db.maCollection.find({}, { nom: 1, âge: 1 })
   ```

---

## Étape 4 : Indexation
Les index permettent d'exécuter les requêtes plus efficacement.
```bash
db.maCollection.createIndex({ nom: 1 })
```

---

## Étape 5 : Utiliser MongoDB Compass
- **MongoDB Compass** : Une interface graphique (GUI) pour MongoDB qui permet d'explorer visuellement vos données.
- **Télécharger** : Obtenez MongoDB Compass [ici](https://www.mongodb.com/try/download/compass).
- **Se connecter** : Utilisez Compass pour vous connecter à votre instance MongoDB, explorer les données, exécuter des requêtes, et gérer les index.

---

## Étape 6 : Connecter MongoDB avec des applications
1. **Exemple avec Node.js** :
   ```javascript
   const { MongoClient } = require('mongodb');

   const uri = "mongodb://localhost:27017";
   const client = new MongoClient(uri);

   async function run() {
     try {
       await client.connect();
       const database = client.db('maBaseDeDonnées');
       const collection = database.collection('maCollection');
       const doc = { nom: "Marie", âge: 25, ville: "Lyon" };
       await collection.insertOne(doc);
       console.log("Document inséré");
     } finally {
       await client.close();
     }
   }

   run().catch(console.dir);
   ```

2. **Exemple avec Python** :
   ```python
   from pymongo import MongoClient

   client = MongoClient("mongodb://localhost:27017/")
   db = client["maBaseDeDonnées"]
   collection = db["maCollection"]
   document = { "nom": "Alice", "âge": 28, "ville": "Marseille" }
   collection.insert_one(document)
   print("Document inséré")
   ```

