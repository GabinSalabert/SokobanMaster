# -*- coding: utf-8 -*-

from tkinter import *
import random
from sys import *
import socket
import urllib.request,urllib.parse,urllib.error
from time import sleep

def Affichage_Level():
    global PosJoueurX,PosJoueurY,NiveauActuel,NumeroNiveau,NomJoueur,TableauNiveaux,coup,nbReboot,SCORE
    #On récupére les coordonnées de base du joueur
    PosJoueurX = NiveauActuel['InfosDepart']['JoueurX']
    PosJoueurY = NiveauActuel['InfosDepart']['JoueurY']
    coup = 0
    
    def gauche():
        global PosJoueurX,PosJoueurY,coup
        if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == " " : #Si la case à gauche du joueur est libre, alors on effectue la série d'action qui suit
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" : #On vérifie si le joueur n'est pas sur une zone de placement. Si oui, alors on execute ce code
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="." #On redefinie l'ancienne position du joueur comme étant une zone libre
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" " #Sinon, on défini que l'ancienne position du joueur deviens une zone libre
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]= "@" #On définie que la position à gauche de la position actuelle deviens un joueur
            PosJoueurX = PosJoueurX-1 #On définie les nouvelles coordonnées du joueur
            PosJoueurY = PosJoueurY
            redessiner() #On redessine
            
            
        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "." : #Si la zone à côté du joueur est une place, alors :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" : #Si on est déjà sur une zone :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="." #L'ancienne place redeviens une place
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" " #Sinon, ça redeviens une zone libre
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]= "+" #On définie la position du joueur
            PosJoueurX = PosJoueurX-1 #Coordonnées du joueurs
            PosJoueurY = PosJoueurY
            redessiner() #On redessine
            
            
                
        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "$"  or NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "*" : #Si on à une caisse à gauche
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == " " or NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == "." : #On vérifie que la zone est libre/que c'est une place
                
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" : #Si on est déjà sur une zone de placement
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="." #La zone redeviens une zone de placement libre
                else :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" " #Sinon, ça redeviens de l'air
                        
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "*" : #Si l'endroit où on va se déplacer est une étoile, alors la caisse était sur une place
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]="+" #Donc, ça deviens un + car le joueur est sur une zone de placement
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]="@" #Sinon, ça deviens un joueur normal
                                        
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == " " : #Si la zone devant la caisse est libre
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2]="$" #Alors la caisse reste une caisse
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2]="*" #Sinon, on est forcément sur une zone de placement (grâce au if du départ) donc ça deviens une étoile
                PosJoueurX = PosJoueurX-1 #Coordonnées du joueur
                PosJoueurY = PosJoueurY
                redessiner() #On redessine
        coup=coup+1 #On incrémente le compteur de coup de un
        MenuInfUpdate() #On met à jour le menu du bas pour afficher le nombre de coup
        checkfini() #On vérifier si on à fini le niveau.
                
                    

    #Pour les trois autres fonctions (droite, haut, bas, la structure est la même, donc le code n'est pas commenté.)
    def droite():
        global PosJoueurX,PosJoueurY,coup
        if NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1] == " " :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1]= "@"
            PosJoueurX = PosJoueurX+1
            PosJoueurY = PosJoueurY
            redessiner()
            
            
        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1] == "." :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1]= "+"
            PosJoueurX = PosJoueurX+1
            PosJoueurY = PosJoueurY
            redessiner()
            
            

        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1] == "$" or NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1] == "*" :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX+2] == " " or NiveauActuel['Carte'][PosJoueurY][PosJoueurX+2] == "." :
                    
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
                else :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
                        
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1] == "*" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1]="+"
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX+1]="@"
                                            
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX+2] == " " :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX+2]="$"
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX+2]="*"
                PosJoueurX = PosJoueurX+1
                PosJoueurY = PosJoueurY
                redessiner()
        coup=coup+1
        MenuInfUpdate()
        checkfini()
                
    def bas():
        global PosJoueurX,PosJoueurY,coup
        if NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX] == " " :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX]= "@"
            PosJoueurX = PosJoueurX
            PosJoueurY = PosJoueurY+1
            redessiner()
            
            
        elif NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX] == "." :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX]= "+"
            PosJoueurX = PosJoueurX
            PosJoueurY = PosJoueurY+1
            redessiner()
            
            

        elif NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX] == "$"  or NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX] == "*" :
            if NiveauActuel['Carte'][PosJoueurY+2][PosJoueurX] == " " or NiveauActuel['Carte'][PosJoueurY+2][PosJoueurX] == "." :
                
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
                else :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
                        
                if NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX] == "*" :
                    NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX]="+"
                else :
                     NiveauActuel['Carte'][PosJoueurY+1][PosJoueurX]="@"
                                            
                if NiveauActuel['Carte'][PosJoueurY+2][PosJoueurX] == " " :
                    NiveauActuel['Carte'][PosJoueurY+2][PosJoueurX]="$"
                else :
                    NiveauActuel['Carte'][PosJoueurY+2][PosJoueurX]="*"
                PosJoueurX = PosJoueurX
                PosJoueurY = PosJoueurY+1
                redessiner()
        coup=coup+1
        MenuInfUpdate()
        checkfini()
                
    def haut():
        global PosJoueurX,PosJoueurY,coup
        if NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX] == " " :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX]= "@"
            PosJoueurX = PosJoueurX
            PosJoueurY = PosJoueurY-1
            redessiner()
        elif NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX] == "." :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX]= "+"
            PosJoueurX = PosJoueurX
            PosJoueurY = PosJoueurY-1
            redessiner()
        elif NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX] == "$" or NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX] == "*" :
            if NiveauActuel['Carte'][PosJoueurY-2][PosJoueurX] == " " or NiveauActuel['Carte'][PosJoueurY-2][PosJoueurX] == "." :
                    
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
                else :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
                        
                if NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX] == "*" :
                    NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX]="+"
                else :
                    NiveauActuel['Carte'][PosJoueurY-1][PosJoueurX]="@"
                                            
                if NiveauActuel['Carte'][PosJoueurY-2][PosJoueurX] == " " :
                    NiveauActuel['Carte'][PosJoueurY-2][PosJoueurX]="$"
                else :
                    NiveauActuel['Carte'][PosJoueurY-2][PosJoueurX]="*"
                PosJoueurX = PosJoueurX
                PosJoueurY = PosJoueurY-1
                redessiner()
        coup=coup+1
        MenuInfUpdate()
        checkfini()
        
    def MenuInfUpdate(): #Fonction de mise à jour du nombre de coup dans l'affichage
        AffichageCoup = 'Coup n° ' + str(coup) #On crée le texte à afficher dans le bouton
        CoupBouton = Button(AffichageMenu, text=AffichageCoup, width=28, bg="black", activeforeground="white",activebackground="black",fg="white") #On code le bouton
        CoupBouton.grid(row=3, column=3,padx="25px") #On affiche.

    def checkfini():
        Fini = True #De base, on à fini le jeu.
        for j in range(0,23):
            for k in range(0,NiveauActuel['Hauteur']):
                if(NiveauActuel['Carte'][k][j]) ==".": #Si on trouve un . ou un +, c'est que toutes les caisses ne sont pas sur toutes les zones, donc on passe à false.
                    Fini = False
                if(NiveauActuel['Carte'][k][j]) =="+":
                    Fini = False
        if Fini == True : #Si on à rien trouvé dans le tableau qui correspond :
            global SCORE,nbReboot,coup
            nbcaisse = NiveauActuel['nbCaisses'] #On récupére le nombre de caisses pour le score
            SCORE = SCORE + 100*nbcaisse-coup-(50*nbReboot) #On incrémente le score
            AffichageJeu.update() #On met à jour l'affichage
            FenetreJeu.unbind("<Down>") #On désactive les touches pour que le joueur puisse plus bouger
            FenetreJeu.unbind("<Up>")
            FenetreJeu.unbind("<Left>")
            FenetreJeu.unbind("<Right>")
            AffichageJeu.create_text(384,75, text="Niveau terminé ! Chargement du nouveau niveau.", font=('courier', 15, 'bold'), fill="white") #On affiche un petit texte
            AffichageJeu.update() #On met à jour
            sleep(2) #On attends 2s
            FenetreJeu.destroy() #On détruit la fenetre pour passer au niveau suivant.
                
                    
    def quitter(): #Fonction pour tout stopper
        FenetreJeu.destroy() #On détruit la fenetre 
        sys.exit() #On coupe le processus.

  
    def rebootLevel(): #Fonction qui permet de réinitaliser le niveau
        global NiveauActuel,PosJoueurX,PosJoueurY,nbReboot
        nbReboot = nbReboot+1

        #1 - On supprime TOUT : Joueur, caisse, etc... On laisse juste les places et les murs
        for j in range(0,23): 
            for k in range(0,NiveauActuel['Hauteur']):
                if NiveauActuel['Carte'][k][j] =="*" or NiveauActuel['Carte'][k][j] =="+":
                    NiveauActuel['Carte'][k][j] ="."
                elif NiveauActuel['Carte'][k][j] =="@":
                    NiveauActuel['Carte'][k][j] =" "
                elif NiveauActuel['Carte'][k][j] =="$":
                    NiveauActuel['Carte'][k][j] =" "

        #2 - On reset l'emplacement de départ du joueur et on le place sur le damier.
        PosJoueurX = NiveauActuel['InfosDepart']['JoueurX']
        PosJoueurY = NiveauActuel['InfosDepart']['JoueurY']
        NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="@"

        #3 - On remet les caisse à leurs lieux d'origine
        Caisses = NiveauActuel['InfosDepart']['Caisses']
        nbcaisse = len(Caisses)
        for k in range(0,nbcaisse):
            NiveauActuel['Carte'][Caisses[k][1]][Caisses[k][0]] ="$"
    
        redessiner()


    def Next():
        FenetreJeu.destroy() #Pour aller au niveau suivant, on ferme juste la fenetre pour lancer une nouvelle.

