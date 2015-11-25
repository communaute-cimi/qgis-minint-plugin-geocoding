# qgis-minint-plugin-geocoding

Plugin QGIS pour le géocodage sur le réseau du MININT

## Objectifs

Permettre le géocodage et géocodage inverse sur :
- Le socle SIG du ST(SI)² (périmètre sécurité intérieure)
- Nominatim (en reverse proxy) : http://wiki.openstreetmap.org/wiki/Nominatim
- La BAN  (en reverse proxy) : https://adresse.data.gouv.fr/api/

## Démarrage rapide avec VAGRANT

Afin de tester la réponse des différents géocodeurs testés, vous pouvez utiliser vagrant. Virtual box doit être installé (quel que soit l'OS).

```sh
# Récupérer les sources de ce projet
git clone https://github.com/communaute-cimi/qgis-minint-plugin-geocoding.git

# Installer Vagrant (debian)
apt-get insall vagrant

# Dans le répertoire sources
vagrant up

# Vérifier les fichiers de test : 
# Géocodage sur le socle
curl http://127.0.0.1:8080/soclesigGeocodeResponse.json
# retourne
{"spatialReference":{"wkid":4326,"latestWkid":4326},"candidates":[{"address":"91580, Etrechy","location":{"x":2.1892890545960464,"y":48.48978918977383}}]}

# Reverse sur le socle
curl http://127.0.0.1:8080/soclesigReverseGeocodeResponse.json
# retourne
{"location":{"x":2.3642342330004453,"y":48.82066720000046,"spatialReference":{"wkid":102110,"latestWkid":2154}},"address":{"Street":"37 BOULEVARD VICTOR","Postal":"75015","City":"PARIS 15","Loc_name":"2_AdressInter"}}
```

## Plugin de base

Le plugin de base est [qgis-geocoding](https://github.com/elpaso/qgis-geocoding)

Ce plugin intègre la librairie GeoPy (dans libs/geopy) qui permet l'ajout de nouveaux géocodeurs

La modification consiste en la création d'un nouveau géocodeur et la modification des géocodeurs externes comme Nominatim ou Ban afin de paramétrer les bonnes URL.

## Plugin

Le plugin modifié est dans le répertoire ./src

## Géocodeur du SOCLE SIG SI

C'est un mix du plugin nominatim et arcgis adapté aux signatures appel et réponse propre au SOCLE SIG
Les modifications sont relativement simples et portent sur l'url et les paramètres d'appel

## Gécodeur nominatim et BAN

Une adaptation de l'url est normalement la seule chose à faire. Il faut pouvoir passer en direct (problématique DNS à gérer)

## Tests

Des fichiers .json dans le répertoire ./tests permettent de simuler une réponse pour chaque appel.

### SOCLE-SIG SI

Appel : 

http://host.minint.fr/{token}/rest/services/geocoding/v1/geocode?singleline=91580%20Etrechy&outSR=4326

- {token} désigne un identifiant correspondant à une application
- singleline : l'adresse recherchée
- outSR : le système de coordonnées en sortie

Résutat : 

[soclesigGeocodeResponse.json](./libs/soclesigGeocodeResponse.json)



