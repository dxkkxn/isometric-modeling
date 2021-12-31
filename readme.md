#I52 Modelisation isometrique
## Utilisation
```bash 
    $ python main.py
```
## Description
L'archive contient les fichiers suivants détaille' ci-dessous :

main.py : Fichier main (coeur du projet)
parserx.py : Le fichier du premier tp ou le fichier /etc/X11/rgb est parse' et 
il genere un dico avec les noms et les couleurs
color.py : Implémentation du un objet Color
colorframe.py : Implémentation du menu ou l'utilisteur peut choisir des couleurs
ou bouger le plan
rhombus.py : Implémentation du un objet Rhombus pour representer les losanges
cube.py : Implémentation du un objet Cube pour representer les cubes
menubar.py : Fichier contenant la frame superieur (le menu) et ses fontions
plan.py : Implémentation de un objet Plan
aide : Repertoire contenant de fichier .txt pour l'aide
img  : Repertoire contenant les images utilises dans le projet
examples : quelques examples pour que vous puissiez tester la fonctionalite d'ouvrir

## Details
* Les fichiers d'aide on des saut des lignes superflus pour demontrer que les 
hiperliens marcher correctement
* Vous pouvez zoomer et dezoomer avec la roulette du souris
* Vous pouvez vous deplacer avec l'outil dedie' 
* Plan n'est pas une class conteneur car je n'ai pas trouve' necessaire, 
en effet faire un dictionaire global `a tous les cubes suffit car il n'y a pas 
besoin de creer differents conteneurs 

