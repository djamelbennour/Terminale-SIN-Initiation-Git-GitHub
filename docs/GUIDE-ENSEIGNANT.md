# 👨‍🏫 Guide enseignant — Initiation Git & GitHub en Terminale SIN

## Intention pédagogique

Cette activité transpose le principe du parcours BTS CIEL à un niveau Terminale STI2D SIN : **manipuler d'abord, conceptualiser progressivement, puis retirer l'aide**.

Les élèves ne reçoivent pas les 12 défis d'un seul coup. Le défi suivant est affiché dans le résumé GitHub Actions lorsque les éléments attendus sont détectés.

## Progressivité

| Phase | Défis | Guidage | Intention |
|---|---:|---|---|
| Prise en main | 01–03 | Très fort | Sécuriser les premières manipulations |
| Historique | 04–06 | Fort | Comprendre add / commit / log / diff |
| Correction | 07–08 | Moyen | Comprendre que Git aide aussi à corriger et protéger |
| Branches | 09–10 | Moyen | Introduire le travail parallèle sans conflit complexe |
| Autonomie | 11–12 | Faible | Faire expliquer puis réinvestir |

## Compétences travaillées

- suivre une procédure technique ;
- interpréter l'état d'un système à partir d'informations affichées ;
- distinguer travail local et service distant ;
- documenter une démarche ;
- organiser les versions d'un projet numérique ;
- développer progressivement son autonomie.

## Carnet de bord

À partir du Défi 03, chaque élève produit un fichier dans `travail/preuves/`.

Le carnet de bord sert à :
- faire verbaliser ce que fait la commande ;
- éviter une activité réduite au copier-coller ;
- fournir une trace exploitable lors d'une reprise ;
- permettre une vérification automatique minimale.

La validation automatique contrôle une **trace technique**, mais elle ne remplace pas l'évaluation de la compréhension par l'enseignant.

## Différenciation

### Élève en difficulté
Lui demander systématiquement :
1. « Quelle branche utilises-tu ? »
2. « Que dit `git status` ? »
3. « Quel fichier as-tu réellement enregistré ? »
4. « Ton commit existe-t-il dans `git log --oneline` ? »

Éviter de donner immédiatement la commande suivante.

### Élève rapide
Après le Défi 12, proposer :
- `git show` ;
- `git fetch` puis `git pull` ;
- une deuxième branche ;
- une Pull Request ;
- un conflit volontaire simple.

Le document `docs/POUR-ALLER-PLUS-LOIN.md` sert de transition.

## Erreurs utiles

Certaines erreurs sont volontairement provoquées :
- Défi 07 : modification indésirable puis `restore` ;
- Défi 08 : fichier qui ne doit pas être versionné ;
- Défis 09–10 : changement de contexte entre `main` et une branche.

L'objectif est de faire comprendre que Git n'est pas seulement une suite de commandes : c'est un outil pour **observer, enregistrer, isoler et retrouver des états d'un projet**.

## Durée indicative

Selon l'aisance de la classe, prévoir environ **3 à 5 heures**. Il est préférable de répartir l'activité sur plusieurs séances et de faire de courts bilans collectifs après les Défis 03, 08 et 10.

## Points de vigilance

- sur un poste partagé, conserver la configuration d'identité **locale au dépôt** ;
- chaque élève doit travailler dans sa propre copie ;
- ne jamais utiliser de vrais secrets au Défi 08 ;
- rappeler que `git add` ne signifie pas « envoyer sur GitHub » ;
- faire verbaliser la différence entre commit local et push ;
- au Défi 10, vérifier visuellement que l'élève sait dire sur quelle branche il travaille.

## Évaluation possible

Une évaluation courte peut demander à l'élève, sans procédure détaillée :
1. modifier un fichier ;
2. expliquer l'état donné par `git status` ;
3. créer un commit correctement nommé ;
4. publier le travail ;
5. expliquer la différence entre Git et GitHub ;
6. expliquer le rôle d'une branche.

Cela mesure mieux l'autonomie que la simple validation des 12 défis.