#Ces 4 fonctions permettent juste de pouvoir appeller les fonctions depuis l'appui de touche et l'appui de bouton.
    def basfix(event):
        bas()
    def hautfix(event):
        haut()
    def gauchefix(event):
        gauche()
    def droitefix(event):
        droite()
    
    def redessiner(): #La fonction qui redessine le tableau
        AffichageJeu.delete("Jeu") #On supprime tout le contenu du canvas hormis le background
        for j in range(0,24): #On redessine tout...
            for k in range(0,NiveauActuel['Hauteur']):
                if(NiveauActuel['Carte'][k][j]) =="#":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photomur, tag="Jeu")
                    AffichageJeu.pack()
                if(NiveauActuel['Carte'][k][j]) =="$":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photocaisse, tag="Jeu")
                    AffichageJeu.pack()
                if(NiveauActuel['Carte'][k][j]) ==".":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photoplace, tag="Jeu")
                    AffichageJeu.pack()
                if(NiveauActuel['Carte'][k][j]) =="@":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photojoueur, tag="Jeu")
                    AffichageJeu.pack()
                if(NiveauActuel['Carte'][k][j]) =="+":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photojoueurplace,tag="Jeu")
                    AffichageJeu.pack()
                if(NiveauActuel['Carte'][k][j]) =="*":
                    AffichageJeu.create_image(j*32+17,k*32+17,image=photocaisseok,tag="Jeu")
                    AffichageJeu.pack()
        AffichageJeu.pack() #On oublie pas de packer à la fin, c'est important.

    #On crée une nouvelle fenêtre Tk
    FenetreJeu=Tk()
    FenetreJeu.resizable(width=False, height=False)
    FenetreJeu.title("Jeu de Sokoban - Joueur %s - Niveau %s ." % (NomJoueur,NumeroNiveau))
    FenetreJeu.geometry('+10+10') 
    
    #On fabrique un canvas, qui accueillera tout le niveau ensuite
    AffichageJeu=Canvas(FenetreJeu,height=448,width=768, bd=0, highlightthickness=0, relief='ridge')

    #On crée le fond d'écran du canvas.
    photomax = PhotoImage(file="images/bgjeu.ppm")
    AffichageJeu.create_image(0,0,anchor=NW, image=photomax)

    #On pack.
    AffichageJeu.pack()

    #ToS de la photo du mur qui sera utilisée...
    nummur = random.randint(1,2)
    if nummur==1:
        photomur = PhotoImage(file="images/mur_1.ppm")
    else:
        photomur = PhotoImage(file="images/mur_2.ppm")

    #On définie les autres images
    photocaisse = PhotoImage(file="images/caisse.ppm")
    photojoueur = PhotoImage(file="images/joueur.ppm")
    photocaisseok = PhotoImage(file="images/caisseok.ppm")
    photoplace = PhotoImage(file="images/place.ppm")
    photojoueurplace = PhotoImage(file="images/placejoueur.ppm")

    #On dessine !
    redessiner()
    
    #On affiche le menu inférieur
    AffichageMenu = Canvas(FenetreJeu,width=768,relief="ridge",highlightthickness=0, bd="0")

    fondmenu = PhotoImage(file="images/fondmenu.ppm")
    AffichageMenu.create_image(0,0,anchor=NW, image=fondmenu)

    #Boutons de direction
    BoutonGauche = Button(AffichageMenu, text ='←', command=gauche, width=7,bg="black",activeforeground="white",activebackground="black",fg="white")
    BoutonGauche.grid(row=1,column=0,padx="4.5px")
    BoutonDroit = Button(AffichageMenu, text ='→', command=droite, width=7,bg="black",activeforeground="white",activebackground="black",fg="white")
    BoutonDroit.grid(row=1,column=2)
    BoutonHaut = Button(AffichageMenu, text ='↑', command=haut, width=7,bg="black",activeforeground="white",activebackground="black",fg="white")
    BoutonHaut.grid(row=0,column=1,pady="1.5px")
    BoutonBas = Button(AffichageMenu, text ='↓', command=bas, width=7,bg="black",activeforeground="white",activebackground="black",fg="white")
    BoutonBas.grid(row=2,column=1)

    #Quitter / Recommencer
    BoutonQuitter = Button(AffichageMenu, text ='Quitter', command=quitter, width=25,activeforeground="white",activebackground="darkred",bg="darkred",fg="white")
    BoutonQuitter.grid(row=4,column=0,columnspan=3,pady="10px")
    BoutonRecommencer = Button(AffichageMenu, text ='Recommencer', command=rebootLevel, width=25,activeforeground="white",activebackground="darkred",bg="darkred",fg="white")
    BoutonRecommencer.grid(row=4,column=3,columnspan=3,pady="10px")

    #Affichage Statistiques
    AffichageNiveauEnCours = 'Niveau ' + str(NumeroNiveau)
    NiveauBouton = Button(AffichageMenu, text=AffichageNiveauEnCours, width=28, activeforeground="white",activebackground="black",bg="black", fg="white")
    NiveauBouton.grid(row=1, column=3,padx="25px")
    AffichageCoup = 'Coup n° ' + str(coup)
    CoupBouton = Button(AffichageMenu, text=AffichageCoup, width=28, bg="black", activeforeground="white",activebackground="black",fg="white")
    CoupBouton.grid(row=3, column=3,padx="25px")
        
        
    #Navigation entre les niveaux
    BoutonPrecedent = Button(AffichageMenu, text='Niveau précédent', width=33, activeforeground="white",activebackground="black",bg="black", fg="white")
    BoutonPrecedent.grid(row=1, column=5,padx="25px")
    BoutonSuivant = Button(AffichageMenu, text='Niveau suivant', width=33, activebackground="black",activeforeground="white",bg="black", fg="white", command=Next)
    BoutonSuivant.grid(row=3, column=5,padx="25px")
    AffichageMenu.pack()
    
    #Fin du menu du bas
    #On se met à l'écoute des agissements du joueur
    FenetreJeu.bind("<Down>",basfix)
    FenetreJeu.bind("<Up>",hautfix)
    FenetreJeu.bind("<Left>",gauchefix)
    FenetreJeu.bind("<Right>",droitefix)
    FenetreJeu.protocol("WM_DELETE_WINDOW", quitter) #Au cas où on fasse Alt+F4 ou qu'on ferme la fenetre...
    FenetreJeu.mainloop()

