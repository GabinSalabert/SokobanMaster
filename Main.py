# -*- coding: utf-8 -*-

#Includes globaux
from tkinter import *
from time import sleep


#Include fenêtre login
from FenetreLogin import *
from MenuPrincipal import *
from RetrieveLevels import *


#Récupération du nom d'utilisateur
username = Fenetre()
#Récupération des niveaux depuis internet
RetrieveLevels()
#Appel du jeu.
Main(username)

