# Web3D
Ce projet vise à extraire des données 3D à partir de sites web tels que Marmoset Viewer, Sketchfab et Google Maps. 

L'idée clé est que si vous pouvez voir ces objets sur votre ordinateur, vous pouvez également les enregistrer, un peu comme prendre une photo en ligne. Chaque site web a sa propre manière de stocker ces objets 3D, ce qui nécessite de comprendre leurs règles spécifiques.

Cette initiative constitue une base pour explorer davantage la récupération de données 3D sur le web, tout en gardant un œil sur les particularités de chaque source.

![anonymous-hacker-3d-model](https://github.com/Llor0na/Web3D/assets/118251856/3118eff1-c827-4534-9368-5be9c658e45b)
An essential mantra for every savvy hacker: whatever data your computer perceives, you too can unearth and preserve.

[ Mesh data ]
Un modèle 3D est essentiellement composé de deux types d'informations : les attributs des points (position, couleur, coordonnées de texture, etc.) et la topologie (relations entre les points). Notre objectif est de trouver et d'exporter ces deux types de données.

[ Inspecteur du navigateur ]
L'inspecteur du navigateur, notamment le Moniteur Réseau, permet d'examiner les requêtes réseau émises par un site web et leurs réponses. Cela nous aide à localiser les données que nous cherchons.
