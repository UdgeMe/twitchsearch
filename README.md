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