# -*- coding: utf-8 -*-

from tkinter import *
import random
from sys import *
from time import sleep

def Affichage_Level():
    global PosJoueurX,PosJoueurY,NiveauActuel,NumeroNiveau,NomJoueur,TableauNiveaux,coup
    #On récupére les coordonnées de base du joueur
    PosJoueurX = NiveauActuel['InfosDepart']['JoueurX']
    PosJoueurY = NiveauActuel['InfosDepart']['JoueurY']
    coup = 0
    
    def gauche():
        global PosJoueurX,PosJoueurY,coup
        if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == " " :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]= "@"
            PosJoueurX = PosJoueurX-1
            PosJoueurY = PosJoueurY
            redessiner()
            
            
        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "." :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
            else :
                NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
            NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]= "+"
            PosJoueurX = PosJoueurX-1
            PosJoueurY = PosJoueurY
            redessiner()
            
            
                
        elif NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "$"  or NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "*" :
            if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == " " or NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == "." :
                
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=="+" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]="."
                else :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX]=" "
                        
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1] == "*" :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]="+"
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX-1]="@"
                                        
                if NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2] == " " :
                    NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2]="$"
                else :
                     NiveauActuel['Carte'][PosJoueurY][PosJoueurX-2]="*"
                PosJoueurX = PosJoueurX-1
                PosJoueurY = PosJoueurY
                redessiner()
        coup=coup+1
        MenuInfUpdate()  
        checkfini()
                
                    

      
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
        
    def MenuInfUpdate():
        AffichageCoup = 'Coup n° ' + str(coup)
        CoupBouton = Button(AffichageMenu, text=AffichageCoup, width=28, bg="black", activeforeground="white",activebackground="black",fg="white")
        CoupBouton.grid(row=3, column=3,padx="25px")

    def checkfini():
        Fini = True
        for j in range(0,23):
            for k in range(0,NiveauActuel['Hauteur']):
                if(NiveauActuel['Carte'][k][j]) ==".":
                    Fini = False
                if(NiveauActuel['Carte'][k][j]) =="+":
                    Fini = False
        if Fini == True :
            AffichageJeu.update()
            FenetreJeu.unbind("<Down>")
            FenetreJeu.unbind("<Up>")
            FenetreJeu.unbind("<Left>")
            FenetreJeu.unbind("<Right>")
            AffichageJeu.create_text(384,75, text="Niveau terminé ! Retour au menu de sélection.", font=('courier', 15, 'bold'), fill="white")
            AffichageJeu.update()
            sleep(2)
            FenetreJeu.destroy()
                
                    
    def quitter():
        FenetreJeu.destroy()
        sys.exit()

    #Fonction réparée (Florian, 16-05-15 02:01)
    def rebootLevel():
        global NiveauActuel,PosJoueurX,PosJoueurY

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
        FenetreJeu.destroy()

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

    #On dessine ! <3
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

            for x in range(Lignes):
                for y in range(len(Map[x])):
                    if Map[x][y] == '@':
                        JoueurX = y
                        JoueurY = x
                    if Map[x][y] == '.':
                        Objectifs.append((y, x))
                    if Map[x][y] == '$':
                        Caisses.append((y, x))

            #On crée ensuite des dictionnaires de données
            InfosNiveauxDepart= {'JoueurX': JoueurX,
                                 'JoueurY': JoueurY,
                                 'Caisses': Caisses}
                
            InfosNiveauxGlobal= {'Carte': Map,
                                 'Objectifs': Objectifs,
                                 'Hauteur':Lignes,
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
    OnWrite.write("#################\n#               #\n# $      @      #\n#               #\n#          .    #\n#               #\n#               #\n#               #\n#################")
    OnWrite.close()

#Constantes
PosJoueurX = 0
PosJoueurY = 0
TableauNiveaux = []
NiveauActuel = []
NumeroNiveau = 0
coup = 0
NomJoueur = ""
NiveauMax = 0
NiveauVoulu = 0

#Programme de lancement principal
def JeuFun(username):
    global TableauNiveaux #Le tableau qui contient tout les niveaux, à la suite, obtenu via LevelsDecompilation()    global NiveauMax #Le numéro du niveau le plus haut possible
    global NiveauActuel #Le tableau du niveau actuel comprennant toute ses informations
    global NumeroNiveau #Le numéro du tableau actuel
    global NomJoueur #Juste pour affecter le nom d'utilisateur
    global NiveauVoulu
    
    NomJoueur = username #Affectation de l'username

    #Vérification de l'existence du fichier de niveaux. Si le fichier existe pas, on en crée un avec 1 niveau de test.
    try:
        FichierVerification = open("levels/levels.skb",'r')
        FichierVerification.close()
    except:
        ProgrammeUrgence()

    #Algorithme de décomposition du fichier de niveaux levels.skb.
    TableauNiveaux = LevelsDecompilation()


    #Deux fonctions car en fait, l'appuie de la touche entrée envoie un event... Et l'appuie sur le bouton n'en envoie pas.
    #On initialise le numéro de niveau et on défini le nombre de niveau maximum.
    NiveauMax = len(TableauNiveaux)
    Play = True
    while Play == True :
        #Donc, si on utilise pas deux fonctions, ça plante. Merci Tkinter, merci Python. <3
        def SelectLevel():
            level = int(ChampLevel.get())
            if level < NiveauMax+1 and level > 0:
                global NiveauVoulu
                NiveauVoulu = level #On retire les espaces avant et après les premières et dernières lettres.
                FenetreSelect.destroy() #Destruction de la fenêtre de login
                

        def SelectLevelKeyStroke(event):
            SelectLevel() #Renvoie à la fonction utilisée. Merci python. <3

        def DestroyWindowInEmergency():  #Au cas où on ferme la fenêtre. Pour pas faire planter ensuite, on défini un username Anonyme et on le return.
            FenetreSelect.destroy()
            sys.exit()

        #Création basique et lambda da la fenêtre Tkinter et du Canvas. C'est assez standard quoi.
        FenetreSelect=Tk()
        FenetreSelect.title("Jeu de Sokoban - Selection du niveau")
        FenetreSelect.resizable(width=False, height=False)
        AffichageSelect=Canvas(FenetreSelect,height=200,width=500, bd=0, highlightthickness=0, relief='ridge')
        AffichageSelect.pack()

        # Image de fond
        photobg = PhotoImage(file="images/bglogin.ppm")
        BackgroundLogin = AffichageSelect.create_image(0,0,anchor=NW, image=photobg)


        AffichageSelect.create_text(310,25, text="Saisissez le numero de niveau voulu", font=('courier', 14, 'bold'), fill="white")

        ChampLevel = Entry(AffichageSelect)
        ChampLevel.config(fg="blue", font=('courrier', 15, 'bold'))
        ChampLevel.bind("<Return>", SelectLevelKeyStroke)
        ChampLevel.pack(side=LEFT,ipadx =80,padx=20,pady=70)

        BoutonLevel = Button(AffichageSelect, text ="Lancer le niveau", command=SelectLevel)
        BoutonLevel.pack(side=LEFT,ipadx =45, padx=20,pady=150)

        FenetreSelect.protocol("WM_DELETE_WINDOW", DestroyWindowInEmergency) #Au cas où on fasse Alt+F4 ou qu'on ferme la fenetre...
        FenetreSelect.mainloop()

        NiveauActuel = TableauNiveaux[NiveauVoulu-1] #On rentre les infos dans NiveauActuel.
        NumeroNiveau = NiveauVoulu
        Affichage_Level()  #On fait afficher le niveau et on commence le mainloop.

