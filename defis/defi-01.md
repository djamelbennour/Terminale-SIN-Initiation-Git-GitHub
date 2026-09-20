# Défi 01 — Prendre en main son dépôt et configurer Git

**Niveau : très guidé**

## 🎯 Objectif
Récupérer votre dépôt personnel sur l'ordinateur, l'ouvrir dans Visual Studio Code et vérifier que Git fonctionne.

> Votre enseignant vous a attribué **votre propre copie du dépôt**. Travaillez uniquement dans cette copie.

## 1. Récupérer votre dépôt

1. Ouvrez le dépôt GitHub qui vous a été attribué.
2. Cliquez sur **Code**.
3. Dans **Local → HTTPS**, copiez l'adresse du dépôt.

## 2. Cloner le dépôt

Ouvrez **Visual Studio Code**, puis **Terminal → Nouveau terminal**.

Placez-vous dans le dossier où vous souhaitez travailler, puis tapez :

```bash
git clone URL_DU_DEPOT
```

Remplacez `URL_DU_DEPOT` par l'adresse copiée sur GitHub.

Entrez ensuite dans le dossier créé :

```bash
cd NOM_DU_DEPOT
code .
```

## 3. Vérifier Git

```bash
git --version
```

Vous devez obtenir une ligne commençant par `git version`.

## 4. Configurer votre identité

> Sur les ordinateurs partagés du lycée, nous configurons l'identité **uniquement pour ce dépôt**. N'utilisez pas `--global`.

```bash
git config user.name "Prénom NOM"
git config user.email "prenom.nom@lycee-jeanrostand.fr"
```

Vérifiez :

```bash
git config user.name
git config user.email
```

## 5. Compléter le fichier demandé

Ouvrez `travail/identite.txt` et complétez :
- votre prénom et votre nom ;
- votre classe ;
- la ligne exacte obtenue avec `git --version`.

Enregistrez avec **Ctrl + S**.

## 6. Enregistrer votre premier travail

```bash
git status
git add travail/identite.txt
git commit -m "Défi 01 terminé"
git push
```

> Si GitHub demande une authentification, utilisez **votre propre compte GitHub** dans la fenêtre du navigateur.

## 🔎 Questions d'observation

Aucune réponse écrite n'est demandée pour ce premier défi. Soyez simplement capable d'expliquer :
- à quoi sert `git clone` ;
- la différence entre le dépôt GitHub et sa copie sur l'ordinateur ;
- pourquoi Git enregistre votre identité ;
- le rôle de `git add`, `git commit` et `git push`.

## ✅ Validation

Sur GitHub : **Actions → Validation des défis → dernière exécution → Summary**.

Si le Défi 01 est validé, le **Défi 02** sera affiché.

> Ne modifiez jamais le dossier `.github/`.
