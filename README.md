# Web3D
Ce projet vise à extraire des données 3D à partir de sites web tels que Marmoset Viewer, Sketchfab et Google Maps. 

L'idée clé est que si vous pouvez voir ces objets sur votre ordinateur, vous pouvez également les enregistrer, un peu comme prendre une photo en ligne. Chaque site web a sa propre manière de stocker ces objets 3D, ce qui nécessite de comprendre leurs règles spécifiques.

Cette initiative constitue une base pour explorer davantage la récupération de données 3D sur le web, tout en gardant un œil sur les particularités de chaque source.

![anonymous-hacker-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/3118eff1-c827-4534-9368-5be9c658e45b)
An essential mantra for every savvy hacker: whatever data your computer perceives, you too can unearth and preserve.

[ Mesh data ]

Un modèle 3D est essentiellement composé de deux types d'informations : les attributs des points (position, couleur, coordonnées de texture, etc.) et la topologie (relations entre les points). Notre objectif est de trouver et d'exporter ces deux types de données.

[ Inspector ]

L'inspecteur web, notamment le Moniteur "Réseau" Network, permet d'examiner les requêtes réseau émises par un site web et leurs réponses. Cela nous aide à localiser les données que nous cherchons.

[ Trouver les données ]

En triant les requêtes par taille décroissante, nous repérons un fichier ".mview" (Pour marmoset viewer ) de grande taille, qui est susceptible de contenir les données 3D que nous recherchons.

[ Code source de Marmoset ]

Nous examinons le code source du Marmoset Viewer, qui n'est pas complètement obscurci. Les noms de fonctions ont du sens, bien que certaines variables soient représentées par des lettres (a, b, c, d, etc.). Cela nous aide à comprendre comment les données sont utilisées.
