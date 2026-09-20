# 📘 Git & GitHub — L'essentiel à retenir

> **Support de cours — Terminale STI2D spécialité SIN**  
> Ce document accompagne les 12 défis. L'objectif est de comprendre le rôle des commandes avant de les utiliser.

## 🎯 À la fin de l'activité

Vous devez savoir :
- expliquer la différence entre **Git** et **GitHub** ;
- cloner un dépôt ;
- identifier fichiers modifiés, non suivis et préparés ;
- utiliser `status`, `add`, `commit`, `push`, `log` et `diff` ;
- annuler une modification locale simple ;
- utiliser `.gitignore` ;
- créer, publier et fusionner une branche ;
- expliquer `main`, `origin` et dépôt local/distant.

## 1. Git n'est pas GitHub

| Git | GitHub |
|---|---|
| Logiciel de gestion de versions | Plateforme en ligne |
| Fonctionne sur l'ordinateur | Héberge les dépôts distants |
| Crée commits et branches | Facilite partage et collaboration |
| Commandes `git ...` | Interface Web + services |

> **À retenir :** Git gère l'historique du projet. GitHub permet notamment d'héberger et partager cet historique.

## 2. Le cycle fondamental

```text
Fichier modifié
      │
      │ git add
      ▼
Fichier préparé (staged)
      │
      │ git commit
      ▼
Historique local
      │
      │ git push
      ▼
GitHub / dépôt distant
```

Le premier réflexe est :

```bash
git status
```

## 3. Les commandes utilisées

| Commande | Rôle |
|---|---|
| `git clone URL` | Copier un dépôt GitHub sur l'ordinateur |
| `git status` | Voir l'état du dépôt |
| `git add fichier` | Préparer un fichier pour le prochain commit |
| `git commit -m "message"` | Enregistrer une version dans l'historique local |
| `git push` | Envoyer les commits vers GitHub |
| `git log --oneline` | Lire l'historique de façon compacte |
| `git diff` | Voir les modifications non préparées |
| `git restore fichier` | Abandonner une modification locale non préparée |
| `git branch` | Afficher les branches |
| `git switch branche` | Changer de branche |
| `git switch -c branche` | Créer et rejoindre une branche |
| `git merge branche` | Fusionner une branche dans la branche courante |
| `git remote -v` | Voir le dépôt distant |

## 4. Comprendre les trois étapes

Un fichier peut être :
1. **modifié** dans votre dossier ;
2. **préparé (staged)** avec `git add` ;
3. **enregistré** dans l'historique avec `git commit`.

`git add` n'envoie rien sur GitHub. `git commit` n'envoie rien non plus sur GitHub. C'est `git push` qui publie les commits.

## 5. Un bon commit

Un commit doit représenter une modification cohérente.

✅ `Ajout du titre de la page`  
✅ `Correction du style du menu`  
❌ `truc`  
❌ `modif`

Avant un commit :

```bash
git status
git diff
git add fichier
git status
git commit -m "Message précis"
```

## 6. L'historique

```bash
git log --oneline
```

Chaque ligne correspond à un commit avec un identifiant court (hash) et son message. L'historique permet de comprendre l'évolution du projet.

## 7. Annuler une modification

```bash
git restore fichier
```

Cette commande remet le fichier dans son dernier état enregistré lorsque la modification n'est pas préparée.

> ⚠️ La modification abandonnée peut être perdue : vérifiez toujours `git status` et `git diff` avant.

## 8. Ignorer certains fichiers

Un fichier `.gitignore` indique à Git quels fichiers non suivis il doit ignorer.

```gitignore
secret.txt
.env
```

> 🔐 Un vrai mot de passe, token ou secret ne doit jamais être envoyé sur GitHub.

## 9. Les branches

Une branche permet d'isoler un travail avant de l'intégrer à `main`.

```text
main ─────●────────────●
           \          /
            ●────────●
            feature-design
```

Créer une branche :

```bash
git switch -c feature-design
```

La publier :

```bash
git push -u origin feature-design
```

La fusionner dans `main` :

```bash
git switch main
git merge feature-design
git push
```

## 10. Local, distant et origin

- **local** : le dépôt présent sur votre ordinateur ;
- **distant** : le dépôt hébergé sur GitHub ;
- **origin** : le nom donné par Git au dépôt distant principal après un clone.

```bash
git remote -v
```

## 11. Méthode de dépannage

Ne lancez pas une série de commandes au hasard. Commencez par :

```bash
git status
git branch
git log --oneline -5
git remote -v
```

| Situation | À vérifier |
|---|---|
| `nothing to commit` | Le fichier est-il modifié et enregistré ? |
| `not a git repository` | Êtes-vous dans le bon dossier ? |
| branche déjà existante | Utilisez `git switch nom` |
| push rejeté | Lisez entièrement le message avant d'agir |
| fichier absent de Git | Vérifiez son chemin et `.gitignore` |

## 12. Correspondance avec les défis

| Défis | Apprentissages |
|---|---|
| 01–03 | clone, identité, status, add, staging |
| 04–06 | commit, log, diff |
| 07–08 | restore, gitignore |
| 09–10 | branches, publication, merge |
| 11 | local, distant, origin |
| 12 | autonomie sur un mini-projet |

## ✅ Checklist

- [ ] Je sais expliquer Git et GitHub.
- [ ] Je commence par `git status`.
- [ ] Je distingue `add`, `commit` et `push`.
- [ ] Je sais lire un historique simple.
- [ ] Je sais utiliser `git diff`.
- [ ] Je comprends l'intérêt de `.gitignore`.
- [ ] Je sais créer et fusionner une branche.
- [ ] Je sais expliquer `origin`.
