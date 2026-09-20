# 🟠 Défi 07 — Annuler une modification

**Niveau : guidé**

## 🎯 Objectif
Apprendre à revenir sur une modification locale non préparée.

Ajoutez volontairement à la fin de `travail/index.html` :

```text
ERREUR A SUPPRIMER
```

Enregistrez puis observez :

```bash
git diff
```

Annulez la modification :

```bash
git restore travail/index.html
```

Vérifiez :

```bash
git status
git diff
```

Dans `travail/preuves/defi07.txt`, expliquez :
1. ce qu'a fait `git restore` ;
2. pourquoi cette commande doit être utilisée avec prudence.

Ajoutez, committez et poussez **uniquement votre preuve**.

> ⚠️ Une modification locale abandonnée avec `restore` peut être perdue.