def LevelsDecompilation(): #Fonction de décompilation des niveaux
    #Constantes
    LargeurNiveau = 24
    HauteurNiveau = 14

    #On ouvre le fichier levels pour le décompiler
    FichierJeu = open("levels/levels.skb", 'r')
    ContenuNiveaux = FichierJeu.readlines()
    FichierJeu.close()

    TableauNiveaux = [] #Contiendra tout les niveaux
    TableauTemporaireNiveau = [] #Va contenir les lignes d'un seul niveau de manière temporaire
    Map = [] #Va contenir la carte de manière temporaire
    Lignes = 0 #Compte le nombre de lignes de manière temporaire toujours

    for NbLignes in range(len(ContenuNiveaux)): #Tant qu'il y à des lignes...
        ligne = ContenuNiveaux[NbLignes].rstrip('\r\n') #On garde le contenu de la ligne hormis le caractère de retour chariot + de début de ligne
        if ligne != '------------------------------------': #Si la ligne n'est pas un séparateur, on traite.
            TableauTemporaireNiveau.append(ligne) #On ajoute la ligne au tableau temporaire gérant un seul niveau.
            Lignes += 1
        else : #Si la ligne est un séparateur, on à terminé un niveau entier
            #Pour toutes les lignes, on fait en sorte à ce que les lignes aient toutes le même nombre de caractères
            for i in range(Lignes):
                TableauTemporaireNiveau[i]+= ' ' * (LargeurNiveau - len(TableauTemporaireNiveau[i]))

            #Ensuite, on envoie toutes les lignes modifiées vers un tableau qui décompose lettre par lettre pour faire une grille de jeu jouable.
            for x in range(Lignes):
                Map.append([])
            for y in range(LargeurNiveau):
                for z in range(len(TableauTemporaireNiveau)):
                    Map[z].append(TableauTemporaireNiveau[z][y])
                    
            Objectifs= [] #Le tableau va contenir l'ensemble des zones ou les caisses doivent être placées.
            Caisses= [] #Le tableau va contenir l'ensembles des emplacements des caisses au départ.
            NombreCaisses = 0
            
            for x in range(Lignes):
                for y in range(len(Map[x])):
                    if Map[x][y] == '@':
                        JoueurX = y
                        JoueurY = x
                    if Map[x][y] == '.':
                        Objectifs.append((y, x))
                    if Map[x][y] == '$':
                        Caisses.append((y, x))
                        NombreCaisses = NombreCaisses+1

            #On crée ensuite des dictionnaires de données
            InfosNiveauxDepart= {'JoueurX': JoueurX,
                                 'JoueurY': JoueurY,
                                 'Caisses': Caisses}
                
            InfosNiveauxGlobal= {'Carte': Map,
                                 'Objectifs': Objectifs,
                                 'Hauteur':Lignes,
                                 'nbCaisses':NombreCaisses,
                                 'InfosDepart':InfosNiveauxDepart}

            TableauNiveaux.append(InfosNiveauxGlobal)

            #On réinitialise tout le bouzin.

            InfosNiveauDepart = {}
            TableauTemporaireNiveau = [] #Va contenir les lignes d'un seul niveau
            Map = []
            Lignes = 0
            
    return TableauNiveaux

