# 🟣 Défi 09 — Créer et publier une branche

**Niveau : semi-guidé**

## 🎯 Objectif
Comprendre qu'une branche permet d'isoler un travail de la branche principale.

Vérifiez d'abord :

```bash
git status
git branch
```

Votre dépôt doit être propre avant de changer de branche.

Créez puis rejoignez :

```bash
git switch -c feature-design
```

Si la branche existe déjà après une nouvelle tentative :

```bash
git switch feature-design
```

Vérifiez :

```bash
git branch
```

Le symbole `*` indique la branche active.

Dans `travail/preuves/defi09.txt`, expliquez :
1. l'intérêt d'une branche ;
2. quelle branche est active ;
3. ce que signifie selon vous `feature-design`.

Puis :

```bash
git add travail/preuves/defi09.txt
git commit -m "Défi 09 - Découvrir les branches"
git push -u origin feature-design
```

> 💡 `-u` associe votre branche locale à sa branche distante. Les prochains `git push` seront plus simples.
