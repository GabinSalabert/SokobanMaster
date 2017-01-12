# -*- coding: utf-8 -*-
from tkinter import *
from JeuAventure import JeuAventure
from JeuLibre import JeuFun

def Main(username):

    def Quitter(): #Si on ferme la fenetre, on fait en sorte à ce que ça se fasse "proprement" pour éviter des messages d'erreur
        FenetreMenu.destroy()
        exit
        
    def ExitToAdventure(): #On lance le jeu d'aventure
        FenetreMenu.destroy()
        JeuAventure(username)
        exit

    def ExitToFun(): #On lance le mode fun
        FenetreMenu.destroy()
        JeuFun(username)
        exit

    #Nouvelle fenetre Tk
    FenetreMenu=Tk()
    FenetreMenu.resizable(width=False, height=False)

    #Un canvas pour tout afficher
    AffichageMenu=Canvas(FenetreMenu,height=410,width=610, bd=0, highlightthickness=0, relief='ridge')
    AffichageMenu.pack()
    
    # Image de fond
    photobg = PhotoImage(file="images/bg.ppm")
    BackgroundJeu = AffichageMenu.create_image(0,0,anchor=NW, image=photobg)

    #On code les boutons
    splash = PhotoImage(file="images/SplashToUse.ppm")
    LabelSplash = Label(AffichageMenu,image=splash, width=312, height=74,borderwidth=0,relief=FLAT,bg="black")
    LabelSplash.pack(side=TOP,pady=10,padx=150)
    
    BoutonCampain = Button(AffichageMenu, text ="Mode Aventure", width=18,fg="white",bg="#000000",borderwidth=0,activebackground="black",activeforeground="white", font=("Tahoma",16),command=ExitToAdventure)
    BoutonCampain.pack(side=TOP,ipadx=45,pady=10,padx=150)

    BoutonFun = Button(AffichageMenu, text ="Sélection du niveau", width=18,fg="white",bg="#000000",command=ExitToFun,borderwidth=0,activebackground="black",activeforeground="white", font=("Tahoma",16))
    BoutonFun.pack(side=TOP,ipadx=45,pady=10,padx=150)

    BoutonQuit = Button(AffichageMenu,command=Quitter, text ="Quitter", width=18,fg="white",bg="#000000",borderwidth=0,activebackground="black",activeforeground="white", font=("Tahoma",16))
    BoutonQuit.pack(side=TOP,ipadx=45,pady=10,padx=150)

    #On défini le titre de la fenetre
    FenetreMenu.title(u"Jeu du Sokoban - Joueur %s - Menu principal" % (username))

    FenetreMenu.protocol("WM_DELETE_WINDOW", Quitter) #Au cas où on fasse Alt+F4 ou qu'on ferme la fenetre...
    
    FenetreMenu.mainloop()
