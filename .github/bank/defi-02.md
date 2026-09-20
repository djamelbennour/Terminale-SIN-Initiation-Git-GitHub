# 🟢 Défi 02 — Créer le mini-site

**Niveau : très guidé**

## 🎯 Objectif
Créer les premiers fichiers du mini-projet et découvrir les fichiers **non suivis** par Git.

## 1. Créer les fichiers

Dans l'explorateur de VS Code, ouvrez le dossier `travail`.

Créez :
- `index.html`
- `style.css`

Dans `index.html` :
```html
<h1>Projet Terminale SIN</h1>
```

Dans `style.css` :
```css
body { font-family: Arial; }
```

Enregistrez les deux fichiers avec **Ctrl + S**.

## 2. Observer avant d'ajouter

```bash
git status
```

Repérez la zone **Untracked files** : Git voit les nouveaux fichiers, mais ils ne sont pas encore suivis.

## 3. Préparer les fichiers

```bash
git add travail/index.html travail/style.css
git status
```

Observez ce qui a changé.

## 4. Créer le commit et publier

```bash
git commit -m "Défi 02 - Créer le mini-site"
git push
```

## 🔎 Questions d'observation
Aucune réponse écrite n'est encore demandée. Soyez capable d'expliquer :
- ce que signifie **Untracked files** ;
- ce que `git add` a changé dans `git status`.

## ✅ Validation
Sur GitHub : **Actions → Validation des défis → dernière exécution → Summary**.
