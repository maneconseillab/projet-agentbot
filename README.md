# Agent IA MANABOT 

## Setup Instructions

### 1. Créer un environnement virtuel pour le Dev. Tous ces développements se déroulent sous VS_Code "https://apps.microsoft.com/detail/xp9khm4bk9fz7q?launch=true&mode=full&hl=fr-fr&gl=fr&ocid=bingwebsearch"

```bash
python -m venv maneenv
```
# IF ERROR: 
# Parfois il peut arriver que le Terminal de VS_Code nous renvoie une erreur à cause des problèmes d'accès La solution va consister a modifier la stratégie d'exécution pour l'utilisateur courant à exécuter dans le terminal
```` bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
````
# Activationn de l'environnement de travail qu'on vient de créer:  

- Vérifier tout d'abord que Python, et Pip sont installés 
````bash
python --version
py --version
pip --version
```
# IF ERROR: 
- Désinstallez Python et supprimez manuellement ses dossiers s'ils existent encore.
- puis Téléchargez la version 3.13.3 depuis python.org
- Installez Python avec les options suivantes ( Cochez "Add Python to PATH" + Sélectionnez "Customize installation". + 
   Cochez toutes les options, y compris "pip", "tcl/tk", et "py launcher" + Choisissez "Install for all users" pour éviter les problèmes de permissions.
- Faire des vérifications à ala fin de l'installation. 

- **Sous Windows**:

```bash
maneenv\Scripts\activate
```

- **Sous macOS/Linux**:

```bash
source maneenv/bin/activate
```

### 2. Configuration requise pour l'installation: 
```bash
pip install -r requirements.txt

```
# IF ERROR: 
# Suivre le lien suivant pour fixer les bugs lors de l'installation des outils dans le fichiers "requirements.txt" https://stackoverflow.com/questions/64261546/how-to-solve-error-microsoft-visual-c-14-0-or-greater-is-required-when-inst


## Structure du Projet

```bash                           #                              
Ai_Agent/                         # Racine du projet:                 
├── app.py                        # C'est le fichier principal qui contient l'interface Streamlit et orchestre l'interaction avec l'agent. C'est ici qu'on définis l'interface utilisateur (UI) et appelles les fonctions pour exécuter l'agent.         
├── requirements.txt              # Liste toutes les dépendances Python nécessaires pour le projet.               
├── .env                          # Contient les variables d'environnement sensibles (clés API).             
├── README.md                     # Documentation du projet (instructions d'installation, exécution, déploiement).              
├── src/                          # Contient le code source modulaire.              
│   ├── __init__.py               #            
│   ├── agent/                    #              
│   │   ├── __init__.py           #                   
│   │   ├── agent_setup.py        # Contient la logique pour configurer l'agent (modèle, outils, mémoire, prompt).                 
│   │   └── tools_setup.py        # Configure les outils (par exemple, Tavily Search).                      
│   ├── config/                   #                   
│   │   ├── __init__.py           #                     
│   │   └── config.py             # Gère la configuration (chargement des variables d'environnement).                 
│   └── utils/                    #                 
│       ├── __init__.py           #                    
│       └── streamlit_utils.py    # Contient les fonctions utilitaires pour l'interface Streamlit (affichage des messages, streaming).                        
├── tests/                        #                    
│   ├── __init__.py               #           
│   └── test_agent.py             # Contient des tests unitaires pour vérifier le fonctionnement de l'agent (par exemple, réponse à une requête simple).             
└── .gitignore                    # Ignore les fichiers inutiles pour le versionnement (par exemple, __pycache__, .env, *.pyc).          
```
---

## Avantages de cette structure

- **Modularité** : Chaque composant (agent, outils, configuration, UI) est isolé, facilitant les modifications et les tests.
- **Réutilisabilité** : Les fonctions dans **src/** peuvent être réutilisées pour d'autres projets ou interfaces.
- **Sécurité** : Les clés API sont gérées via **.env**, évitant leur exposition.
- **Testabilité** : Le dossier **tests/** permet de vérifier le bon fonctionnement des composants.
- **Déploiement facile** : La structure est compatible avec Streamlit Cloud, Render, ou Heroku, avec un **requirements.txt** clair.

---

---
## Instructions pour initialiser le projet
- Crée les dossiers et fichiers comme indiqué.
- Ajoute les dépendances dans **requirements.txt**.
- Configure ton .env avec les clés API.
- Exécute localement avec :
```bash 
streamlit run app.py
```
- Pour le déploiement, pousse le projet sur GitHub et configure Streamlit Cloud (ou autre) avec les variables d'environnement.
---

---
## Ajouts possibles
- **Logs** : Ajoute un dossier logs/ et un module de journalisation dans **src/utils/** pour tracer les erreurs.
- **Assets** : Crée un dossier **assets/** pour les images ou fichiers statiques (par exemple, logo).
- **CI/CD** : Configure un fichier **.github/workflows/** pour des tests automatisés ou un déploiement continu.
---