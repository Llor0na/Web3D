# Web3D
Ce projet vise à extraire des données 3D à partir de sites web tels que Marmoset Viewer, Sketchfab et Google Maps. 

L'idée clé est que si vous pouvez voir ces objets sur votre ordinateur, vous pouvez également les enregistrer, un peu comme prendre une photo en ligne. Chaque site web a sa propre manière de stocker ces objets 3D, ce qui nécessite de comprendre leurs règles spécifiques.

![anonymous-hacker-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/3118eff1-c827-4534-9368-5be9c658e45b)
An essential mantra for every savvy hacker: whatever data your computer perceives, you too can unearth and preserve.

[ Mesh data ]

Un modèle 3D est essentiellement composé de deux types d'informations : les attributs des points (position, couleur, coordonnées de texture, etc.) et la topologie (relations entre les points). Notre objectif est de trouver et d'exporter ces deux types de données.

[ Inspector ]

L'inspecteur web, notamment le Moniteur Réseau, permet d'examiner les requêtes réseau émises par un site web et leurs réponses. Cela nous aide à localiser les données que nous cherchons.

[ Trouver les données ] 

Dans le Moniteur Réseau, En triant les requêtes par taille décroissante, nous repérons un fichier ".mview" ( Marmoset Viewer ) de grande taille, qui est susceptible de contenir les données 3D que nous recherchons. (Copier > url pour télécharger le fichier mview)

[ Code source de Marmoset ]

Dans Source "débogueur" Nous examinons le code source du Marmoset Viewer "marmoset.js". Les noms de fonctions ont du sens, bien que certaines variables soient représentées par des lettres (a, b, c, d, etc.). Cela nous aide à comprendre comment les données sont utilisées (Inspecteur > l'onglet Débogueur > {} pour prettifier ).

Point d'Entrée :
        Nous cherchons à extraire des données du fichier mview à l'intérieur du visualiseur.
        Notre point de départ idéal est de repérer les requêtes réseau, car le fichier mview est chargé par le visualiseur via une fonction JavaScript appelée XMLHttpRequest.

Rechercher les Requêtes :
        Nous trouvons huit utilisations de XMLHttpRequest, mais nous nous concentrons sur les fonctions génériques fetchText(), fetchBinary() et fetchBinaryIncremental, car elles semblent traiter des données binaires.

Analyser fetchBinary() :
        La fonction fetchBinary() est particulièrement intéressante, car elle est appelée à la fin de la fonction WebViewer.loadScene, ce qui est logique.
        En examinant le contenu de fetchBinary(), nous remarquons que ses arguments sont des fonctions de rappel (callbacks), et le deuxième argument est une fonction appelée lorsque le fichier est entièrement chargé.

Traitement des Données :
        Dans cette fonction de rappel, les données sont transmises à la méthode scene.load() en utilisant une classe appelée Archive.
        La classe Archive agit comme un décodeur ZIP, lisant les fichiers concaténés dans le fichier mview, les décompressant s'ils sont compressés et les stockant par nom.

Analyse du Contenu :
        Le fichier mview est un fichier binaire, mais nous pouvons déjà identifier certaines parties, comme le nom des fichiers et leur type MIME.
        Nous pouvons également obtenir des informations sur la taille des fichiers et leur taille brute.
        Cette étape 
nous permet de comprendre ce que contient le fichier mview.


![anonymous-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/2bb7e07f-59eb-4981-97e9-f006d13356ef)
