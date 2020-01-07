#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from time import time
import urllib.request
from datetime import datetime
from requests.utils import requote_uri

url = "https://fr.wikipedia.org/w/api.php?action=query&format=json&titles="

nameList = [
            '1928_au_cinéma',
            '1962_au_cinéma',
            '1965_au_cinéma',
            'Aaltra',
            'Ado_Kyrou',
            'Alejandro_Jodorowsky',
            'Alexander_Hammid',
            'Alfred_Hitchcock',
            'Alice_(film,_1988)',
            'Anemic_cinema',
            'Animation_(audiovisuel)',
            'Antonin_Artaud',
            'Arzach',
            'Au-delà_du_réel_(film)',
            'Au_poste_!',
            'Avant-garde_(art)',
            'Benoît_Delépine',
            'Blue_Velvet',
            'Brazil_(film,_1985)',
            'Cache-cache_pastoral',
            'Carlos_Atanes',
            'Cinéma_expérimental',
            'Cinéma_fantastique',
            'Cinéma_structurel',
            'Cinéma_underground',
            'Dadaïsme',
            'Darkened_Room',
            'David_Lynch',
            'Dead_or_Alive_(film,_1999)',
            'Destino',
            'Dominique_Monféry',
            'Doppelherz',
            'El_Topo',
            'Gregory_Peck',
            'Gustave_Kervern',
            'György_Pálfi',
            'Henri_Xhonneux',
            'Inland_Empire_(film)',
            'J\'irai_comme_un_cheval_fou',
            'Jabberwocky_(film)',
            'Jacques_Baratier',
            'Jan_Švankmajer',
            'Jean-Pierre_Jeunet',
            'Jean_Cocteau',
            'Jean_Giraud',
            'Jean_Rollin',
            'Juliette_des_esprits',
            'KO_Kid',
            'Ken_Russell',
            'L\'imitation_du_cinéma',
            'L\'Âge_d\'or_(film,_1930)',
            'L\'Étoile_de_mer_(film,_1928)',
            'La_Belle_et_la_Bête_(film,_1946)',
            'La_Coquille_et_le_Clergyman',
            'Walt_Disney',
            'Wrong_(film)',
            'Wrong_Cops',
            'Écriture_automatique',
            'Cinéma',
]

error = 0
success = 0
count = 0
for name in nameList:
    count += 1
    response = urllib.request.urlopen(requote_uri(url+name))
    resId = json.loads(response.read().decode('utf-8'))
    for key in resId["query"]["pages"]:
        if str(key) == "-1":
            error += 1
            key = "No id found"
        else:
            success += 1
        print("Film: {}  - Wikipedia Id : {}".format(str(name), str(key)))
        

print("Total: {} - Error(s) : {} - Success : {}".format(str(count), str(error), str(success)))