# 🟢 Défi 03 — Comprendre `git status` et `git add`

**Niveau : très guidé — début du carnet de bord**

## 🎯 Objectif
Comprendre la différence entre un fichier **modifié** et un fichier **préparé (staged)**.

Ajoutez dans `travail/index.html` :

```html
<p>Mon premier projet SIN</p>
```

Enregistrez, puis :

```bash
git status
git add travail/index.html
git status
```

Comparez les deux affichages.

## 📝 Carnet de bord

Créez le dossier `travail/preuves` s'il n'existe pas, puis le fichier :

```text
travail/preuves/defi03.txt
```

Répondez avec des phrases complètes :
1. À quoi sert `git status` ?
2. Que fait `git add` ?
3. Que signifie **préparé (staged)** ?

Puis :

```bash
git add travail/preuves/defi03.txt
git commit -m "Défi 03 - Comprendre status et add"
git push
```

> 💡 À partir de maintenant, les fichiers `defiXX.txt` constituent votre carnet de bord.
