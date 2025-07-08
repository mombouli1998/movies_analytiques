# movies_analytiques
# **Phase 2 : Data Analyst - Exploration et Visualisation**  

![](architecturephase.png)

## Introduction

**Objectif : Explorer et analyser les données en interrogeant l’API.**  

🔹 **Analyse Exploratoire des Données (EDA)** :  
- Utiliser le **SDK Python** pour requêter l’API et récupérer les données.  
- Identifier les tendances dans les notes des films.  
- Étudier les genres les plus populaires et les préférences des utilisateurs.  

🔹 **Construction d’une Data App avec Streamlit** :  
- Créer une **application interactive** qui permet de visualiser les tendances du cinéma.  
- Intégrer des **tableaux dynamiques** et des **graphiques interactifs**.  
- Offrir une **recherche avancée** des films en fonction des notes et des genres.  

**Livrables** :  
- Un notebook d'analyse exploratoire interactif.  
- Une **application web Streamlit** connectée à l’API qui présente, de manière interactive, les insights aux parties prenantes.

---

## Présentation de Jupyter Notebook

**Jupyter Notebook** est un environnement interactif très populaire dans le monde de la **Data Science**. Il permet d’écrire du code Python, de visualiser des graphiques, d’insérer des textes explicatifs (en Markdown), et de documenter une analyse de données de manière fluide et lisible.

---

### Pourquoi Jupyter Notebook est si populaire ?

🔹 **Interactivité totale** : Chaque cellule de code peut être exécutée indépendamment, ce qui permet d’explorer les données pas à pas.

🔹 **Documentation intégrée** : On peut facilement alterner entre du code Python et des explications en langage naturel (Markdown), ce qui en fait un excellent outil pédagogique et professionnel.

🔹 **Visualisation immédiate** : Les bibliothèques comme `matplotlib`, `seaborn` ou `plotly` s’intègrent parfaitement à Jupyter pour créer des visualisations dynamiques.

🔹 **Support riche** : Intègre du HTML, des tableaux interactifs, des widgets, etc. Parfait pour présenter un projet à un client ou à une équipe.

---

### Un outil central pour le Data Analyst

Durant la phase 2, vous utiliserez Jupyter Notebook pour :

- Charger et explorer les données extraites via votre SDK (et donc indirectement via l’API).
- Réaliser une **analyse exploratoire** complète : tendances, corrélations, genres populaires...
- Visualiser les résultats sous forme de **graphiques** compréhensibles et exploitables.
- Créer un **notebook professionnel** que vous pourrez intégrer dans votre portfolio.

---

Parfait, voici une version retravaillée de la section **Installation rapide** (renommée en **⚙️ Mise en place de l’environnement d’analyse**), adaptée au contexte de la formation, en précisant que l’on travaille avec **VSCode**, un environnement virtuel Python, et un dépôt GitHub :

---

## Mise en place de l’environnement d’analyse

Dans cette formation, nous utilisons **VSCode** comme éditeur principal et organisons chaque phase dans un répertoire Git dédié. Pour cette phase 2 (*Data Analyst – Exploration & Visualisation*), tu vas travailler dans un nouveau projet nommé par exemple `movielens-analytics` (tu crées ton propre répertoire GitHub et tu lui donnes le nom que tu veux)

Voici les étapes pour bien démarrer :

### 1. Cloner le dépôt GitHub du projet

Si ce n’est pas encore fait, commence par cloner le dépôt Git que tu as créé pour cette phase :

```bash
https://github.com/mombouli1998/movies_analytiques
```

### 2. Créer et activer un environnement virtuel

Ensuite, configure un environnement Python isolé pour gérer les dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Si tu es sur Windows, utilise :  
> `.\.venv\Scripts\activate`

### 3. Ouvrir le projet dans VSCode

```bash
code .
```

Si tu reçois une notification *"Sélectionner l'interpréteur Python"*, choisis l’interpréteur correspondant à ton environnement `.venv`.

### 4. Créer un fichier notebook

Cree un fichier dédié à l’analyse :

```bash
touch movie_analytiques.ipynb
```

### 5. Installer le SDK `moviesdk`

Ce SDK te permettra d’interagir avec l’API MovieLens. Installe-le dans ton environnement :

```bash
pip install moviesdk
```

### 6. Lancer et configurer le Jupyter Notebook

Ouvre ton fichier `.ipynb` dans VSCode. Lorsque tu exécutes ta **première cellule**, si Jupyter n’est pas encore installé, VSCode te proposera automatiquement de l’installer (avec `ipykernel`). Accepte pour que tout soit configuré automatiquement.

---

**Ton environnement est prêt !**

Tu peux maintenant démarrer ton **analyse exploratoire interactive** directement dans le fichier `movie_data_analysis.ipynb`.  
On va explorer les films, les notes, les genres... et visualiser tout ça avec des graphiques dynamiques !

---

## Familiarisation avec l'API dans un notebook 

Voir Fichier `movies_analytiques.ipynb` 

## Visualisation des données

Voir Fichier `visualisation.ipynb` 

## Intégration de l'API dans une application Streamlit

Streamlit est une bibliothèque open-source en Python qui permet de créer des applications web interactives pour la visualisation de données et le machine learning de manière rapide et simple. Il est particulièrement populaire auprès des Data Scientists, des ingénieurs et des chercheurs qui souhaitent partager leurs analyses et modèles sans avoir à développer des interfaces web complexes.

Avec Streamlit, il suffit de quelques lignes de code pour créer des applications avec des éléments interactifs comme des graphiques, des tables, des cartes, des curseurs, des boutons, etc. Le principal avantage de Streamlit est sa facilité d'utilisation : il transforme un script Python classique en une application web sans avoir besoin de connaître HTML, CSS ou JavaScript.

Voici quelques caractéristiques principales de Streamlit :
- **Simplicité** : Écrire une application Streamlit se fait généralement en quelques lignes de code.
- **Interactivité** : Il permet d'ajouter facilement des widgets interactifs (curseurs, boîtes de sélection, champs de texte, etc.).
- **Intégration facile avec des bibliothèques Python** : Il supporte des bibliothèques populaires telles que Matplotlib, Plotly, Pandas, et bien d’autres.
- **Mise à jour dynamique** : Les modifications apportées au code sont immédiatement visibles sans avoir à recharger la page.

C'est donc un outil idéal pour prototyper des applications de data science rapidement et les déployer de manière simple.

Pour utiliser *streamlit*, vous devez préalablement l'installer :

```bash
pip install streamlit
```

Notre application Streamlit comprendra un fichier de point d'entrée, le fichier que Streamlit chargera en premier. Dans cette application, nous utiliserons ce fichier pour définir la configuration initiale et créer la navigation entre les pages/menus de l'application.

Exécutez ces commandes à partir du répertoire racine de votre projet :

```bash
mkdir streamlit_app
cd streamlit_app
touch movielens_app.py
touch page1.py
touch page2.py
touch page3.py
```

Codes complet de l'application : voir dossier `streamlit_app`

