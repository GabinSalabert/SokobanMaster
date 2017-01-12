# -*- coding: utf-8 -*-
from tkinter import *

#C'est la fonction appellée par le programme principal. Elle contient tout.
def Fenetre():
    #Deux fonctions car en fait, l'appuie de la touche entrée envoie un event... Et l'appuie sur le bouton n'en envoie pas.
    #Donc, si on utilise pas deux fonctions, ça plante. Merci Tkinter, merci Python. <3
    def LoginUser(event=42):
        user = ChampPseudo.get()
        if user != "" and user.strip() != "":
            global username
            username = user.strip() #On retire les espaces avant et après les premières et dernières lettres.
            FenetreLogin.destroy() #Destruction de la fenêtre de login
            return username #On renvoie l'username

    def DestroyWindowInEmergency():  #Au cas où on ferme la fenêtre. Pour pas faire planter ensuite, on défini un username Anonyme et on le return.
        global username
        username = "Anonyme"
        FenetreLogin.destroy()
        return username

    #Création basique et lambda da la fenêtre Tkinter et du Canvas. C'est assez standard quoi.
    FenetreLogin=Tk()
    FenetreLogin.title("Jeu de Sokoban - Connexion")
    FenetreLogin.resizable(width=False, height=False)
    AffichageLogin=Canvas(FenetreLogin,height=200,width=500, bd=0, highlightthickness=0, relief='ridge')
    AffichageLogin.pack()

    # Image de fond
    photobg = PhotoImage(file="images/bglogin.ppm")
    BackgroundLogin = AffichageLogin.create_image(0,0,anchor=NW, image=photobg)


    AffichageLogin.create_text(310,25, text="Bienvenue ! Veuillez saisir votre nom d'utilisateur", font=('courier', 14, 'bold'), fill="white")

    ChampPseudo = Entry(AffichageLogin)
    ChampPseudo.config(fg="blue", font=('courrier', 15, 'bold'))
    ChampPseudo.bind("<Return>", LoginUser)
    ChampPseudo.pack(side=LEFT,ipadx =80,padx=20,pady=70)

    BoutonLogin = Button(AffichageLogin, text ="Connection", command=LoginUser)
    BoutonLogin.pack(side=LEFT,ipadx =45, padx=20,pady=150)

    AffichageLogin.create_text(310,200, text="© 2015 - Théo Dunion, Florian Forestier et Gabin Salabert", font=('courier', 12, 'bold'), fill="white")

    FenetreLogin.protocol("WM_DELETE_WINDOW", DestroyWindowInEmergency) #Au cas où on fasse Alt+F4 ou qu'on ferme la fenetre...
    FenetreLogin.mainloop()
    return username #Une fois la fenêtre détruite, il retourne l'username qui va directement s'inscrire dans le fichier principal.
