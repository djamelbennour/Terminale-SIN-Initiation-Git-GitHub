# 🟠 Défi 08 — Ignorer un fichier sensible

Créez `travail/secret.txt` avec :
```text
FAUX_SECRET_EXERCICE
```

Observez `git status`.

Créez ensuite `travail/.gitignore` contenant :
```text
secret.txt
```

Relancez `git status`. Le fichier `secret.txt` ne doit plus être proposé par Git.

Dans `travail/preuves/defi08.txt`, expliquez le rôle de `.gitignore` et pourquoi un mot de passe réel ne doit jamais être envoyé sur GitHub.

Ajoutez uniquement `.gitignore` et votre preuve, puis committez et poussez.
