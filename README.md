# Orientation Lycée

Ce projet fournit une base pour un site de suivi des choix d'orientation des élèves du lycée.
Il est construit avec Django et propose quelques fonctionnalités de base :

- Création de classes avec un professeur principal.
- Gestion des élèves et de leurs choix d'orientation au fil des trimestres.
- Possibilité d'ajouter des notes ou incidents sur un élève.

## Installation

Créez un environnement virtuel et installez les dépendances :

```bash
pip install django
```

Initialisez la base de données :

```bash
python manage.py migrate
```

Créez un compte administrateur pour accéder à l'interface d'administration :

```bash
python manage.py createsuperuser
```

Lancez le serveur de développement :

```bash
python manage.py runserver
```

## Structure

- `tracker/models.py` : modèles principaux (`SchoolClass`, `Student`, `OrientationRecord`, `Note`).
- `tracker/views.py` : vues simples permettant de lister les classes et les élèves.
- `tracker/templates/` : quelques modèles HTML rudimentaires.

Ce dépôt sert de point de départ. De nombreuses fonctionnalités restent à implémenter pour coller au cahier des charges complet.
