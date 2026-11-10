#!/usr/bin/env python3
"""Vérifie la santé du guide : liens externes vivants, et versions synchronisées.

Sans dépendance : bibliothèque standard uniquement.

    python3 scripts/check.py            # tout
    python3 scripts/check.py --sync     # synchronisation des langues seulement
    python3 scripts/check.py --links    # liens externes seulement

Code de sortie 1 si un contrôle échoue, 0 sinon.
"""

import argparse
import concurrent.futures
import pathlib
import re
import sys
import urllib.error
import urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
VERSIONS = {"EN": "README.md", "FR": "README.fr.md", "ES": "README.es.md"}
AUTRES = ["DEPRECATED.md"]

# Certains hôtes refusent les requêtes automatisées ou n'acceptent que GET.
# Les lister ici évite un faux positif hebdomadaire plutôt que de masquer un vrai lien mort.
TOLERES = {
    "www.uc.cn",          # sert un .doc, réponse erratique
    "open.mobile.qq.com",  # bloque les clients non navigateurs
}

UA = "HEAD-guide-linkcheck/1.0 (+https://github.com/david-corroy/HEAD)"


def liens_externes(texte):
    """Les URL http(s) citées en Markdown, dédoublonnées, hors blocs de code."""
    sans_code = re.sub(r"(?s)```.*?```", "", texte)
    return sorted({m.group(1) for m in re.finditer(r"\]\((https?://[^)\s]+)\)", sans_code)})


def tester(url, delai=20):
    """(url, ok, detail). HEAD d'abord, GET en repli : beaucoup d'hôtes refusent HEAD."""
    hote = urllib.parse.urlparse(url).netloc
    if hote in TOLERES:
        return url, True, "toléré"
    for methode in ("HEAD", "GET"):
        requete = urllib.request.Request(url, method=methode, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(requete, timeout=delai) as reponse:
                return url, True, str(reponse.status)
        except urllib.error.HTTPError as err:
            if methode == "HEAD" and err.code in (403, 405, 501):
                continue  # l'hôte n'aime pas HEAD, on retente en GET
            if err.code in (403, 429):
                return url, True, f"{err.code} (anti-robot, non concluant)"
            return url, False, f"HTTP {err.code}"
        except Exception as err:  # noqa: BLE001 — réseau, DNS, TLS, délai dépassé
            if methode == "GET":
                return url, False, type(err).__name__
    return url, False, "inatteignable"


def controle_liens():
    urls = set()
    for fichier in list(VERSIONS.values()) + AUTRES:
        urls |= set(liens_externes((RACINE / fichier).read_text(encoding="utf-8")))
    urls = sorted(urls)
    print(f"Liens externes à vérifier : {len(urls)}")

    casses = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, ok, detail in pool.map(tester, urls):
            if not ok:
                casses.append((url, detail))
                print(f"  CASSÉ  {detail:<28} {url}")

    if casses:
        print(f"\n{len(casses)} lien(s) cassé(s) sur {len(urls)}.")
        return False
    print(f"Les {len(urls)} liens répondent.")
    return True


def empreinte(texte):
    sans_commentaires = re.sub(r"(?s)<!--.*?-->", "", texte)
    return {
        "balises": len(re.findall(r"<(?:meta|link|script)[^>]*>", sans_commentaires)),
        "titres": len(re.findall(r"^#{2,3} ", texte, re.M)),
        "blocs": texte.count("```") // 2,
        "liens": len(re.findall(r"\]\(https?://", re.sub(r"(?s)```.*?```", "", texte))),
    }


def controle_sync():
    """Les trois versions doivent porter la même structure : seule la prose diffère."""
    empreintes = {
        langue: empreinte((RACINE / fichier).read_text(encoding="utf-8"))
        for langue, fichier in VERSIONS.items()
    }
    reference = empreintes["EN"]
    print("Structure des trois versions :")
    for langue, valeurs in empreintes.items():
        print(f"  {langue} : " + "  ".join(f"{cle}={val}" for cle, val in valeurs.items()))

    ecarts = [
        f"{langue}.{cle} = {valeurs[cle]}, attendu {reference[cle]} (EN)"
        for langue, valeurs in empreintes.items()
        if langue != "EN"
        for cle in reference
        if valeurs[cle] != reference[cle]
    ]
    if ecarts:
        print("\nLes versions ont divergé :")
        for ecart in ecarts:
            print(f"  {ecart}")
        print("\nUne balise ajoutée dans une langue doit l'être dans les trois.")
        return False
    print("Les trois versions sont synchronisées.")
    return True


def main():
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument("--links", action="store_true", help="liens externes seulement")
    analyseur.add_argument("--sync", action="store_true", help="synchronisation seulement")
    args = analyseur.parse_args()

    tout = not (args.links or args.sync)
    resultats = []
    if tout or args.sync:
        resultats.append(controle_sync())
        print()
    if tout or args.links:
        resultats.append(controle_liens())

    return 0 if all(resultats) else 1


if __name__ == "__main__":
    sys.exit(main())
