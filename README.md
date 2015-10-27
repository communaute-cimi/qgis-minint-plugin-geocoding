# qgis-minint-plugin-geocoding

Plugin QGIS pour le géocodage sur le réseau du MININT


## Fonctionnalités cherchées :

Permettre le géocodage sur :
- Le socle SIG de la Sécurité Intérieure
- Nominatim (en reverse proxy)
- BAN (en reverse proxy)

Permettre le reverse géocodage

## Plugin de base

Le plugin de base est [qgis-geocoding](https://github.com/elpaso/qgis-geocoding)

Ce plugin intègre la librairie GeoPy (dans libs/geopy) qui permet l'ajout de nouveaux géocodeurs

## Plugin

Le plugin modifié est dans le répertoire ./dist

## Géocodeur du SOCLE SIG SI

On part sur le géocdeur nominatim que l'on adapte au SOCLE.
Les modifications sont relativement simples et portent sur l'url et les paramètres d'appel

## Gécodeur nominatim 

Une adaptation de l'url est normalement la seule chose à faire.
Il faut pouvoir passer en direct (problématique DNS à gérer)

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



