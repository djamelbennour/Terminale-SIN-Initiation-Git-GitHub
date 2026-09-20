# 🟠 Défi 07 — Annuler une modification

Ajoutez volontairement dans `travail/index.html` :
```text
ERREUR A SUPPRIMER
```

Enregistrez puis observez :
```bash
git diff
```

Annulez cette modification :
```bash
git restore travail/index.html
```

Vérifiez avec `git status`.

Dans `travail/preuves/defi07.txt`, expliquez à quoi sert `git restore` et pourquoi il faut l'utiliser avec prudence. Ajoutez, committez et poussez votre preuve.
