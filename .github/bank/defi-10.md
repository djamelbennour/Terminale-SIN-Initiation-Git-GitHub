# 🟣 Défi 10 — Modifier puis fusionner une branche

Vous devez être sur `feature-design`.

Ajoutez à `travail/style.css` :
```css
/* Design SIN */
h1 { text-align: center; }
```

Créez `travail/preuves/defi10.txt` et expliquez la différence entre `main` et `feature-design`.

Ajoutez, committez et poussez votre travail.

Puis revenez sur `main` et fusionnez :
```bash
git switch main
git merge feature-design
git push
```

### 🔎 À observer
Après la fusion, les modifications réalisées dans la branche apparaissent aussi dans `main`.
