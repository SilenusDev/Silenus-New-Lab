# Dockerfile
# Utilise une image de base officielle Python
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers requis depuis le répertoire local vers le conteneur
COPY requirements.txt requirements.txt

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste de l'application
COPY . .

# Expose le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]