def ProgrammeUrgence(): #Cette fonction crée un fichier levels.skb au cas où il soit manquant !
    OnWrite = open("levels/levels.skb",'w')
    OnWrite.write("""
#########################
#                      #
#  $                  #
#     #.             #
#     ####          #
#                  #
###   #################
#                  #
#     ####          #
#     #.        @    #
#     #               #
#   $                  #
############   ##########
           #####""")
    OnWrite.close()

#Variables globales
PosJoueurX = 0 #Position du joueur en abscisse 
PosJoueurY = 0 #... en ordonnée
TableauNiveaux = [] #Le tableau qui contient tout les niveaux
NiveauActuel = [] #Le tableau qui contient un seul niveau, celui en cours
NumeroNiveau = 0 #Le numéro du niveau en cours
coup = 0
NomJoueur = ""
NiveauMax = 0
SCORE = 0
nbReboot = 0

def Congrats(): #Fonction appellée quand on à fini le jeu

    def QuitterDef(): #Pour quitter, comme plus haut
        FenetreCongrats.destroy()
        sys.exit()
    
    global NomJoueur,SCORE
    urlSend = "http://sokoban.nelva.fr/scoreboard.php?username="+NomJoueur+"&score="+str(SCORE) #On parse l'url permettant l'envoie de donnée via GET
    try:
        urllib.request.urlretrieve(urlSend) #On tente d'envoyer l'info, sinon, on laisse faire.
    except:
        pass
    
    #On crée une nouvelle fenêtre Tk
    FenetreCongrats=Tk()
    FenetreCongrats.resizable(width=False, height=False)
    
    #On fabrique un canvas, qui accueillera tout le niveau ensuite
    AffichageCongrats=Canvas(FenetreCongrats, bd=0, highlightthickness=0, relief='ridge')

    #On crée le fond d'écran du canvas.
    fondcongrats = PhotoImage(file="images/bg.ppm")
    AffichageCongrats.create_image(0,0,anchor=NW, image=fondcongrats)

    #On pack.
    AffichageCongrats.pack()

    splashlol = PhotoImage(file="images/SplashToUse.ppm")
    LabelSplash = Label(AffichageCongrats,image=splashlol, width=312, height=74,borderwidth=0,relief=FLAT,bg="black")
    LabelSplash.pack(side=TOP,pady=10,padx=150)

    AffichageCongrats.create_text(300,120, text="Félicitation", font=('courier', 20, 'bold'), fill="white")
    AffichageCongrats.create_text(300,150, text="Vous venez d'achever le jeu de Sokoban !", font=('courrier', 14, 'bold'), fill="white")
    AffichageCongrats.update()

    QuitButton = Button(AffichageCongrats, text ="Quitter le jeu", width=18,fg="white",bg="#000000",borderwidth=0,activebackground="black",command=QuitterDef,activeforeground="white", font=("Tahoma",16))
    QuitButton.pack(side=TOP,ipadx=45,pady=80,padx=150)

    FenetreCongrats.mainloop()

    

