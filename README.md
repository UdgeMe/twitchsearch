# Installation réalisée sur Ubuntu 22.04

# Installer mongodb
Suivre la documentation officielle ici : https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu
Quand l'install est OK, démarrer mongo
```
sudo systemctl start mongod
```

# Récupérer le dépot deadsnakes puis installer python3.12
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
sudo apt install python3-pip
```

# Installation et activation d'un environnement virtuel python (optionnel)
```
sudo apt -y install python3.12-venv python3.12-dev
python3.12 -m venv .venv3.12
. .venv3.12/bin/activate
```

# Installation des librairies python
```
pip install fastapi pymongo requests python-dotenv websockets
pip install "fastapi[standard]"
```

# Installation de node et npm
```
sudo apt install nodejs
sudo apt install npm
```

# Cloner le repository
```
git clone git@github.com:UdgeMe/twitchsearch.git
```

# Installer les dépendances pour le front Vue
```
cd twitchsearch/vue
npm install
```

# Créer un .env à la racine du dossier cloné (twitchsearch) avec les token "client" et "secret" de votre application Twitch
Le fichier `.env` doit ressembler à
```
TWITCH_CLIENT="xxxxxxxxxxxxx"
TWITCH_SECRET="yyyyyyyyyyyyy"
```

# Lancer le back fastapi en local (depuis le dossier twitchsearch)
```
fastapi dev main.py
```

# Lancer le front vue en local (depuis le dossier twitchsearch/vue)
```
npm run dev
```
Une fois le front lancé, on pourra accéder à l'application sur http://localhost:5173/