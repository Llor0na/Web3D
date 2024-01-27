import struct
from tkinter import Tk, filedialog

def read_c_string(file):
    """Lit une chaîne de caractères terminée par un zéro depuis un fichier"""
    string = bytearray()
    while True:
        char = file.read(1)
        if char == b'\0':
            break
        string += char
    return string.decode()

def get_file_size(file):
    """Obtient la taille d'un fichier en octets"""
    current_position = file.tell()
    file.seek(0, 2)
    size = file.tell()
    file.seek(current_position, 0)
    return size

def open_file_dialog():
    """Ouvre une boîte de dialogue pour sélectionner un fichier .mview"""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier .mview", filetypes=[("Fichiers MView", "*.mview")])
    return file_path

try:
    # Demander à l'utilisateur de sélectionner un fichier .mview
    file_path = open_file_dialog()
    
    # Ouvrir le fichier sélectionné en mode binaire
    with open(file_path, 'rb') as file:
        # Obtenir la taille totale du fichier
        end = get_file_size(file)
        
        # Afficher l'en-tête du tableau
        print("| {:<20} | {:<20} | {:<10} | {:<10} | {:<10} |".format("Nom", "Type MIME", "Compressé", "Taille", "Taille brute"))
        print("|" + "-"*22 + "|" + "-"*22 + "|" + "-"*12 + "|" + "-"*12 + "|" + "-"*12 + "|")

        # Lire et afficher les informations pour chaque section du fichier .mview
        while file.tell() < end:
            name = read_c_string(file)
            mime = read_c_string(file)
            
            # Lire les trois entiers non signés de 32 bits (compressed, size, raw_size)
            compressed, size, raw_size = struct.unpack("III", file.read(3*4))
            
            # Afficher les informations sur la section dans un format de tableau
            print("| {:<20} | {:<20} | {:<10} | {:<10} | {:<10} |".format(name, mime, bool(compressed & 1), hex(size), hex(raw_size)))
            
            # Aller à la section suivante dans le fichier
            if file.tell() + size >= end:
                break
            file.seek(size, 1)

except FileNotFoundError:
    print("Le fichier .mview sélectionné n'a pas pu être trouvé.")
except Exception as e:
    print("Une erreur s'est produite : {}".format(e))
