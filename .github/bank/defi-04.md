# 🔵 Défi 04 — Comprendre le commit

**Niveau : guidé**

## 🎯 Objectif
Comprendre qu'un commit enregistre un état du projet dans l'historique local.

Ajoutez dans `travail/index.html` :

```html
<p>Premier commit</p>
```

Puis :

```bash
git status
git add travail/index.html
git status
git commit -m "Défi 04 - Mon premier vrai commit"
git status
```

Observez l'état du dépôt avant et après le commit.

Dans `travail/preuves/defi04.txt`, expliquez avec vos mots :
1. la différence entre `git add` et `git commit` ;
2. si `git commit` envoie le travail sur GitHub.

Ajoutez la preuve, créez son commit puis publiez :

```bash
git add travail/preuves/defi04.txt
git commit -m "Défi 04 - Compte rendu"
git push
```
