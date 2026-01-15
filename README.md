# Particle Pinball

Un projet de jeu de flipper prétexte à l'experimentation d'implémentation de concept mathématiques.

## Overview

Particle Pinball est un projet éducatif qui simule un jeu de flipper avec une implémentation physique réaliste. Le projet sert de plateforme pour expérimenter et visualiser divers concepts mathématiques et physiques, notamment:

- Mécanique classique (gravité, collisions, énergie)
- Calcul vectoriel et géométrie
- Méthodes d'intégration numérique
- Systèmes de particules et effets visuels
- Détection et réponse aux collisions

## Features

### Core Features
- **Simulation physique réaliste**: Gravité, collisions, et réponse aux obstacles
- **Système de vue modulaire**: Architecture MVC avec vues interchangeables
- **Objets de jeu variés**: Balles, murs, pegs, bumpers, et plateaux inclinés
- **Visualisation en temps réel**: Affichage des vecteurs vitesse, trajectoires, et effets
- **Interface interactive**: Contrôles clavier pour la navigation et l'interaction

### Physics Demos
Le projet inclut plusieurs démonstrations physiques (voir `docs/physics_demo_catalog.md`):
- Mécanique des flippers
- Systèmes de rampe et modification de vitesse
- Champs de force et effets de particules

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation rapide
```bash
# Cloner le repository
git clone <repository-url>
cd particlespinball

# Installer les dépendances
make install

# Lancer l'application
make run
```

### Installation manuelle
```bash
# Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# Lancer l'application
python src/main.py
```

## Utilisation

### Contrôles
- **ÉCHAP**: Quitter l'application
- **Flèches directionnelles**: Contrôler la balle (dans certaines vues)

### Navigation
1. **Écran d'accueil**: Menu principal avec boutons interactifs
   - **Clic souris**: Sélectionner une vue
   - **Touches numériques**: Accéder aux différentes démos
2. **Vue du jeu**: Simulation complète du flipper

## Structure du Projet

```
particlespinball/
├── src/
│   ├── core/                 # Cœur du moteur physique
│   │   ├── __init__.py
│   │   └── world.py         # Constantes globales et état du monde
│   ├── objects/              # Objets du jeu
│   │   ├── __init__.py
│   │   ├── ball.py          # Balle avec propriétés physiques
│   │   ├── board.py         # Plateau de jeu
│   │   ├── bumper.py       # Obstacles dynamiques
│   │   ├── peg.py           # Obstacles passifs
│   │   └── wall.py          # Murs et limites
│   ├── utils/                # Utilitaires
│   │   ├── __init__.py
│   │   └── colors.py        # Définition des couleurs
│   ├── views/                # Vues de l'interface
│   │   ├── __init__.py
│   │   ├── view.py          # Classe de base des vues
│   │   ├── home_view.py     # Écran d'accueil
│   │   └── game_view.py     # Vue principale du jeu
│   └── main.py              # Point d'entrée de l'application
├── docs/
│   └── physics_demo_catalog.md  # Catalogue des démos physiques
├── .gitignore
├── AGENTS.md                # Guidelines pour les agents
├── LICENSE
├── Makefile                 # Commandes de build
├── pyproject.toml           # Configuration du projet
├── README.md               # Ce fichier
└── requirements.txt       # Dépendances Python
```

## Développement

### Commandes Make
```bash
make install      # Installer les dépendances
make run          # Lancer l'application
make clean        # Supprimer l'environnement virtuel
make reinstall    # Nettoyer et réinstaller
make requirements # Générer requirements.txt
```

### Style de Code
Le projet suit les conventions suivantes:
- **Imports**: Utiliser les imports absolus depuis la racine du projet
- **Types**: Utiliser systématiquement les annotations de type
- **Nomage**: PascalCase pour les classes, snake_case pour les variables
- **Docstrings**: Utiliser les triples guillemets pour les descriptions de classes
- **Constantes**: MAJUSCULES pour les constantes
- **Gestion d'erreurs**: Utiliser try/except où approprié

### Outils
- **Formatage**: Ruff pour le formatage et le linting
- **Dépendances**: numpy, pygame-ce
- **Tests**: À implémenter

## Concepts Mathématiques Implémentés

### Physique de Base
- **Gravité**: `F = mg` avec inclinaison du plateau
- **Énergie cinétique**: `E_k = ½mv²`
- **Énergie potentielle**: `E_p = mgh`
- **Conservation de l'énergie**: `E_total = E_k + E_p`

### Mécanique des Collisions
- **Coefficient de restitution**: `e = (v₂' - v₁') / (v₁ - v₂)`
- **Conservation de la quantité de mouvement**: `m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'`
- **Vecteurs normaux et réflexion**

### Méthodes d'Intégration
- **Intégration d'Euler**: `x(t+Δt) = x(t) + v(t)Δt`
- **Intégration de Verlet**: `x(t+Δt) = 2x(t) - x(t-Δt) + a(t)Δt²`

## Contribuer

1. Forker le repository
2. Créer une branche pour votre fonctionnalité
3. Suivre les guidelines de code dans `AGENTS.md`
4. Tester vos changements
5. Soumettre une pull request

## License

Ce projet est sous licence (voir fichier LICENSE).

## Auteurs

- Alex
- Olivier

## Documentation Supplémentaire

- `docs/physics_demo_catalog.md`: Catalogue détaillé des démonstrations physiques
- `AGENTS.md`: Guidelines de développement pour les agents
