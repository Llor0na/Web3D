# Web3D
Ce projet vise à extraire des données 3D à partir de sites web tels que [Marmoset Viewer](https://marmoset.co/support/viewer/), [Sketchfab](https://sketchfab.com) et [Google Maps](https://www.google.fr/maps/)

L'idée clé est que si vous pouvez voir ces models sur votre ordinateur, vous pouvez également les enregistrer, un peu comme prendre une photo en ligne. Chaque site web a sa propre manière de stocker ces objets 3D, ce qui nécessite de comprendre leurs règles spécifiques.


![anonymous-hacker-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/3118eff1-c827-4534-9368-5be9c658e45b)

An essential mantra for every savvy hacker: whatever data your computer perceives, you too can unearth and preserve. 

--- 

## [Mesh data](https://fr.wikipedia.org/wiki/Maillage_(structure_de_données))

![image](https://github.com/Llor0na/Web3D/assets/118251856/8232b2cd-b6ec-481d-aecf-a8d60e62d482)


Un modèle 3D est essentiellement composé de deux types d'informations : les **attributs des points** (position, couleur, [coordonnées de texture](https://fr.wikipedia.org/wiki/Cartographie_UV), etc.) et la [topologie](https://youtu.be/cS_03N-e1h4?feature=shared) (relations entre les points). Notre objectif est de trouver et d'exporter ces deux types de données.

## [Inspector](https://support.hostinger.com/fr/articles/2152545-comment-inspecter-les-elements-du-site-web)

![image](https://github.com/Llor0na/Web3D/assets/118251856/7787ea5a-e968-44c9-a2f2-a2589c914ddf)

L'inspecteur web, notamment le Moniteur Réseau, permet d'examiner les requêtes réseau émises par un site web et leurs réponses. Cela nous aide à localiser les données que nous cherchons.

![image](https://github.com/Llor0na/Web3D/assets/118251856/a2515266-d824-4e7c-80fe-5f71f11360b5)

En triant les requêtes par taille décroissante (size), nous repérons un fichier ".mview" ( Marmoset Viewer ) de grande taille, qui est susceptible de contenir les données 3D que nous recherchons. (Cliquer pour télécharger le fichier mview)

![image](https://github.com/Llor0na/Web3D/assets/118251856/558533a3-70f1-498d-a27a-91bb99e6880e)


Dans le **débogueur**, nous examinons le code source du Marmoset Viewer "marmoset.js". Les noms de fonctions ont du sens, bien que certaines variables soient représentées par des lettres (a, b, c, d, etc.). Cela nous aide à comprendre comment les données sont utilisées ![image](https://github.com/Llor0na/Web3D/assets/118251856/70689856-d9ca-4f5e-94ea-04ab26d1aaaf)

![image](https://github.com/Llor0na/Web3D/assets/118251856/3bf9e3a6-4e6a-4573-8a12-f504c29dbe06)


## Marmoset.js


-  Point d'Entrée : Repérer les requêtes réseau, car le fichier mview est chargé par le visualiseur via une fonction JavaScript appelée XMLHttpRequest.
 
![image](https://github.com/Llor0na/Web3D/assets/118251856/65b759ab-1b7f-4b32-a3e3-52dc47c1a4da)





-  Rechercher les Requêtes : Nous trouvons huit utilisations de XMLHttpRequest, mais nous nous concentrons sur les fonctions génériques fetchText(), fetchBinary() et fetchBinaryIncremental, car elles semblent traiter des données binaires.
  
![image](https://github.com/Llor0na/Web3D/assets/118251856/f954c730-62f3-4d51-9e4d-c9f4da27d245)

-  Analyser fetchBinary() : La fonction fetchBinary() est particulièrement intéressante, car elle est appelée à la fin de la fonction WebViewer.loadScene, ce qui est logique.
En examinant le contenu de fetchBinary(), nous remarquons que ses arguments sont des fonctions de rappel (callbacks), et le deuxième argument est une fonction appelée lorsque le fichier est entièrement chargé.
![image](https://github.com/Llor0na/Web3D/assets/118251856/979c6fff-f02c-43aa-a720-cf6250592420)

        
-  Traitement des Données : Dans cette fonction de rappel, les données sont transmises à la méthode scene.load() en utilisant une classe appelée Archive.
La classe Archive agit comme un décodeur ZIP, lisant les fichiers concaténés dans le fichier mview, les décompressant s'ils sont compressés et les stockant par nom.

## .mview

Analyse du Contenu : Le fichier mview est un fichier binaire, mais nous pouvons déjà identifier certaines parties, comme le nom des fichiers et leur type MIME.
Nous pouvons également obtenir des informations sur la taille des fichiers et leur taille brute.

Git Bash
```
xxd wooden_bat_360.mview | less
```

Powershell
```
Get-Content -Encoding Byte -TotalCount 1000 wooden_bat_360.mview | Format-Hex | more
```

![Capture d'écran](https://github.com/Llor0na/Web3D/assets/118251856/b2cc4432-3148-4517-ac21-cb2f20d97802)

## Python 
```
python list_marmoset_archive.py
```
![image](https://github.com/Llor0na/Web3D/assets/118251856/a2c7be8a-51de-4505-b079-db6732f9ebc2)

- compressed (c, potentiellement b) :
        Indique si le fichier est compressé. Le code utilise l'opération bool(compressed & 1) pour vérifier si le bit le moins significatif de compressed est défini.

- size (d) :
        Représente la taille du fichier. C'est la taille du fichier compressé si le fichier est compressé, sinon c'est la taille brute du fichier.

- raw_size (e) :
        Représente la taille (brute) décompressée du fichier. Si le fichier n'est pas compressé, la taille brute pourrait être égal à la taile.














