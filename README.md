# Web3D
Ce projet vise à extraire des données 3D à partir de sites web tels que [Marmoset Viewer](https://marmoset.co/support/viewer/), [Sketchfab](https://sketchfab.com) et [Google Maps](https://www.google.fr/maps/)

L'idée clé est que si vous pouvez voir ces models sur votre ordinateur, vous pouvez également les enregistrer, un peu comme prendre une photo en ligne. Chaque site web a sa propre manière de stocker ces objets 3D, ce qui nécessite de comprendre leurs règles spécifiques.


![anonymous-hacker-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/3118eff1-c827-4534-9368-5be9c658e45b)

An essential mantra for every savvy hacker: whatever data your computer perceives, you too can unearth and preserve. 

--- 

## [Mesh data](https://www.danthree.studio/fr/blog-cgi/qu%27est-ce-qu%27un-modèle-maillé-3d-définition-exemples) 

![image](https://github.com/Llor0na/Web3D/assets/118251856/da72cc77-af0c-40a9-af21-14b30e678950)


Un modèle 3D est essentiellement composé de deux types d'informations : les **attributs des points** (position, couleur, coordonnées de texture, etc.) et la ***topologie*** (relations entre les points). Notre objectif est de trouver et d'exporter ces deux types de données.

## [Inspector](https://support.hostinger.com/fr/articles/2152545-comment-inspecter-les-elements-du-site-web)

![image](https://github.com/Llor0na/Web3D/assets/118251856/7787ea5a-e968-44c9-a2f2-a2589c914ddf)

L'inspecteur web, notamment le Moniteur Réseau, permet d'examiner les requêtes réseau émises par un site web et leurs réponses. Cela nous aide à localiser les données que nous cherchons.

![image](https://github.com/Llor0na/Web3D/assets/118251856/a2515266-d824-4e7c-80fe-5f71f11360b5)

Dans le Moniteur Réseau, En triant les requêtes par taille décroissante, nous repérons un fichier ".mview" ( Marmoset Viewer ) de grande taille, qui est susceptible de contenir les données 3D que nous recherchons. (Copier > url pour télécharger le fichier mview)

![image](https://github.com/Llor0na/Web3D/assets/118251856/79256194-c3bf-4744-a6ad-a9757367ac26)


Dans le débogueur, nous examinons le code source du Marmoset Viewer "marmoset.js". Les noms de fonctions ont du sens, bien que certaines variables soient représentées par des lettres (a, b, c, d, etc.). Cela nous aide à comprendre comment les données sont utilisées ![image](https://github.com/Llor0na/Web3D/assets/118251856/70689856-d9ca-4f5e-94ea-04ab26d1aaaf)

## Start


-  Point d'Entrée : Repérer les requêtes réseau, car le fichier mview est chargé par le visualiseur via une fonction JavaScript appelée XMLHttpRequest.

-  Rechercher les Requêtes : Nous trouvons huit utilisations de XMLHttpRequest, mais nous nous concentrons sur les fonctions génériques fetchText(), fetchBinary() et fetchBinaryIncremental, car elles semblent traiter des données binaires.

-  Analyser fetchBinary() : La fonction fetchBinary() est particulièrement intéressante, car elle est appelée à la fin de la fonction WebViewer.loadScene, ce qui est logique.
En examinant le contenu de fetchBinary(), nous remarquons que ses arguments sont des fonctions de rappel (callbacks), et le deuxième argument est une fonction appelée lorsque le fichier est entièrement chargé.
        
-  Traitement des Données : Dans cette fonction de rappel, les données sont transmises à la méthode scene.load() en utilisant une classe appelée Archive.
La classe Archive agit comme un décodeur ZIP, lisant les fichiers concaténés dans le fichier mview, les décompressant s'ils sont compressés et les stockant par nom.

-  Analyse du Contenu : Le fichier mview est un fichier binaire, mais nous pouvons déjà identifier certaines parties, comme le nom des fichiers et leur type MIME.
Nous pouvons également obtenir des informations sur la taille des fichiers et leur taille brute.
 
