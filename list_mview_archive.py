import struct # importe le module "struct" pour manipuler les données binaires
import tkinter as tk # importe le module "tkinter" pour créer l'interface graphique
from tkinter import filedialog # importe la fonction "filedialog" du module "tkinter"

def read_c_string(file):
    """Lit une chaîne de caractères null-terminée à partir d'un fichier"""
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

def import_mview_file():
    # Ouvre la boîte de dialogue pour sélectionner le fichier .mview
    file_path = filedialog.askopenfilename(filetypes=[("MVIEW Files", "*.mview")])

    try:
        with open(file_path, 'rb') as file:
            end = get_file_size(file)
            files_info = []  # Stocke les informations pour chaque fichier .mview
            while file.tell() < end:
                name = read_c_string(file) # lit le nom du fichier
                mime = read_c_string(file) # lit le type MIME du fichier
                compressed, size, raw_size = struct.unpack("III", file.read(3*4)) # lit les données de taille du fichier
                files_info.append([name, mime, bool(compressed & 1), size, raw_size]) # ajoute les informations du fichier à la liste
                if file.tell() + size >= end:
                    break
                file.seek(size, 1) # passe au fichier suivant
            print_files_info(files_info) # affiche les informations de chaque fichier
    except FileNotFoundError:
        print("Le fichier '{}' n'a pas été trouvé.".format(file_path))
    except Exception as e:
        print("Une erreur s'est produite : {}".format(e))

def print_files_info(files_info):
    """Affiche les informations de chaque fichier .mview"""
    print("Nom\t\tMIME type\t\tCompressé\tTaille\t\tTaille brute")
    for info in files_info:
        name = info[0][:15] if len(info[0]) > 15 else info[0]  # Raccourcit le nom si nécessaire
        mime = info[1][:15] if len(info[1]) > 15 else info[1]  # Raccourcit le type MIME si nécessaire
        compressed = "Oui" if info[2] else "Non"  # affiche "Oui" ou "Non" selon que le fichier est compressé ou non
        size = hex(info[3]) # affiche la taille en hexadécimal
        raw_size = hex(info[4]) # affiche la taille brute en hexadécimal
        print("{}\t{}\t{}\t{}\t{}".format(name.ljust(16), mime.ljust(16), compressed.ljust(10), size.ljust(10), raw_size))

root = tk.Tk() # Crée la fenêtre principale
button = tk.Button(root, text="Importer un fichier .mview", command=import_mview_file) # Crée un bouton pour importer un fichier
button.pack() # place le bouton dans la fenêtre principale
root.mainloop()