#Programme de lancement principal
def JeuAventure(username):
    global TableauNiveaux #Le tableau qui contient tout les niveaux, à la suite, obtenu via LevelsDecompilation()    global NiveauMax #Le numéro du niveau le plus haut possible
    global NiveauActuel #Le tableau du niveau actuel comprennant toute ses informations
    global NumeroNiveau #Le numéro du tableau actuel
    global NomJoueur #Juste pour affecter le nom d'utilisateur
    
    NomJoueur = username #Affectation de l'username

    #Vérification de l'existence du fichier de niveaux. Si le fichier existe pas, on en crée un avec 1 niveau de test.
    try:
        FichierVerification = open("levels/levels.skb",'r')
        FichierVerification.close()
    except:
        ProgrammeUrgence()

    #Algorithme de décomposition du fichier de niveaux levels.skb.
    TableauNiveaux = LevelsDecompilation()


    #On initialise le numéro de niveau et on défini le nombre de niveau maximum.
    NiveauMax = len(TableauNiveaux)

    for i in range(0,NiveauMax,1):
        NiveauActuel = TableauNiveaux[i] #On rentre les infos dans NiveauActuel.
        NumeroNiveau = i+1 #Le numéro du niveau de manière compréhensible pour un humain (Il n'y à pas de niveau "0" dans un jeu, d'où le "+1".
        Affichage_Level()  #On fait afficher le niveau et on commence le mainloop.
    #Une fois fini, on apelle une petite fonction qui fait juste afficher une fenetre félicitation avec la possibilité de retourner au menu général. ^^
    Congrats()
