# 🧰 Fiche mémo — Git & GitHub

## Le cycle à retenir

```bash
git status
git add fichier
git commit -m "Message clair"
git push
```

## Observer avant d'agir

```bash
git status
git diff
git log --oneline
git branch
git remote -v
```

## Branches

```bash
git switch -c ma-branche
git switch main
git merge ma-branche
git push -u origin ma-branche
```

## Corriger

```bash
git restore fichier
```

⚠️ Avant `restore`, utilisez `git diff` : la modification locale abandonnée peut être perdue.

## Les mots importants

| Mot | Signification |
|---|---|
| dépôt | dossier suivi par Git |
| commit | version enregistrée du projet |
| staged / préparé | prêt à entrer dans le prochain commit |
| branche | ligne de travail indépendante |
| main | branche principale |
| origin | nom habituel du dépôt distant |
| push | publier les commits locaux |

## En cas de problème

**1.** Ne paniquez pas et ne recopiez pas une commande trouvée au hasard.  
**2.** Lancez `git status`.  
**3.** Lisez le message complet.  
**4.** Vérifiez votre branche avec `git branch`.  
**5.** Consultez le résumé de **GitHub → Actions → Validation des défis**.
