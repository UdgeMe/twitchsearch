# Installation réalisée sur Ubuntu

# Installer mongodb en suivant https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#std-label-install-mdb-community-ubuntu
Démarrer mongo
```
sudo systemctl start mongod
```

# Récupérer le dépot deadsnakes pour installer python3.12
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
sudo apt install python3-pip
```

# Installation d'un environnement virtuel python (optionnel)
```
sudo apt -y install python3.12-venv python3.12-dev
mkdir projects
cd projects
python3.12 -m venv .venv3.12
. .venv3.12/bin/activate
```

# Installation des librairies python
```
pip install fastapi pymongo requests python-dotenv
pip install "fastapi[standard]"
```

# Installer npm
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

# Lancer le back fastapi en local (dans le dossier twitchsearch)
```
fastapi dev main.py
```

# Lancer le front vue en local (dans le dossier twitchsearch/vue)
```
npm run dev
```
