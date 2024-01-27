import struct
import os
from tkinter import Tk, filedialog

def lire_chaine_c(fichier):
    """Cette fonction lit les données d'un fichier jusqu'à ce qu'un caractère nul soit rencontré,
    et retourne les données lues sous forme de chaîne."""
    chaine = b''
    caractere = fichier.read(1)
    while caractere != b'\0':
        chaine += caractere
        caractere = fichier.read(1)
    return chaine.decode()

def obtenir_taille_fichier(fichier):
    """Cette fonction retourne la taille d'un fichier en octets."""
    position_actuelle = fichier.tell()
    fichier.seek(0, 2)
    taille = fichier.tell()
    fichier.seek(position_actuelle, 0)
    return taille

def ouvrir_boite_dialogue():
    """Ouvre une boîte de dialogue pour sélectionner un fichier .mview"""
    root = Tk()
    root.withdraw()
    fichier_mview = filedialog.askopenfilename(title="Sélectionnez un fichier .mview", filetypes=[("Fichiers MView", "*.mview")])
    root.destroy()
    return fichier_mview

# Sélectionner le fichier .mview avec une boîte de dialogue
archive = ouvrir_boite_dialogue()

# Créer le répertoire de sortie
nom_fichier, extension = os.path.splitext(archive)
repertoire = nom_fichier
if not os.path.exists(repertoire):
    os.makedirs(repertoire)

with open(archive, 'rb') as fichier_archive:
    taille_finale = obtenir_taille_fichier(fichier_archive)
    while True:
        nom = lire_chaine_c(fichier_archive)
        type_mime = lire_chaine_c(fichier_archive)
        compressé, taille, taille_brute = struct.unpack("III", fichier_archive.read(3*4))
        if compressé:
            nom += ".compressed"
        nom_fichier_sortie = os.path.join(repertoire, nom)
        print(nom_fichier_sortie)
        with open(nom_fichier_sortie, 'wb') as fichier_sortie:
            fichier_sortie.write(fichier_archive.read(taille))

        if fichier_archive.tell() >= taille_finale:
            break
