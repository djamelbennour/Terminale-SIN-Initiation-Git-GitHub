# 🟢 Défi 03 — Comprendre git status et git add

Ajoutez dans `travail/index.html` :
```html
<p>Mon premier projet SIN</p>
```

Lancez :
```bash
git status
git add travail/index.html
git status
```

Observez la différence avant/après `git add`.

Créez le dossier `travail/preuves` puis `travail/preuves/defi03.txt`. Expliquez avec vos mots :
1. à quoi sert `git status` ;
2. ce que fait `git add` ;
3. ce que signifie « préparé (staged) ».

Puis :
```bash
git add travail/preuves/defi03.txt
git commit -m "Défi 03 - Comprendre status et add"
git push
```
