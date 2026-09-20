# 🟢 Défi 01 — Découvrir Git

## 🎯 Objectif
Vérifier que Git fonctionne et configurer votre identité pour **ce dépôt uniquement**.

### 1. Ouvrez le terminal dans VS Code

Dans VS Code : **Terminal → Nouveau terminal**.

### 2. Vérifiez Git

```bash
git --version
```

Vous devez obtenir une ligne commençant par `git version`.

### 3. Configurez votre identité

Sur les ordinateurs partagés du lycée, n'utilisez pas `--global`.

```bash
git config user.name "Prénom NOM"
git config user.email "prenom.nom@lycee-jeanrostand.fr"
```

Vérifiez :

```bash
git config user.name
git config user.email
```

### 4. Complétez le fichier

Ouvrez `travail/identite.txt` et complétez votre nom, votre classe et la ligne obtenue avec `git --version`.

Enregistrez puis exécutez :

```bash
git status
git add travail/identite.txt
git commit -m "Défi 01 - Identifier mon environnement Git"
git push
```

### ✅ Validation
Sur GitHub, ouvrez **Actions → Validation des défis**. Le résumé doit vous indiquer le prochain défi.

> Ne modifiez jamais les fichiers du dossier `.github/`.
