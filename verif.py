#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de verification de la conformite d'un dossier de projet
pour les Trophees NSI 2026.
"""

from __future__ import print_function
import io
import os
import re

# Fichiers obligatoires (fichier ou repertoire)
FICHIERS_OBLIGATOIRES = [
    'presentation.md',
    'README.md',
    'LICENSE',
    'requirements.txt',
    'sources',
    'sources/main.py',
]

# Repertoires optionnels
REPERTOIRES_OPTIONNELS = [
    'docs',
    'data',
    'tests',
    'exemples',
]

# Fichiers d'exemple a supprimer (detection par presence)
FICHIERS_EXEMPLE_A_SUPPRIMER = [
    'data/Paris-Roubais_2023.gpx',
    'docs/trouver_adresse.html',
    'sources/trouver_adresse.py',
    'tests/test_trouver_adresse.py',
]

# Fichiers a verifier pour les marqueurs (detection par contenu)
# Format: (chemin, marqueur_a_detecter)
FICHIERS_AVEC_MARQUEURS = [
    ('presentation.md', 'MODELE_PRESENTATION'),
    ('README.md', 'MODELE_README'),
    ('LICENSE', 'MODELE_LICENSE'),
    ('requirements.txt', 'MODELE_REQUIREMENTS'),
]

# Pattern pour valider les lignes de requirements.txt
PATTERN_REQUIREMENT = re.compile(
    r'^[a-zA-Z0-9]([a-zA-Z0-9._-]*[a-zA-Z0-9])?(\[.*\])?(==|>=|<=|>|<|~=|!=)?.*$'
)


def chemin_existe(racine, chemin):
    """Verifie si un chemin existe (fichier ou repertoire)."""
    full_path = os.path.join(racine, chemin)
    return os.path.exists(full_path)


def est_fichier(racine, chemin):
    """Verifie si le chemin est un fichier."""
    full_path = os.path.join(racine, chemin)
    return os.path.isfile(full_path)


def est_repertoire(racine, chemin):
    """Verifie si le chemin est un repertoire."""
    full_path = os.path.join(racine, chemin)
    return os.path.isdir(full_path)


def lire_fichier(racine, chemin):
    """Lit le contenu d'un fichier. Retourne None en cas d'erreur."""
    full_path = os.path.join(racine, chemin)
    try:
        with io.open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None


def verifier_fichiers_obligatoires(racine):
    """Verifie la presence des fichiers et repertoires obligatoires."""
    manquants = []
    for chemin in FICHIERS_OBLIGATOIRES:
        if not chemin_existe(racine, chemin):
            manquants.append(chemin)
    return manquants


def verifier_fichiers_optionnels(racine):
    """Verifie la presence des repertoires optionnels."""
    absents = []
    for repertoire in REPERTOIRES_OPTIONNELS:
        if not est_repertoire(racine, repertoire):
            absents.append(repertoire)
    return absents


def valider_requirements(racine):
    """
    Valide le contenu du fichier requirements.txt.
    Retourne: (valide, est_vide)
    """
    contenu = lire_fichier(racine, 'requirements.txt')
    if contenu is None:
        return (False, False)
    
    lignes_utiles = []
    for ligne in contenu.splitlines():
        ligne = ligne.strip()
        if ligne and not ligne.startswith('#'):
            lignes_utiles.append(ligne)
    
    if len(lignes_utiles) == 0:
        return (False, True)
    
    for ligne in lignes_utiles:
        if not PATTERN_REQUIREMENT.match(ligne):
            return (False, False)
    
    return (True, False)


def detecter_fichiers_exemple(racine):
    """Detecte si des fichiers d'exemple n'ont pas ete remplaces."""
    fichiers_a_supprimer = []
    fichiers_non_remplaces = []
    
    # Detecter les fichiers d'exemple qui doivent etre supprimes
    for chemin in FICHIERS_EXEMPLE_A_SUPPRIMER:
        if chemin_existe(racine, chemin):
            fichiers_a_supprimer.append(chemin)
    
    # Detecter les fichiers avec marqueur (non remplaces)
    for chemin, marqueur in FICHIERS_AVEC_MARQUEURS:
        contenu = lire_fichier(racine, chemin)
        if contenu is not None and marqueur in contenu:
            fichiers_non_remplaces.append(chemin)
    
    return fichiers_a_supprimer, fichiers_non_remplaces


def main():
    """Fonction principale."""
    racine = os.getcwd()
    
    # Collecter les informations
    fichiers_manquants = verifier_fichiers_obligatoires(racine)
    fichiers_optionnels_manquants = verifier_fichiers_optionnels(racine)
    fichiers_a_supprimer, fichiers_non_remplaces = detecter_fichiers_exemple(racine)
    requirements_valide, requirements_vide = valider_requirements(racine)
    
    # Combiner les fichiers d'exemple
    fichiers_exemple = fichiers_a_supprimer + fichiers_non_remplaces
    
    # Afficher les resultats
    a_problemes = False

    print(u'Verification du dossier de projet pour les Trophées NSI 2026')
    print('')

    if fichiers_manquants:
        print(u'Certains fichiers requis sont manquants : ' + ', '.join(fichiers_manquants))
        a_problemes = True
    
    if fichiers_exemple:
        print(u'Certains fichiers sont la version du modèle : ' + ', '.join(fichiers_exemple))
        a_problemes = True

    if not requirements_valide:
        print(u'Le fichier requirements.txt contient des lignes invalides. Vérifiez sa syntaxe, ou recréez-le.')
        a_problemes = True

    if requirements_vide:
        print(u'Note : Le fichier requirements.txt est vide. Vérifiez que votre projet ne nécessite pas de dépendances.')
    
    if not a_problemes:
        if fichiers_optionnels_manquants:
            print(u'Tous les fichiers requis sont présents, votre projet semble prêt !')
            print(u'Certains dossiers optionnels peuvent être ajoutés : ' + ', '.join(fichiers_optionnels_manquants))
        else:
            print(u'Tous les fichiers requis et optionnels sont présents, votre projet semble prêt !')
        
        print(u'Nous vous conseillons de revérifier les détails du dossier de candidature dans le règlement avant de le soumettre.')


if __name__ == '__main__':
    main()
