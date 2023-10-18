# WebGL
Ce projet explore la possibilité d'extraire des données 3D à partir de sources web, telles que Google Maps, Sketchfab et Marmoset Viewer. 

Il repose sur le principe fondamental selon lequel ce que l'ordinateur du client voit, l'utilisateur peut également voir et sauvegarder.

Pour illustrer, nous prenons l'exemple d'images en 2D, où le serveur doit redimensionner les images pour éviter que les utilisateurs n'accèdent aux versions haute résolution.

En revanche, lorsqu'il s'agit de données 3D, il devient possible d'accéder aux données brutes du modèle 3D sur l'ordinateur du client. Cependant, il existe des différences majeures entre les images 2D et les modèles 3D, car chaque acteur a son propre format de données, rendant nécessaire la compréhension de la manière dont ces données sont utilisées par le lecteur.

Enfin, bien que des formats de normalisation tels que GLTF existent, les visualiseurs utilisant des techniques de rendu avancées nécessitent souvent des options spécifiques à leur logiciel. 
Ce projet sert de base pour explorer davantage la récupération de données 3D depuis le web, en gardant à l'esprit les spécificités de chaque source de données.
