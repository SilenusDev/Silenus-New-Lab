#!/bin/bash

# Arrête et supprime les conteneurs, réseaux, volumes et images
echo "🔨 Nettoyage des conteneurs Docker existants..."
docker-compose down --rmi local -v --remove-orphans

# Supprime les ressources Docker non utilisées
echo "🧹 Nettoyage des ressources système Docker..."
docker system prune -f

# Supprime spécifiquement le volume mysql_data au cas où
echo "🧽 Nettoyage des volumes résiduels..."
docker volume prune -f

echo "✅ Nettoyage terminé !"