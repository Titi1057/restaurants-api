Ce projet nommé restaurants-api est une API collaborative développée avec FastAPI pour partager mes restaurants préférés en France.

Lancer l’application
Cloner le dépôt GitHub :

git clone https://github.com/TonUtilisateur/restaurants-api.git
cd restaurants-api

Créer un environnement virtuel Python et l’activer :

python3 -m venv venv
source venv/bin/activate

Installer les dépendances :

pip install -r requirements.txt

Lancer le serveur FastAPI :


uvicorn main:app --reload

Accéder à la documentation interactive dans un navigateur :
http://127.0.0.1:8000/docs

Fonctionnalités
Lister les restaurants (avec filtres par ville, cuisine, ou note)

Ajouter, modifier ou supprimer un restaurant

Stockage des données dans un fichier JSON

Collaboration

Ce projet est collaboratif et ouvert à toutes et tous !
Si tu souhaites partager tes restaurants préférés ou améliorer l’application, n’hésite pas à contribuer.

Comment contribuer ?
Fork ce dépôt sur GitHub.

Clone ta copie locale avec :

git clone <URL-de-ton-fork>
Crée une nouvelle branche pour ta contribution :

git checkout -b ma-nouvelle-fonctionnalite

Modifie le fichier data.json pour ajouter ou mettre à jour des restaurants, ou améliore le code.

Committe tes changements :


git add .
git commit -m "Ajout de nouveaux restaurants"

Pousse ta branche sur ton fork :

git push origin ma-nouvelle-fonctionnalite
Ouvre une Pull Request depuis ton fork vers ce dépôt principal.

Les contributions sont relues et validées avant d’être intégrées. Merci pour ta participation ! 🙌
