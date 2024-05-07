![Visitor](https://visitor-badge.laobi.icu/badge?page_id=MuNumworks.mu-pygame)
# mu-pygame
**Ce script est fait pour fonctionner sur une calculatrice Numworks, peut importe son OS. Néanmoins, il n'a été testé que sur la version 
1.4.3 de <a href="https://munumworks.github.io/mu-website/">Mu</a>.** <br />

mu-pygame est un script python a destination des calculatrice numworks, ayant pour but de permettre l'utilisation de scripts python faits avec <a href="https://www.pygame.org">pygame</a>. Pour ce faire, il recrée des classes et des fonctions similaires à celles utilisées par pygame. 

### Installation 
Pour installer mu-pygame sur votre calculatrice, plusieurs choix s'offrent à vous.
* Depuis le <a href="https://my.numworks.com/python/systeme-eratz/pygame">site de Numworks</a>, en cliquant sur *envoyer sur ma calculatrice*.
* Depuis le <a href="https://munumworks.github.io/mu-website/Subfiles/script-store.html">script store</a> de Mu (⚠️Ne marche pas encore⚠️).

### Utilisation 
Veillez à renommer le script en `pygame` ou à utiliser 
```py
import mu_pygame as pygame
```
si le nom du script n'est pas déja `pygame` pour une utilisation plus proche de celle du vrai pygame. Sinon 
```py
import pygame
```

### Fonctionnalités prises en charge 
* Initialiser pygame
  ```py
  pygame.init()
  ```
  Initialise mu-pygame, concrètement ne fait rien pour l'instant.


* Définir la fenêtre 
  ```py
  screen = pygame.display.set_mode((320,222))
  ```
  Crée une fenêtre sur la calculatrice, des dimensions spécifiés en argument. 
  A noter que (320,222) est la taille de l'écran utilisable par python sur la Numworks, et que s'ajoute à celà 18 pixels de bandeau pour le titre de la 
  fenêtre. La taille est donc automatiquement redéfinie si y+18 supérieur à 222.
  Ce détail est réglable par les flags
  ```py
  screen = pygame.display.set_mode((320,222), pygame.NOFRAME | pygame.FULLSCREEN)
  ```
  Ne sont pour l'instant supportés que ces deux flags, `pygame.NOFRAME` qui enlève la bordure en haut de la fenètre et `pygame.FULLSCREEN` qui redimensionne   la taille en (320,222 - *la taille de la bordure*)


* Définir le titre de la fenêtre
  ```py
  pygame.display.set_caption("Test mu-pygame")
  ```
  Défini le titre de la fenêtre, prends en argument n'importe quel str


* Mettre à jour la fenêtre
  ```py
  pygame.display.flip()
  ```
  Met à jour la fenêtre


* Remplir l'écran
  ```py
  screen = pygame.display.set_mode((100,100))
  screen.fill((255,255,255))
  ```
  Remplit l'écran de la couleur spécifiée


* Créer des rectangles
  ```py
  rect = pygame.Rect(0,0,10,10)
  ```
  Crée un objet de type pygame.Rect, concrètement un rectangle de position (x, y) et de taille (width, height)


* Détecter la collision entre deux rectangles
  ```py
  rect1 = pygame.Rect(10,10,20,20)
  rect2 = pygame.Rect(20,20,20,20)

  print(rect1.colliderect(rect2))
  ```
  Affiche s'il y a une collision entre les rectangles `rect1` et `rect2` (en l'occurence oui)


* Faire bouger un rectangle
  ```py
  rect = pygame.Rect(10,10,10,1O)
  rect = rect.move(10,10)
  ``` 
  Déplace le rectangle de 10 en abscisse et 10 en ordonnée 
  ```py
  rect = pygame.Rect(10,10,10,10)
  rect.move_to(100,100)
  ```
  Déplace le rectangle à (100,100)


* Dessiner le rectangle
  ```py
  screen = pygame.display.set_mode((100,100))
  rect = pygame.Rect(10,10,10,10)
  pygame.draw.rect(screen, (255,0,0) rect)
  ```
  Dessine le rectangle `rect` sur la surface spécifiée, de la couleur spécifiée


* Dessiner une ligne
  ```py
  screen = pygame.display.set_mode((100,100))
  pygame.draw.line(screen, (255,255,0), (10,10), (80,80))
  ```
  Dessine la ligne de (10,10) à (80,80) sur la surface spécifiée, de la couleur spécifiée
  ⚠️Ne prends pas encore en argument l'épaisseur de la ligne⚠️


* Dessiner un cercle
  ```py
  screen = pygame.display.set_mode((100,100))
  pygame.draw.circle(screen, (0,0,255), (50,50), 10)
  ```
  Dessine le cercle aux coordonnées (50,50), de rayon 10 pixels, sur la fenêtre spécifiée, de la couleur spécifiée
  ⚠️Ne prends pas encore en argument l'épaisseur du cercle⚠️


* Obtenir les touches préssées
  ```py
  keys = pygame.key.get_pressed()
  ```
  Obtient un dictionnaire des touches, et leur état en booléen
  ⚠️Ne fonctionne que pour les touches OK, Flèche du haut, Flèche du bas, Flèche de droite, Flèche de gauche, et Retour⚠️
  

* Constantes
  mu-pygame implémente aussi certaines constantes de pygame
  * `K_DOWN`
  * `K_UP`
  * `K_RIGHT`
  * `K_LEFT`
  * `FULLSCREEN`
  * `NOFRAME`
  
  par obligation, l'ajout de certaines touches spécifiques a été nécessaire
  * `K_OK`
  * `K_BACK`

### Prévisions
Seront ajoutés prochainement les fonctionnalités suivantes
* `pygame.time`
* `pygame.event`
* Plus de touches pour `pygame.key`
* plus de flags pour `pygame.display`

### Contributeurs
* Gauthier M.
* Kojiverse Productions
  
 
