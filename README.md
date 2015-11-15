# qgis-minint-plugin-geocoding

Plugin QGIS pour le géocodage sur le réseau du MININT

## VAGRANT

En dev vous pouvez utiliser vagrant, virtual box doit être installé (quel que soit l'OS)

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
## Fonctionnalités cherchées :

Géocodage et reverse géocodage sur :
- Le socle SIG du ST(SI)² (périmètre sécurité intérieure)
- Nominatim (en reverse proxy) : http://wiki.openstreetmap.org/wiki/Nominatim
- La BAN  (en reverse proxy) : https://adresse.data.gouv.fr/api/

## Plugin de base

Le plugin de base est [qgis-geocoding](https://github.com/elpaso/qgis-geocoding)

Ce plugin intègre la librairie GeoPy (dans libs/geopy) qui permet l'ajout de nouveaux géocodeurs

## Plugin

Le plugin modifié est dans le répertoire ./dist

## Géocodeur du SOCLE SIG SI

On part sur le géocdeur nominatim que l'on adapte au SOCLE.
Les modifications sont relativement simples et portent sur l'url et les paramètres d'appel

## Gécodeur nominatim 

Une adaptation de l'url est normalement la seule chose à faire. Il faut pouvoir passer en direct (problématique DNS à gérer)

## Géocodeur BAN

Mêmes choses à faire que pour le SOCLE

Même problématique de DNS que Nominatim

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



