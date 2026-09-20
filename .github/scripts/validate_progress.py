#!/usr/bin/env python3
from pathlib import Path
import os, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/"travail"
PROOFS=WORK/"preuves"

def read(path):
    try: return path.read_text(encoding="utf-8",errors="ignore")
    except: return ""

def proof(n, minimum=40):
    p=PROOFS/f"defi{n:02d}.txt"
    return p.exists() and len(read(p).strip())>=minimum

def git(*args):
    r=subprocess.run(["git",*args],cwd=ROOT,text=True,capture_output=True)
    return r.stdout.strip() if r.returncode==0 else ""

def git_ok(*args):
    return subprocess.run(["git",*args],cwd=ROOT,text=True,capture_output=True).returncode==0

def rel(path): return str(path.relative_to(ROOT))

def tracked(path):
    return bool(git("ls-files","--error-unmatch",rel(path)))

def last_commit(path):
    return git("log","-1","--format=%H","--",rel(path))

def history_contains(path,text):
    return bool(git("log","-S",text,"--format=%H","--",rel(path)).strip())

def branch_ref(name):
    for ref in (f"origin/{name}",name,f"refs/remotes/origin/{name}",f"refs/heads/{name}"):
        if git_ok("rev-parse","--verify",ref): return ref
    return ""

def branch_contains(name,commit):
    ref=branch_ref(name)
    return bool(ref and commit and git_ok("merge-base","--is-ancestor",commit,ref))

def valid(n):
    if n==1:
        return "git version" in read(WORK/"identite.txt").lower()

    if n==2:
        return (
            (WORK/"index.html").exists()
            and (WORK/"style.css").exists()
            and history_contains(WORK/"index.html","Projet Terminale SIN")
            and history_contains(WORK/"style.css","font-family")
        )

    if n==3:
        return proof(3) and "mon premier projet sin" in read(WORK/"index.html").lower()

    if n==4:
        return proof(4) and "premier commit" in read(WORK/"index.html").lower()

    if n==5:
        return proof(5)

    if n==6:
        return proof(6) and "découverte de git diff" in read(WORK/"index.html").lower()

    if n==7:
        return proof(7) and "erreur a supprimer" not in read(WORK/"index.html").lower()

    if n==8:
        gi=WORK/".gitignore"
        return proof(8) and gi.exists() and "secret.txt" in read(gi) and not tracked(WORK/"secret.txt")

    if n==9:
        c=last_commit(PROOFS/"defi09.txt")
        return proof(9) and branch_contains("feature-design",c)

    if n==10:
        c=last_commit(PROOFS/"defi10.txt")
        return (
            proof(10)
            and "design sin" in read(WORK/"style.css").lower()
            and branch_contains("feature-design",c)
            and branch_contains("main",c)
        )

    if n==11:
        return proof(11) and bool(git("remote","get-url","origin"))

    if n==12:
        t=read(WORK/"projet-final.html").lower()
        return proof(12) and "<h1" in t and "<p" in t

    return False

def diagnostic(n):
    p=PROOFS/f"defi{n:02d}.txt"
    if n>=3 and not p.exists():
        return f"Le fichier `travail/preuves/defi{n:02d}.txt` est absent. Créez-le et répondez aux questions."
    if n>=3 and len(read(p).strip())<40:
        return f"Le compte rendu `defi{n:02d}.txt` est trop court. Répondez avec des phrases complètes."
    hints={
      1:"Complétez travail/identite.txt avec la ligne obtenue grâce à git --version.",
      2:"Vérifiez index.html et style.css dans travail/ puis assurez-vous qu'ils ont été committés.",
      3:"Vérifiez la phrase demandée dans index.html et votre compte rendu.",
      4:"Vérifiez que index.html contient « Premier commit » et que la preuve est enregistrée.",
      5:"Relancez git log --oneline et complétez le compte rendu avec le hash et le message.",
      6:"Faites git diff avant git add et vérifiez la phrase demandée dans index.html.",
      7:"La chaîne « ERREUR A SUPPRIMER » ne doit plus être présente après git restore.",
      8:"Vérifiez travail/.gitignore et assurez-vous que secret.txt n'est pas suivi par Git.",
      9:"Le compte rendu doit être committé puis publié sur feature-design.",
      10:"Le travail doit être réalisé sur feature-design puis cette branche doit être fusionnée dans main.",
      11:"Vérifiez git remote -v puis répondez aux quatre questions du compte rendu.",
      12:"Vérifiez projet-final.html, votre compte rendu, puis add, commit et push."
    }
    return hints.get(n,"Commencez par git status, relisez le défi puis vérifiez vos fichiers.")

completed=0
for n in range(1,13):
    if valid(n): completed=n
    else: break

lines=["# 🎓 Terminale SIN — Progression",""]
if completed==0:
    lines += ["ℹ️ **Défi 01 à réaliser.**","","Suivez l'énoncé du Défi 01 puis complétez `travail/identite.txt`."]
elif completed>=12:
    lines += ["# 🎉 Parcours terminé","","Vous avez validé les **12 défis**. Vous savez maintenant utiliser les bases de Git et GitHub."]
else:
    nxt=completed+1
    lines += [
      f"## ✅ Progression validée jusqu'au Défi {completed:02d}","",
      f"## 🔓 Défi {nxt:02d} à réaliser","",
      "> Si vous venez de tenter ce défi et qu'il réapparaît ici, il n'est pas encore validé.","",
      f"**Aide au diagnostic :** {diagnostic(nxt)}",""
    ]
    bank=ROOT/".github"/"bank"/f"defi-{nxt:02d}.md"
    lines += ["---","",read(bank)] if bank.exists() else [f"⚠️ Énoncé du Défi {nxt:02d} introuvable."]

summary=os.environ.get("GITHUB_STEP_SUMMARY")
if summary: Path(summary).write_text("\n".join(lines),encoding="utf-8")
print(f"Progression détectée : {completed}/12")
sys.exit(0)
