# 🟣 Défi 09 — Créer une branche

Vérifiez d'abord :
```bash
git status
git branch
```

Créez une branche :
```bash
git switch -c feature-design
```

Si elle existe déjà après une nouvelle tentative :
```bash
git switch feature-design
```

Vérifiez avec :
```bash
git branch
```

Créez `travail/preuves/defi09.txt` et expliquez l'intérêt de travailler dans une branche.

Puis ajoutez et committez la preuve et publiez la branche :
```bash
git add travail/preuves/defi09.txt
git commit -m "Défi 09 - Découvrir les branches"
git push -u origin feature-design
```
