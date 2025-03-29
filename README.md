# Installation réalisée sur Ubuntu


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

# Cloner le repository
```
git clone git@github.com:UdgeMe/twitchsearch.git
```

# Installer npm
```
sudo apt install nodejs
sudo apt install npm
```

# Installer les dépendances pour le front Vue
```
cd twitchsearch/vue
npm install
```

# Lancer l'app fastapi en local
```
fastapi dev main.py
```
