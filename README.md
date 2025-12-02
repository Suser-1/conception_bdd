# Projet BDD : Ventes de Jeux Vidéo (SIDORA AI)
**Auteur : Sadi FANSA**

## 1. Contexte du projet

Ce projet a été réalisé dans le cadre de la formation **Développeur en intelligence artificielle (Titre RNCP niveau 6)**.

L'objectif est de concevoir et normaliser une **base de données de ventes de jeux vidéo**, en intégrant les bonnes pratiques **RGPD** dès la conception (privacy by design).

Le projet comprend :

* Analyse exploratoire du dataset `vgsales.csv`
* Modélisation de la base de données (MCD et MLD)
* Création et peuplement de la base avec **Python**, **SQLAlchemy**, et la bibliothèque **Faker** pour les utilisateurs simulés
* Gestion des relations entre entités (jeux, utilisateurs, plateformes, éditeurs, genres, ventes)

---

## 2. Technologies utilisées

* **Python 3.11**
* **SQLAlchemy** (ORM pour créer et manipuler la base)
* **SQLite** (base de données locale)
* **Faker** (génération de données utilisateurs)
* **bcrypt** (hachage des mots de passe)
* **pandas** (lecture du CSV `vgsales.csv`)

---

## 3. Structure de la base de données

### 3.1. Entités principales

| Entité    | Attributs principaux                                                | Commentaires                                             |
| --------- | ------------------------------------------------------------------- | -------------------------------------------------------- |
| User      | pseudo_user, mail_user, password_user, consent_user, limitdate_user | Données pseudonymisées, consentement et date limite RGPD |
| Game      | name_game, rank_game                                                | Jeux vidéo du dataset                                    |
| Platform  | name_platform                                                       | Plateformes des jeux                                     |
| Publisher | name_publisher                                                      | Éditeurs des jeux                                        |
| Genre     | type_genre                                                          | Genres des jeux                                          |
| Sale      | na_sales, eu_sales, jp_sales, other_sales, global_sales, id_game    | Ventes associées à un jeu                                |

### 3.2. Tables de liaison

| Table          | Relations        | Commentaires                      |
| -------------- | ---------------- | --------------------------------- |
| user_game      | User ↔ Game      | Association plusieurs-à-plusieurs |
| game_platform  | Game ↔ Platform  | Contient release_year             |
| game_publisher | Game ↔ Publisher | Association plusieurs-à-plusieurs |
| game_genre     | Game ↔ Genre     | Association plusieurs-à-plusieurs |

---

## 4. Diagrammes MCD et MLD

* **MCD et MLD** représentent les entités et leurs relations, ainsi que les clés primaires/étrangères et contraintes.
* Exportés depuis **dbdiagram.io** et sauvegardés en **SVG**.
* Chemin dans le projet : `diagrams/MCD_MLD.svg`

![Diagramme MCD et MLD](diagrams/MCD_MLD.svg)

> Pour générer à nouveau depuis dbdiagram.io :

```sql
# Exemple d'export SQL dbdiagram.io
Table User {
  id_user int [pk]
  pseudo_user varchar(50)
  mail_user varchar(100)
  password_user varchar(100)
  consent_user boolean
  limitdate_user date
}

Table Game {
  id_game int [pk]
  name_game varchar(100)
  rank_game int
}

# ... Ajouter les autres tables et relations
```

---

## 5. Conformité RGPD

* Les **emails et mots de passe** des utilisateurs sont générés et **hachés** avec bcrypt.
* La table `User` inclut :

  * `consent_user` : booléen indiquant le consentement
  * `limitdate_user` : date limite de rétention des données personnelles
* Respect de la **pseudonymisation** et de la **rétention minimale**
* Données sensibles simulées uniquement, aucun vrai utilisateur n’est utilisé

---

## 6. Script de peuplement (`populate.py`)

Le script Python effectue :

1. Génération de 5 utilisateurs avec Faker et bcrypt
2. Import des jeux depuis le CSV `vgsales.csv`
3. Création des liaisons entre jeux, utilisateurs, plateformes, genres et éditeurs
4. Création des ventes associées à chaque jeu

**Exemple d’exécution :**

```bash
python populate.py

Sortie :
⏳ Importation des utilisateurs...
✔ Utilisateurs créés :
- joseph17 (thompsondavid@example.net)
- terri22 (odalton@example.com)
...
⏳ Importation des jeux...
✔ Jeux importés (exemples) :
...
✅ Base de données remplie avec succès !
```

---

## 7. Instructions pour GitHub

1. Ajouter tous les fichiers du projet (code, CSV, diagrammes) dans le dépôt local
2. Créer un fichier `README.md` (ce document)
3. Initialiser le dépôt et pousser sur GitHub :

```bash
git init
git add .
git commit -m "Version finale du projet BDD SIDORA AI"
git branch -M main
git remote add origin <URL_GITHUB>
git push -u origin main
```

---

## 8. Livrables

* Script Python complet (`populate.py`, modèles SQLAlchemy)
* Base de données SQLite créée et remplie
* Diagrammes MCD et MLD en SVG (`diagrams/MCD_MLD.svg`)
* README détaillé (ce document)

---

## 9. Remarques finales

* Base normalisée en **3NF** (3ème forme normale), toutes dépendances transitive éliminées
* Clés primaires, étrangères, contraintes NOT NULL et UNIQUE respectées
* Conception respectant la **privacy by design** et bonnes pratiques RGPD
* Projet prêt à présenter au formateur et à pousser sur GitHub

---