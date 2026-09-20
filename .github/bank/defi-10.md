# 🟣 Défi 10 — Modifier puis fusionner une branche

**Niveau : semi-guidé**

## 🎯 Objectif
Réaliser une modification sur `feature-design`, la publier puis l'intégrer à `main`.

Vérifiez que vous êtes sur la bonne branche :

```bash
git branch
```

Vous devez voir `* feature-design`.

Ajoutez à `travail/style.css` :

```css
/* Design SIN */
h1 { text-align: center; }
```

Dans `travail/preuves/defi10.txt`, expliquez :
1. la différence entre `main` et `feature-design` ;
2. pourquoi la modification n'apparaît pas automatiquement dans `main`.

Ajoutez les deux fichiers, créez un commit et poussez `feature-design`.

Revenez ensuite sur la branche principale :

```bash
git switch main
git merge feature-design
git push
```

> Si Git affiche **Fast-forward**, ce n'est pas une erreur : la fusion a réussi sans commit de merge supplémentaire.

## 🔎 À observer
Après la fusion, le style réalisé sur `feature-design` appartient maintenant aussi à l'historique de `main`.
