#!/usr/bin/env python3
from pathlib import Path
import os, subprocess, sys

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/"travail"
PROOFS=WORK/"preuves"

def read(p):
    try: return p.read_text(encoding="utf-8",errors="ignore")
    except: return ""

def proof(n):
    p=PROOFS/f"defi{n:02d}.txt"
    return p.exists() and len(read(p).strip())>=30

def git(*args):
    r=subprocess.run(["git",*args],cwd=ROOT,text=True,capture_output=True)
    return r.stdout.strip() if r.returncode==0 else ""

def tracked(p):
    return bool(git("ls-files","--error-unmatch",str(p.relative_to(ROOT))))

def valid(n):
    if n==1: return "git version" in read(WORK/"identite.txt").lower()
    if n==2: return all((WORK/x).exists() for x in ("index.html","style.css"))
    if n==3: return proof(3) and "mon premier projet sin" in read(WORK/"index.html").lower()
    if n==4: return proof(4) and "premier commit" in read(WORK/"index.html").lower()
    if n==5: return proof(5)
    if n==6: return proof(6) and "git diff" in read(WORK/"index.html").lower()
    if n==7: return proof(7) and "erreur a supprimer" not in read(WORK/"index.html").lower()
    if n==8:
        return proof(8) and "secret.txt" in read(WORK/".gitignore") and not tracked(WORK/"secret.txt")
    if n==9: return proof(9) and bool(git("rev-parse","--verify","feature-design"))
    if n==10: return proof(10) and "design sin" in read(WORK/"style.css").lower()
    if n==11: return proof(11) and bool(git("remote","get-url","origin"))
    if n==12:
        t=read(WORK/"projet-final.html").lower()
        return proof(12) and "<h1" in t and "<p" in t
    return False

def diagnostic(n):
    p=PROOFS/f"defi{n:02d}.txt"
    if n>=3 and not p.exists(): return f"Créez travail/preuves/defi{n:02d}.txt et répondez aux questions."
    if n>=3 and len(read(p).strip())<30: return "Votre compte rendu est trop court."
    return "Relisez le défi, enregistrez vos fichiers puis utilisez git status."

completed=0
for n in range(1,13):
    if valid(n): completed=n
    else: break

lines=["# 🎓 Terminale SIN — Progression",""]
if completed==12:
    lines += ["# 🎉 Parcours terminé","Vous avez validé les **12 défis**."]
else:
    nxt=completed+1
    lines += [f"## ✅ Progression : {completed}/12",f"## 🔓 Défi {nxt:02d}",f"**Aide :** {diagnostic(nxt)}",""]
    bank=ROOT/".github"/"bank"/f"defi-{nxt:02d}.md"
    if bank.exists(): lines += ["---","",read(bank)]

summary=os.environ.get("GITHUB_STEP_SUMMARY")
if summary: Path(summary).write_text("\n".join(lines),encoding="utf-8")
print(f"Progression détectée : {completed}/12")
sys.exit(0)
