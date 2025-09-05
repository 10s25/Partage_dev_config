# Collectif Indignons-nous bloquons tout

<img src="https://indignonsnous.fr/global/img/logo-inbt.svg" alt="Logo Indignons-nous" width="200">

**Bienvenue sur l'espace collectif du 10 septembre 2025**

Espace collaboratif Indignons-nous bloquons tout pour échanger projets, scripts et configurations de développement.

## 🎯 Objectif

Cet espace collectif permet à l'équipe de :

- Participer les outils et scripts de développement
- Échanger les configurations d'environnement optimisées
- Collaborateur sur des projets communs
- Co-construire les bonnes pratiques de l'équipe

## 📁 Structure

```
collectif-indignons-nous/
├── README.md # Principe de documentation
├── CONTRIBUTING.md # Guide de contribution
├── LICENCE # Licence AGPL-3.0
├── docs/ # Documentation collective et guides techniques
├── scripts/ # Scripts et outils partis
│ ├── python/ # Scripts Python
│ ├── bash/ # Scripts Bash
│ ├── javascript/ # Scripts JavaScript
│ ├── php/ # Scripts PHP
│ ├── go/ # Scripts Go
│ ├── rouille/ # Scripts Rouille
│ ├── java/ # Scripts Java
│ ├── csharp/ # Scripts C#
│ └── automatisation/ # Scripts d'automatisation
├── exemples/ # Projets de référence et modèles
│ ├── web/ # Exemples web
│ ├── api/ # Exemples d'API
│ ├── mobile/ # Exemples de mobiles
│ └── bureau/ # Exemples bureau
├── configs/ # Configurations échangées
│ ├── vscode/ # Configuration VS Code
│ ├── docker/ # Configuration Docker
│ ├── ci-cd/ # Configuration CI/CD
│ └── dotfiles/ # Fichiers de configuration
└── .github/ # Automatisations et workflows
 ├── flux de travail/ # Actions GitHub
 └── ISSUE_TEMPLATE/ # Modèles d'émissions
```

## 🤝 Contributeur de commentaires

### 📋 Bande 1 : Créer une Issue (OBLIGATOIRE)

1. **Allez** Questions dans l'onglet
2. **Cliquez** "Nouveau numéro"
3. **Choisissez** un modèle :
   - « Nouvelle contribution » pour proposer un script/config
   - "Demande de création de projet" pour un nouveau projet
4. **Remplissage** le formule-guide
5. **Attendez** validation/discussion de l'équipe

### 🔧 Étape 2 : Développement

6. **Fourchette** ce dépôt
7. **Cloneur** localisation de la fourche de vote
8. **Créez** une branche pour votre contribution
9. **Développez** selon les spécifications de l'Issue

### 🚀 Étape 3 : Pull Request

10. **Ajoutez** vos fichers dans le dossier approprié
11. **Commitez** avec un message descriptif
12. **Poussez** fourchette d'électeur vers
13. **Ouvrez** une Pull Request en référençant l'Issue

Consultez [CONTRIBUANT.md](CONTRIBUANT.md) verser plus de détails.

## 📋 Types de contributions acceptées

- Scripts d'automatisation
- Configurations d'IDE et d'outils
- Modèles de projets
- Technique de documentation
- Outils de développement
- Exemples de code

## 📄 Licence

Ce projet est sous licence [AGPL-3.0](LICENCE) - voir le fichier LICENCE pour plus de détails.

## 🔧 Maintenance automatique

Ce dépôt utilise GitHub Actions pour :

- Tests automatiques des contributions
- Mise à jour des dépendances
- Validation de la structure des fichers

### 🧹 Scripts de purge GitHub Actions

Pour nettoyer l'historique des workflow runs :

```bash
# Authentification GitHub CLI (une seule fois)
gh auth login

# Script simple et efficace - TESTÉ ✅
./scripts/purge-simple.sh
```

### ⚠️ Configuration requise pour les automatisations

Si vous rencontrez l'erreur `Erreur : Entrée requise et non fournie : jeton`, cela signifie que le jeton d'organisation n'est pas configuré.

**Pour l'administrateur de l'organisation :**

- Consultez le guide complet : [Configuration des jetons](docs/CONFIGURATION_TOKENS.md)
- Configurez le secret `PAT_TOKEN` au niveau de l'organisation

**Pour les contributeurs :**

- Les automatisations fonctionneront automatisation une fois le token configuré
- L'action Aucune demande de votre part

---

**Indignons-nous bloquons tout - 10 septembre 2025**  
_Partigeons nos outils et constructions ensemble !_
