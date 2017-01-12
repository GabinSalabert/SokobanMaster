# -*- coding: utf-8 -*-

import socket
import urllib.request,urllib.parse,urllib.error
import os, sys

def RetrieveLevels():
    try: #Tentative de connection au serveur (Vérification online-mode)
        host = socket.gethostbyname("sokoban.goldheim.fr") #On récupére l'IP du serveur
        s = socket.create_connection((host, 80), 2) #On ouvre un socket.
        connected= True
    except:
        pass
        connected= False

    if connected == True: #Récupération des niveaux si on est connecté.
        urllib.request.urlretrieve('http://sokoban.goldheim.fr/getLevels.php', "levels/levels.skb")

