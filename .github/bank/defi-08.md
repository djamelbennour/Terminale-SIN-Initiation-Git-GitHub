# 🟠 Défi 08 — Ignorer un fichier sensible

**Niveau : semi-guidé**

## 🎯 Objectif
Comprendre le rôle de `.gitignore` et adopter un bon réflexe de sécurité.

Créez `travail/secret.txt` contenant uniquement :

```text
FAUX_SECRET_EXERCICE
```

> Il s'agit volontairement d'un faux secret pédagogique. N'utilisez jamais un vrai mot de passe.

Observez :

```bash
git status
```

Créez ensuite `travail/.gitignore` contenant :

```text
secret.txt
```

Relancez :

```bash
git status
```

`secret.txt` ne doit plus être proposé comme fichier à suivre.

Dans `travail/preuves/defi08.txt`, expliquez :
1. le rôle de `.gitignore` ;
2. si le fichier `secret.txt` existe toujours sur votre ordinateur ;
3. pourquoi un vrai mot de passe ne doit jamais être versionné.

Ajoutez **uniquement** `travail/.gitignore` et votre preuve. Créez un commit puis poussez-le.
