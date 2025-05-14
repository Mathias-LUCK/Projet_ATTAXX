import math
import tkinter
from tkinter import ttk
import random
import time
import copy
import colorsys
import pygame
from PIL import ImageTk, Image, ImageDraw, ImageSequence
import os

'''
===================
== PROJET ATTAXX ==
===================
Créateurs : Ilyes, Noah, Mathias
Date : 04.12.2023
Efficacité du code : 100%
Créativité : 100% 
Interface : Parfaite
Note : 20/20
Commentaires additionnels : les variables de score sont inversées (bleu est rouge est vice versa) car le code était programmé avec les bleus en haut à gauche et en bas à droite au début mais cela a été changé en cours de route
'''

bon_mdp, lancer_jeu = False, False
tentatives = 0
FonctionBloquée = False
jouer_son = False
ancien_son = None
chemin_fichier = os.path.dirname(os.path.abspath(__file__)) # Donne le chemin du dossier du fichier du programme
temps = []
'''
========================================================================================
== Ces fonctions permettent au programme de joueur les effets sonores et les musiques ==
========================================================================================
'''

def musicbot1():
    pygame.mixer.stop() # Arrête tous les sons qui se jouent 
    
    bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
    bouton_arreter.pack()  # Afficher le bouton "Arrêter"
    pygame.init() # Initialisation de la bibliothèque pygame
    son_bot1 = pygame.mixer.Sound(os.path.join(chemin_fichier, "rainbow-road-mario-kart-8-deluxe-ost.mp3")) # Donne le chemin du son à lire grâce au chemin du dossier du programme pour éviter de le changer à chaque fois qu'on change le programme de dossier
    channel = son_bot1.play(-1) # Joue le son en boucle
    channel.set_volume(0.25)  # Réglage du volume du son de fond à 30%
    while pygame.mixer.music.get_busy():  # Boucle principale pour maintenir la lecture
        continue

def musicbot2():
    pygame.mixer.stop()
    bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
    bouton_arreter.pack()  # Afficher le bouton "Arrêter"
    pygame.init()
    son_bot1 = pygame.mixer.Sound(os.path.join(chemin_fichier, "Skylanders_Spyros_Adventure_Soundtrack-Leviathan_Lagoon.mp3"))
    channel = son_bot1.play(-1)
    channel.set_volume(0.25)
    while pygame.mixer.music.get_busy():
        continue

def musicbot3():
    pygame.mixer.stop()
    bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
    bouton_arreter.pack()  # Afficher le bouton "Arrêter"
    pygame.init()
    son_bot1 = pygame.mixer.Sound(os.path.join(chemin_fichier, "Crazy_Frog_-_Axel_F_Official_Video.mp3"))
    channel = son_bot1.play(loops=-1)
    channel.set_volume(0.25)
    while pygame.mixer.music.get_busy():
        continue

def musicbot4():
    pygame.mixer.stop()
    bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
    bouton_arreter.pack()  # Afficher le bouton "Arrêter"
    pygame.init()
    son_bot1 = pygame.mixer.Sound(os.path.join(chemin_fichier, "Doom_musique.mp3"))
    channel = son_bot1.play(-1)
    channel.set_volume(0.25)
    while pygame.mixer.music.get_busy():
        continue

def musicbot5():
    pygame.mixer.stop()
    bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
    bouton_arreter.pack()  # Afficher le bouton "Arrêter"
    pygame.init()
    son_bot1 = pygame.mixer.Sound(os.path.join(chemin_fichier, "time_to_save_the_world.mp3"))
    channel = son_bot1.play(-1)
    channel.set_volume(0.25)
    while pygame.mixer.music.get_busy():
        continue

def jouer_lancement():
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "lancement.mp3"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

def jouergta():
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "gta.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

def jouermariodefaite():
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "mario_death_sfx.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

def jouermariovictoire():
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "Marios_Victory_Theme.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

def jouerstar():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "Magic_Sound_Effect_No_Copyright_Free_Download.mp3"))
    pygame.mixer.music.set_volume(0.12)
    pygame.mixer.music.play()

def jouer_capture():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "capture.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    

def jouer_bonne_rep():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "Bruitage_bonne_reponse.mp3"))
    pygame.mixer.music.set_volume(0.12)
    pygame.mixer.music.play()

def jouerwrong():
    pygame.init()
    pygame.mixer.music.load(os.path.join(chemin_fichier, "mauvaiserep.mp3"))
    pygame.mixer.music.set_volume(0.12)
    pygame.mixer.music.play()

def changer_volume(val):
    """
    Permet à l'utilisateur de changer le volume du son    
    I : volume de la musique de base
    O : valeur volume variable sur 100 et a 25% de son volume de base
    """
    volume = int(val) / 100*0.25 #fait en sorte que le volume de la musique de fond soit basse (x0.25)
    pygame.mixer.Channel(0).set_volume(volume) # Change le volume


# Classe pour gérer un GIF animé comme fond de fenêtre Tkinter
class GIFAnime(tkinter.Label):
    def __init__(self, master, chemin):
        # Initialisation de la classe parent tk.Label
        self.master = master  # Stocke la référence à la fenêtre parente
        self.gif = Image.open(chemin)  # Charge le GIF à partir du chemin spécifié
        self.frames_gif = []  # Stocke les frames du GIF animé
        self.index = 0  # Indice actuel de la frame affichée
        self.delai = self.gif.info.get("duration", 100)  # Récupère la durée de chaque frame du GIF (par défaut 100 ms)
        self.charger_frames()  # Charge les frames du GIF dans self.frames_gif
        self.creer_label()  # Crée un label pour afficher le GIF animé

    # Charge chaque frame du GIF dans self.frames_gif
    def charger_frames(self):
        try:
            while True:
                self.frames_gif.append(ImageTk.PhotoImage(self.gif))
                self.gif.seek(len(self.frames_gif))
        except EOFError:
            self.gif.seek(0)

    # Crée un label pour afficher le GIF animé en tant que fond de fenêtre
    def creer_label(self):
        super().__init__(self.master)  # Initialise le label avec la fenêtre parente
        self.place(x=0, y=0, relwidth=1, relheight=1)  # Place le label sur toute la fenêtre
        self.animer()  # Démarre l'animation du GIF

    # Anime le GIF en changeant l'image du label à chaque intervalle de temps
    def animer(self):
        self.config(image=self.frames_gif[self.index])  # Affiche la frame actuelle du GIF
        self.index += 1  # Passe à la frame suivante pour la prochaine itération
        if self.index == len(self.frames_gif):  # Si on atteint la dernière frame, retourne au début
            self.index = 0
        self.after(self.delai, self.animer)  # Programme la prochaine itération de l'animation


def mot_de_passe_verif():
    """
    Vérifie si le mot de passe est correct
    I : None
    O : None
    """
    global bon_mdp, tentatives #variables globales
    mdp = "a" # mot de passe à entrer
    max_tentatives = 3 #tentatives maximales autorisées

    while tentatives < max_tentatives : #tant qu'il y a des tentatives restantes

        mdp_entré = zone_entrée.get() # Le mot de passe est celui de la zone d'entrée

        if mdp_entré == "" :
            jouerwrong() #Mauvais mdp
            break #Sort de la boucle car aucun mdp n'est entré

        if mdp_entré == mdp:
            jouer_bonne_rep() # Bon mdp
            bon_mdp = True # Le mot de passe est bon
            fen_mdp.destroy() #Détruit la fenetre
            break #Sort de la boucle

        else:
            jouerwrong() #Mauvais mdp
            tentatives += 1 #empêche les erreurs dues au reste du programme qui s'exécute
            
            zone_entrée.delete(0, tkinter.END) # Supprime le mdp entré car il n'est pas correct
            mdp_txt.config(text=f"Mot de passe incorrect. {max_tentatives - tentatives} tentative{'s' if max_tentatives - tentatives != 1 else ''} restante{'s' if tentatives - tentatives != 1 else ''}.") # Affiche le nombre de tentatives restantes
            break #Sort de la boucle

    if tentatives == max_tentatives:
        fen_mdp.destroy() # Détruit la fenetre si le nombre de tentatives maximales est atteint

# Création de la fenêtre
fen_mdp = tkinter.Tk() # crée la fenêtre
fen_mdp.title("Mot de passe requis") # Titre de la fenetre
fen_mdp.iconbitmap(os.path.join(chemin_fichier, "OIP.ico")) # icone de la fenêtre
fen_mdp.geometry(f"{600}x{600}+{(fen_mdp.winfo_screenwidth()-600)//2}+{(fen_mdp.winfo_screenheight()-600)//2}") #Place la fenêtre au milieu de l'écran
fen_mdp.resizable(0,0) # Empêche l'utilisateur de changer la taille de la fenêtre
fen_mdp.configure(bg="black")



chemin_gif = (os.path.join(chemin_fichier, "PADEL.gif")) 

# Instance de la classe GIFAnime pour afficher le GIF animé en boucle
gif_anime = GIFAnime(fen_mdp, chemin_gif)

# Composants de l'interface utilisateur
mdp_txt = tkinter.Label(fen_mdp, text="MOT DE PASSE :", bg="#f56563", foreground="white", font='Helvetica 18 bold')
mdp_txt.pack(pady=(10, 0), padx=0)


def touche_entrée(event):
    if event.keycode == 13:
        mot_de_passe_verif()

zone_entrée = tkinter.Entry(fen_mdp, show="*")  #Cachel le mdp avec "*"
zone_entrée.bind('<KeyPress>', touche_entrée)

zone_entrée.pack(pady = 5, padx = (0))

mdp_bouton = ttk.Button(fen_mdp, text="Jouer", command=mot_de_passe_verif, cursor = "hand2") # Bouton qui exécute la fonction "mot_de_passe_verif"
mdp_bouton.pack(pady = (5, 10), padx = (0))



# Lancement de la boucle principale
fen_mdp.mainloop() # Affiche la fenêtre

lancer_le_jeu = False # Variable qui permet de lancer le jeu, uniquement si l'utilisateur clique sur "valider"

def eclaircir_couleur(couleur_hex, facteur):
    """
    Permet d'éclarcir ou d'assombrir la couleur
    I : Couleur en HEX, facteur d'assombrissement ou d'éclaircissement
    O : Nouvelle couleur en HEX
    """
    # Convertir la couleur hexadécimale en valeurs RGB
    r, g, b = int(couleur_hex[1:3], 16), int(couleur_hex[3:5], 16), int(couleur_hex[5:7], 16)
    
    # Convertir les valeurs RGB en valeurs HLS (Teinte, Luminosité, Saturation)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    
    # Ajuster la luminosité
    l *= facteur
    l = min(max(l, 0), 0.8)  # Assurer que la luminosité reste dans la plage [0, 1]
    
    # Reconvertir les valeurs HLS en valeurs RGB
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    
    # Convertir les valeurs RGB en couleur hexadécimale
    r, g, b = round(r * 255), round(g * 255), round(b * 255)
    nouvelle_couleur = f"#{r:02x}{g:02x}{b:02x}"  # Format hexadécimal
    
    return nouvelle_couleur

class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # Définir le titre et la taille de la fenêtre
        self.title("Paramètres")
        self.resizable(0, 0)
        self.geometry(f"{300}x{118}+{(self.winfo_screenwidth()-300)//2}+{(self.winfo_screenheight()-118)//4}") #Place la fenêtre au milieu de l'écran

        # Définir l'icône de la fenêtre
        self.iconbitmap(os.path.join(chemin_fichier, "telecharger.ico"))

        # Initialiser les variables
        self.cases_cliquees = ["#db0000", "#1d00db"]
        self.ancienne_case_select = [[None, None], [None, None]]

        # Créer et placer les étiquettes et les champs de saisie
        self.Choisir_nom_1 = tkinter.Label(self, text="Joueur 1 :")
        self.Choisir_nom_1.grid(row=0, column=0)
        self.nom_joueur_1 = tkinter.Entry(self, justify="center", validate="key", validatecommand= (self.register(self.valider_longueur), "%P"))
        self.nom_joueur_1.grid(row=1, column=0, padx=(20, 0))
        self.Choisir_nom_2 = tkinter.Label(self, text="Joueur 2 :")
        self.Choisir_nom_2.grid(row=0, column=1)
        self.nom_joueur_2 = tkinter.Entry(self, justify="center", validate="key", validatecommand= (self.register(self.valider_longueur), "%P"))
        self.nom_joueur_2.grid(row=1, column=1, padx=10)

        # Créer et placer les boutons de sélection de couleur
        self.bouton_couleur_1 = ttk.Button(
            self,
            text="Choisir la couleur",
            cursor="hand2",
            command=lambda: self.choisir_les_couleurs('joueur_1')
        )
        self.bouton_couleur_1.grid(row=2, column=0, padx=(20, 0), pady=8)
        self.bouton_couleur_2 = ttk.Button(
            self,
            text="Choisir la couleur",
            cursor="hand2",
            command=lambda: self.choisir_les_couleurs('joueur_2')
        )
        self.bouton_couleur_2.grid(row=2, column=1, padx=10, pady=8)

        # Créer et placer le bouton de validation
        self.bouton_valider = ttk.Button(
            self,
            text="Valider",
            cursor="hand2",
            command=lambda: self.enregistrer_et_fermer(skip=False)
        )
        self.bouton_valider.grid(row=3, column=0, columnspan=2, pady=(2, 10))

        # Définir les noms par défaut et le drapeau de continuation
        self.nom_1 = 'bleu'
        self.nom_2 = 'rouge'
        self.continuer = False
    
    def valider_longueur(self, texte):
        if len(texte) <= 12:  # Limit to 10 characters
            return True
        else:
            return False

    def clic_sur_case(self, couleur, label_case, joueur) :
        """
        Cette fonction permet de sélectionner la couleur d'une case pour jouer avec en cliquant dessus.
        I : couleur (la couleur de la case), label_case (la case cliquée), joueur (joueur_1 ou joueur_2)
        O : None, mais stocke la couleur dans la liste cases_cliquees
        """
        global label_couleur
        jouerstar()
        
        if joueur == 'joueur_1':
            if self.ancienne_case_select[0][0] is not None:
                self.ancienne_case_select[0][0].configure(bd=2, relief="solid", cursor="hand2") # Réinitialiser la bordure de l'ancienne case
            
            self.cases_cliquees[0] = couleur # Sélectionner la couleur pour joueur_1
            self.ancienne_case_select[0][0] = label_case
            self.ancienne_case_select[0][1] = couleur
            
        # Réinitialiser la bordure de la case précédemment sélectionnée pour joueur_2
        elif joueur == 'joueur_2':
            if self.ancienne_case_select[1][0] is not None:
                self.ancienne_case_select[1][0].configure(bd=2, relief="solid", cursor="hand2") # Réinitialiser la bordure de l'ancienne case
            
            self.cases_cliquees[1] = couleur #Sélectionner la couleur pour joueur_2
            self.ancienne_case_select[1][0] = label_case
            self.ancienne_case_select[1][1] = couleur

        # Configurer la case cliquée pour montrer qu'elle est sélectionnée
        label_case.configure(bd=0, relief="solid", cursor="arrow")

    def choisir_les_couleurs(self, joueur) :
        """
        Cette fonction permet de sélectionner les couleurs des joueurs en cliquant dessus.
        I : joueur (joueur_1 ou joueur_2)
        O : None, mais ouvre une fenêtre pour selectionner la couleur du joueur
        """
        fenetre_couleurs = tkinter.Tk() # Crée la fenêtre
        fenetre_couleurs.title("Sélection des couleurs") # Nomme la fenêtre
        fenetre_couleurs.geometry(f"{400}x{260}+{(fenetre_couleurs.winfo_screenwidth()-400)//2}+{(fenetre_couleurs.winfo_screenheight()-260)//2}") #Place la fenêtre au milieu de l'écran
        fenetre_couleurs.resizable(0,0) # Empêche l'utilisateur de changer la taille de la fenêtre
        fenetre_couleurs.iconbitmap(os.path.join(chemin_fichier, "color-circle.ico"))

        if joueur == 'joueur_1' :
            couleur_1_txt = tkinter.Label(fenetre_couleurs, text="Couleur 1 : ")
            couleur_1_txt.grid(row = 0, column = 0, columnspan = 15, padx = 0, pady = (10,6)) # Cette fenêtre est gérée avec une grille pour afficher les couleurs
            self.creer_grille(fenetre_couleurs, "joueur_1") # Affiche la grille des couleurs du joueur 1
        elif joueur == 'joueur_2' :
            couleur_2_txt = tkinter.Label(fenetre_couleurs, text="Couleur 2 : ")
            couleur_2_txt.grid(row = 0, column = 0, columnspan = 15, padx = 0, pady = (10,6))
            self.creer_grille(fenetre_couleurs, "joueur_2") # Affiche la grille des couleurs du joueur 2
        fermeture = ttk.Button(fenetre_couleurs, text="Fermer", cursor = "hand2", command=fenetre_couleurs.destroy)
        fermeture.grid(row = 20, column = 0, columnspan = 15, pady = 10)

    def creer_grille(self, fen_couleurs, joueur) :
        """
        Cette fonction permet d'afficher les couleurs des joueurs
        I : fen_couleurs (fenêtre de paramètres), joueur (joueur_1 ou joueur_2)
        O : None, mais affiche la grille de sélection
        """
        global label_couleur
        
        self.ancienne_case_select = [[None, None], [None, None]] # Réinitialise les bordures
        nombre_colonnes = 7
        couleurs = self.generer_couleurs(joueur)

        for i, couleur in enumerate(couleurs):
            ligne = i // nombre_colonnes
            colonne = i % nombre_colonnes
            label_couleur = tkinter.Label(fen_couleurs, bg=couleur, width=6, height=3, cursor = "hand2") # Le curseur est une main
            label_couleur.grid(row=ligne + 4, column=colonne, padx=(7, 1), pady=3)
            label_couleur.config(bd = - 3, relief = "solid") 
            label_couleur.config(bd = 2, relief = "solid") # Ajoute une bordure noire

            label_couleur.bind("<Button-1>", lambda event, couleur=couleur, label=label_couleur: self.clic_sur_case(couleur, label, joueur)) # Lorsque l'utilisateur clique sur la couleur, on appelle la fonction clic_sur_case
    
    def generer_couleurs(self, joueur):
        """"
        Renvoie les différentes couleurs en fonction du jouer et en utilisant la fonction eclaircir_couleur()
        I : joueur (joueur_1 ou joueur_2)
        O : couleurs (liste des couleurs)
        """
        if joueur == 'joueur_1' :
            couleurs = [
                eclaircir_couleur("#9b00f5", 0.76),
                eclaircir_couleur("#f000b2", 0.83),
                eclaircir_couleur("#f0005f", 0.82),
                eclaircir_couleur("#f02900", 0.85),
                eclaircir_couleur("#f04300", 0.85),
                eclaircir_couleur("#f09e00", 0.90),
                eclaircir_couleur("#f0d200", 0.90),

                "#9b00f5", 
                "#f000b2", 
                "#f0005f",
                "#f02900",
                "#f04300",
                "#f09e00",
                "#f0d200",

                eclaircir_couleur("#9b00f5", 1.20),
                eclaircir_couleur("#f000b2", 1.40),
                eclaircir_couleur("#f0005f", 1.42),
                eclaircir_couleur("#f01f00", 1.39),
                eclaircir_couleur("#f04300", 1.36),
                eclaircir_couleur("#f09e00", 1.33),
                eclaircir_couleur("#f0d200", 1.28)
            ]
        
        elif joueur == 'joueur_2':
            couleurs = [
                eclaircir_couleur("#201fff", 0.850),
                eclaircir_couleur("#007af5", 0.865),
                eclaircir_couleur("#00c8f5", 0.865),
                eclaircir_couleur("#00f5c9", 0.865),
                eclaircir_couleur("#00f586", 0.865),
                eclaircir_couleur("#00f535", 0.865),
                eclaircir_couleur("#72f500", 0.865),

                "#201fff",
                "#007af5",
                "#00c8f5",
                "#00f5c9",
                "#00f586",
                "#00f535",
                "#72f500",

                eclaircir_couleur("#201fff", 1.12),
                eclaircir_couleur("#007af5", 1.30),
                eclaircir_couleur("#00c8f5", 1.30),
                eclaircir_couleur("#00f5c9", 1.30),
                eclaircir_couleur("#00f586", 1.30),
                eclaircir_couleur("#00f535", 1.30),
                eclaircir_couleur("#72f500", 1.30)
            ]
        return couleurs 
    
    def enregistrer_et_fermer(self, skip) :
        """
        Enregistre les paramètres et ferme la fenêtre de paramètres
        I : skip (booleen permettant de fermer la fenêtre si l'utilisateur n'a pas renseigné tous les paramètres mais clique sur "continuer")
        O : None, ferme la fenêtre
        """
        global Joueur1, Joueur2, couleur_1, couleur_2, parametres_incomplets, lancer_jeu
        if skip : lancer_jeu = True # Si l'utilisateur a renseigné tous les paramètres ou continue, on peut lancer le jeu
        elif not skip : 
            if not self.nom_joueur_1.get() or not self.nom_joueur_2.get() or not self.cases_cliquees[0] or not self.cases_cliquees[1] :
                parametres_incomplets = tkinter.Tk() # Creer la fenêtre
                parametres_incomplets.title("Attention") # Nomme la fenêtre
                parametres_incomplets.geometry(f"{800}x{85}+{(parametres_incomplets.winfo_screenwidth()-800)//2}+{(parametres_incomplets.winfo_screenheight()-85)//2}") #Place la fenêtre au milieu de l'écran
                parametres_incomplets.resizable(0,0) # Empêche l'utilisateur de changer la taille de la fenêtre
                parametres_incomplets.title("Attention")
                message_erreur = tkinter.Label(parametres_incomplets, text = "Vous n'avez pas configuré tous les paramètres. Ceux que vous n'avez pas configurés seront mis aux paramètres par défaut. Voulez-vous continuer ?")
                message_erreur.grid(row = 0, column = 0, columnspan = 2, padx = 8, pady = 10)
                parametres_incomplets.iconbitmap(os.path.join(chemin_fichier, "warning.ico"))
                bouton_oui = ttk.Button(parametres_incomplets, text="Continuer", cursor = "hand2", command = lambda: self.enregistrer_et_fermer(skip=True))
                bouton_oui.grid(row = 1, column = 0, padx = (200, 0))
                bouton_non = ttk.Button(parametres_incomplets, text="Annuler", cursor = "hand2", command = lambda: parametres_incomplets.destroy())
                bouton_non.grid(row = 1, column = 1, padx = (0, 200))
                return
            else : 
                self.enregistrer_et_fermer(True)

        Joueur1 = self.nom_joueur_1.get() if self.nom_joueur_1.get() else "Joueur 1" # Stocke le nom des joueurs dans des variables globales
        Joueur2 = self.nom_joueur_2.get() if self.nom_joueur_2.get() else "Joueur 2"
        couleur_1 = self.cases_cliquees[0] # Stocke la couleur des joueurs dans des variables globales
        couleur_2 = self.cases_cliquees[1]
        try : parametres_incomplets.destroy() # Supprime la fenêtre si elle existe
        except NameError : pass
        self.destroy()

if bon_mdp == True : # Si le mot de passe est correct, on ouvre la fenêtre de paramètres
    app = Application()
    app.mainloop()

Joueur = 0 # permet de tester avec tour == Joueur/Adversaire (J2) plutot que tour%2 (!)= 0
Adversaire = 1
tour = Joueur # Variable indiquant à qui est le tour (pair = joueur 1, impair = joueur 2)
clic = [1, None] # clic[0] permet de savoir si c'est le deuxième clic du joueur ou non, clic[1] contient les coordonées du premier clic
ContreIA = False # False par défaut (l'utilisateur ne joue pas contre l'IA)
X2, Y2 = 1, 1
tourIA = 1

def Evaluate(board) :
    '''
    Evalue le score de l'IA simplement
    I : plateau
    O : Score de la position pour l'IA
    '''
    ActualiserScoreEval(board)
    return 18*(ScoreRouge - ScoreBleu) + ControleCentral(board)

def EvaluateHard(plateau) :
    '''
    Evalue le score de l'IA avec plus de précision
    I : plateau
    O : Score de la position pour l'IA
    '''
    global PionsCapturés
    ActualiserScore(plateau)
    ScorePionsIsolés = CalculerPionsIsolésEtInfiltrés(plateau)
    return 290*(ScoreRouge - ScoreBleu + 1) + 2*PionsCapturés + 10*ControleCentral(plateau) - 15*RestrictionMouvement(plateau)[0] + 40*RestrictionMouvement(plateau)[1] + 3*ScorePionsIsolés

def CalculerPionsIsolésEtInfiltrés(plateau) :
    Score = 0
    for i in plateau :
        if plateau[i][1] == "rouge" :
            CasesVérifiées = []
            Pion_infiltré = True
            ScorePion = 0
            Pion_isolé = True
            for x in range(-1, 2) :
                for y in range(-1, 2) :
                    X = i[0]+x
                    Y = i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y))
                    if (X, Y) == i or (X, Y) in CasesVérifiées : continue
                    if plateau[X,Y][0] == False : 
                        Pion_infiltré = False
                        CasesVérifiées.append((X, Y))
                        continue
                    elif plateau[X,Y][1] == "rouge" : 
                        Pion_isolé = False
                        ScorePion += 5
                        CasesVérifiées.append((X, Y))
                    elif plateau[X,Y][1] == "bleu" : 
                        ScorePion += 10
                        Pion_isolé = False
                        CasesVérifiées.append((X, Y))
            if Pion_isolé == True : ScorePion -= 15
            if Pion_infiltré == True and i[0] != 1 and i[0] != 7 and i[1] != 1 and i[1] != 7 and i[1] != 1 : ScorePion += 30
            for x in range(-2, 3) :
                for y in range(-2, 3) :
                    if (x, y) in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (-1, 1)] : continue
                    X = i[0]+x
                    Y = i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y))
                    if plateau[X,Y][0] == False : continue
                    if plateau[X,Y][1] == "bleu" : 
                        ScorePion += 25
            if Pion_isolé == True : ScorePion -= 10
            Score += ScorePion
        if plateau[i][1] == "bleu" :
            CasesVérifiées = []
            Pion_infiltré_adv = True
            ScorePion_adv = 0
            Pion_isolé_adv = True
            for x in range(-1, 2) :
                for y in range(-1, 2) :
                    X = i[0]+x
                    Y = i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y))
                    if (X, Y) == i or (X, Y) in CasesVérifiées : continue
                    if plateau[X,Y][0] == False : 
                        Pion_infiltré_adv = False
                        CasesVérifiées.append((X, Y))
                        continue
                    if plateau[X,Y][1] == "rouge" : 
                        Pion_isolé_adv = False
                        ScorePion_adv += 5
                        CasesVérifiées.append((X, Y))
                    if plateau[X,Y][1] == "bleu" : 
                        ScorePion_adv += 10
                        Pion_isolé_adv = False
                        CasesVérifiées.append((X, Y))
            if Pion_isolé_adv == True : ScorePion_adv -= 15
            if Pion_infiltré_adv == True and i[0] != 1 and i[0] != 7 and i[1] != 1 and i[1] != 7 and i[1] != 1 : ScorePion_adv += 100
            Score -= ScorePion_adv
    return Score

def RestrictionMouvement(plateau) :
    '''
    Evalue la restriction de mouvement (combien de coup sans saut possible) pour l'IA et le joueur
    I : plateau
    O : tuple renvoyant des valeurs attribuées à la restriction de mouvement pour chaque joueur
    '''
    NbCoupsLegauxSansSautBleu = 0 # Initialisation des variables
    NbCoupsLegauxSansSautRouge = 0
    for i in plateau :
        CasesVerifiées=[]
        if plateau[i][1] == "bleu" : 
            for x in range(-1, 2) :
                for y in range(-1, 2) :
                    X=i[0]+x
                    Y=i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y))
                    if (X,Y) in CasesVerifiées : continue
                    if plateau[X,Y][0]==False :
                        CasesVerifiées.append((X,Y))
                        NbCoupsLegauxSansSautBleu += 1 #Ajoute 1 si une case à côté d'un pion du joueur est vide
        elif plateau[i][1] ==  "rouge" : 
            for x in range(-1, 2) :
                for y in range(-1, 2) :
                    X=i[0]+x
                    Y=i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y))
                    if (X,Y) in CasesVerifiées : continue
                    if plateau[X,Y][0]==False :
                        CasesVerifiées.append((X,Y))
                        NbCoupsLegauxSansSautRouge += 1 #Ajoute 1 si une case à été d'un pion de l'IA est vide
    return (NbCoupsLegauxSansSautBleu,NbCoupsLegauxSansSautRouge)

def ControleCentral(plateau) :
    """
    Attribue un score pour l'IA en fonction du placement de ces pions sur le plateau, le centre est favorisé
    I : plateau
    O : score placement des pions
    """
    ScorePosition = 0
    nbPions = 0
    for case in plateau :
        if plateau[case][1] == "rouge" :
            nbPions += 1
            if (case[0] == 1 or case[0] == 7) and (case[1] == 1 or case[1] == 7) : ScorePosition += 1 #Plus le pion est centré, plus l'IA a une position avantageuse
            if case[0] == 4 : ScorePosition += 10
            if case[1] == 4 : ScorePosition += 10
            if case[0] == 3 or case[0] == 5 : ScorePosition += 5
            if case[1] == 3 or case[1] == 5 : ScorePosition += 5
            if case[0] == 2 or case[0] == 6 : ScorePosition += 2
            if case[1] == 2 or case[1] == 6 : ScorePosition += 2
    return ScorePosition/10*nbPions

# Fonctions factices à personnaliser pour votre jeu
def check_partie_finie(board):
    """
    Vérifie si la partie est finie ou non
    I : board
    O : True si la partie est finie, False sinon
    """
    global FonctionBloquée
    ActualiserScore(board)
    if (ScoreRouge == 0 or ScoreBleu == 0 or NbCasesVides==0) :
        FonctionBloquée = True
        return True
    elif ScoreBleu>0 and tour == Adversaire and NbCasesVides>0:
        if not(aUnCoupLegal(board, 'bleu')) :
            FonctionBloquée = True
            return False if ContreIA else True
    elif ScoreRouge>0 and tour == Joueur and NbCasesVides>0: 
        if not(aUnCoupLegal(board, 'rouge')) :
            FonctionBloquée = True
            return True
    return False

class IA :
    def __init__(self, difficulté) :
        self.niveau = difficulté # Choisi le niveau
        self.CoupsLegaux = {} # Dictionnaire des coups legaux
        self.jouer_moyen = False, False

    def __str__(self) :
        return self.niveau # Affiche le niveau choisi par l'utilisateur
    
    def Jouer(self) :
        """
        Oriente les actions de l'IA en fonction du niveau choisi
        I : None
        O : None, appel de la fonction appropriée
        """
        global X2, Y2, tour, tourIA, CoupsCalculés

        if self.niveau != "Impossible" and self.niveau != "Difficile" : 
            self.CoupsLegaux = {}
            for i in cases : # Parcourt toutes les cases
                CasesVerifiées=[] # Remet les cases vérifiées à 0 car on cherche les coups légaux à partir d'une autre case
                if cases[i][1]=="rouge" :  # Regarde si la case est occupée par un pion bleu
                    for x in range(-2,3) : # Parcourt toutes les ordonnées
                        for y in range(-2,3) : # Parcourt toutes les abscisses pour chaque ordonnée
                            X=i[0]+x
                            Y=i[1]+y
                            X = max(1, min(7, X))
                            Y = max(1, min(7, Y)) # Empêche les valeurs négatives ou supérieures à 7
                            if (X,Y) in CasesVerifiées : continue # Saute la case si elle a déja été vérifiée
                            if cases[X,Y][0]==False :
                                CasesVerifiées.append((X,Y)) #Ajoute la case aux cases vérifiées pour qu'elle ne soit pas comptée plusieurs fois (lorsque a ou b est négatif et est ramené à 1)
                    self.CoupsLegaux[i]=CasesVerifiées
        
        fenetre.update() # Actualise la fenetre car le calcul du coup l'empêche se s'actualiser

        if self.niveau != ('Difficile' or 'Très difficile') : time.sleep(0.5)
        if self.niveau == 'TrèsFacile' : self.__JouerTrèsFacile(self.CoupsLegaux)
        elif self.niveau == 'Facile' : self.__JouerFacile()
        elif self.niveau == 'Moyen' : 
            if tour == Adversaire :
                self.__JouerMoyen(False)
        elif self.niveau == 'Difficile' : self.__JouerDifficile()
        elif self.niveau == 'Très difficile' : self.__JouerMAX()
        tourIA += 1 # Calcule le nombre de coups joués par l'IA


    def __JouerTrèsFacile(self, saut) :
        """
        Calcule le coup de l'IA pour le niveau "très facile" 
        I : saut, indique si l'IA inclut les coups avec saut ou non dans son calcul
        O : Renvoie un coup aléatoire parmi les coups légaux
        """
        global X2, Y2, tour
        time.sleep(0.35)
        if saut == {} : return
        nouveau_saut = saut.copy()
        for i in saut :
            if not saut[i] :
                del nouveau_saut[i]
        random_key = random.choice(list(nouveau_saut.keys())) #Choix d'un coup au hasard
        x1, y1 = random_key[0], random_key[1]
        random_key2 = random.choice(list(nouveau_saut[random_key]))
        X2, Y2 = random_key2[0], random_key2[1]
        clic[0] = 2
        clic[1] = (x1, y1)
        CreerPion('IA') #Joue le coup

    def __JouerFacile(self) :
        """
        Calcule le coup de l'IA pour le niveau "facile"
        I : None
        O : Renvoie un coup aléatoire parmi les coups legaux si aucun pion ne peut être capturé, sinon renvoie le coup qui capture le plus de pions
        """
        global X2, Y2, tour

        time.sleep(0.35)
        max_pions_captures = 0
        AncienScoreRouge = ScoreRouge
        meilleur_coup = {}

        for i in self.CoupsLegaux :
            for j in self.CoupsLegaux[i] :
                X2, Y2 = j
                pions_captures = CalculerPionsCaptures(cases, X2, Y2)-AncienScoreRouge
                if pions_captures == max_pions_captures :
                    if i not in meilleur_coup : meilleur_coup[i] = [j] # Ajoute le coup aux meilleurs coups
                    else : meilleur_coup[i].append(j)
                elif pions_captures > max_pions_captures:
                    max_pions_captures = pions_captures # Le nouveau nombre de pions capturés maximal
                    meilleur_coup = {} #Réinitialise les meilleures coups car un meilleur coup a été trouvé
                    meilleur_coup[i] = [j] # Ajoute le coup au dictinnaire

        if max_pions_captures != 0: # Si le nombre de pions capturés maximal est different de 0
            clic[0] = 2
            clic[1] = random.choice(list(meilleur_coup.keys())) # Choisissez aléatoirement parmi les coups légaux possibles pour le meilleur coup
            X2, Y2 = random.choice(meilleur_coup[clic[1]])
            CreerPion('IA')
        else : self.__JouerTrèsFacile(self.CoupsLegaux) # Joue un coup aléatoire avec la fonction JouerTrèsFacile

    def __JouerMoyen(self, fromMAX) :
        """
        Calcule le coup de l'IA pour le niveau "moyen"
        I : fromMAX, indique si l'IA joue depuis la fonction JouerMAX
        O : Renvoie un coup aléatoire sans saut parmi les coups legaux si aucun pion ne peut être capturé, sinon renvoie le meilleur coup estimé à une profondeur de 1
        """
        global X2, Y2, tour
        
        if fromMAX :
            time.sleep(1.5) # Maintient une constance au niveau du temps d'attente
        max_pions_captures_avec_saut = 0
        max_pions_captures_sans_saut = 0
        AncienScoreRouge = ScoreRouge
        meilleur_coup = {}
        meilleur_coup_sans_saut = {}
        meilleur_coup_avec_saut = {} # Initialise les variables

        #Même principe que pour la fonction JouerFacile
        for i in self.CoupsLegaux :
            for j in self.CoupsLegaux[i]:
                x1, y1 = i
                X2, Y2 = j
                pions_captures_sans_saut = CalculerPionsCaptures(cases, X2, Y2)-AncienScoreRouge
                pions_captures_avec_saut = CalculerPionsCaptures(cases, X2, Y2)-AncienScoreRouge
                if not Coup_Autorisé(x1, y1, X2, Y2)[1]:
                    if pions_captures_sans_saut == max_pions_captures_sans_saut :
                        if i not in meilleur_coup_sans_saut : meilleur_coup_sans_saut[i] = [[j],pions_captures_sans_saut]
                        else : meilleur_coup_sans_saut[i].append([[j],pions_captures_sans_saut])
                    elif pions_captures_sans_saut > max_pions_captures_sans_saut:
                        max_pions_captures_sans_saut = pions_captures_avec_saut
                        meilleur_coup_sans_saut = {}
                        meilleur_coup_sans_saut[i] = [[j],pions_captures_avec_saut]
                else : 
                    if pions_captures_avec_saut == max_pions_captures_avec_saut :
                        if i not in meilleur_coup_avec_saut : meilleur_coup_avec_saut[i] = [[j],pions_captures_avec_saut]
                        else : meilleur_coup_avec_saut[i].append([[j],pions_captures_avec_saut])
                    elif pions_captures_avec_saut > max_pions_captures_avec_saut:
                        max_pions_captures = pions_captures_avec_saut
                        meilleur_coup_avec_saut = {}
                        meilleur_coup_avec_saut[i] = [[j],pions_captures_avec_saut]

        max_pions_captures=max(max_pions_captures_avec_saut, max_pions_captures_sans_saut)
        if max(max_pions_captures_avec_saut, max_pions_captures_sans_saut) != 0 :
            #Utiliser le meilleur coup avec saut s'il est mieux
            if meilleur_coup_avec_saut and (not meilleur_coup_sans_saut or max_pions_captures >= 2*(max(p[1] for p in meilleur_coup_sans_saut.values())+1)):
                meilleur_coup = {k: v[0] for k, v in meilleur_coup_avec_saut.items()}
            else:
                # Sinon, utilisez les meilleurs coups sans saut
                meilleur_coup = {k: v[0] for k, v in meilleur_coup_sans_saut.items()}
            clic[0] = 2
            clic[1] = random.choice(list(meilleur_coup.keys())) # Choisissez aléatoirement parmi les coups légaux possibles pour le meilleur coup
            X2, Y2 = random.choice(meilleur_coup[clic[1]])
            CreerPion('IA')

        else :
            CoupsLegauxSansSaut = {}
            for i in self.CoupsLegaux :
                for j in self.CoupsLegaux[i]:
                    x1, y1 = i
                    x2, y2 = j
                    if not Coup_Autorisé(x1, y1, x2, y2)[1] :
                        if i not in CoupsLegauxSansSaut : CoupsLegauxSansSaut[i] = [j]
                        else : CoupsLegauxSansSaut[i].append(j) # Ajoute les coups legaux dans le dictionnaire si ils sont sans saut
            if CoupsLegauxSansSaut : self.__JouerTrèsFacile(CoupsLegauxSansSaut) # Si il y a des coups legaux sans saut
            else :
                self.__JouerTrèsFacile(self.CoupsLegaux)

    def __JouerDifficile(self) :
        '''
        Utilise une fonction minimax pour calculer le meilleur coup
        I : None
        O : Renvoie le meilleur coup selon la fonction minimax
        '''
        global X2, Y2, tour, CoupsCalculés
        ActualiserScore(cases)
        ancien_score = ScoreBleu # On enregistre le score actuel
        CoupsCalculés = 0
        start_time = time.time()
        list = minimax(cases, 2, True, False) # On utilise une liste pour éviter d'exécuter la fonction plusieurs fois
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Temps écoulé :", elapsed_time)
        print("Positions calculées", CoupsCalculés) # Affiche le temps écoulé ainsi que le nombre de positions calculées
        clic[1] = list[1]
        X2 = list[2]
        Y2 = list[3]
        CreerPion('IA') # Crée le pion de l'IA
        ActualiserScore(cases)
        if ScoreBleu != ancien_score and not check_partie_finie(cases) : jouer_capture() # Si le score actuel du joueur est différent, un pion a été capturé donc on joue le son
    
    def __JouerMAX(self) :
        '''
        Utilise une fonction minimax pour calculer le meilleur coup avec une meilleure fonction d'évaluation
        I : None
        O : Renvoie le meilleur coup selon la fonction minimax
        '''
        global X2, Y2, tour, tourIA, CoupsCalculés, ancien_score
        ActualiserScore(cases)
        CoupsCalculés = 0
        temps_départ = time.time() # "heure" de départ
        ancien_score_joueur = ScoreBleu
        ancien_score = ScoreRouge
        list = minimax(cases, 2, True, True)
        print(list)
        temps_fin = time.time() # "heure" d'arrêt
        temps_écoulé = round(temps_fin - temps_départ, 100)
        print("Temps écoulé :", temps_écoulé)
        print("Positions calculées", CoupsCalculés)
        clic[1] = list[1]
        X2 = list[2]
        Y2 = list[3]
        CreerPion('IA') # Crée le pion de l'IA
        ActualiserScore(cases)
        if ScoreBleu != ancien_score_joueur and not check_partie_finie(cases) :
            jouer_capture()

def CalculerPionsCaptures(board, x2, y2):
    '''
    Calcule le nombre de pions capturés
    '''
    global cases_simul
    cases_simul = copy.deepcopy(cases)
    if board == cases :
        ChangerCouleurPions(cases_simul, x2, y2, 'rouge')
    ActualiserScore(cases_simul)
    return ScoreRouge

def get_new_board(old_board, x1y1, x2y2, couleur) :
    """
    Actualise le plateau sur un plateau simulé
    I : ancien plateau, coordonnées du pion d'origine, coordonnées du pion de destination, couleur du pion de destination
    O : plateau modifié
    """
    old_board[x2y2] = (True, couleur)
    new_board = ChangerCouleurPions(old_board, x2y2[0], x2y2[1], couleur)
    if Coup_Autorisé(x1y1[0], x1y1[1], x2y2[0], x2y2[1])[1] :
        new_board[x1y1[0], x1y1[1]] = (False, None)
    return new_board

def ChangerCouleurPions(dictionnaire, x1, y1, couleur) :
    '''
    Change la couleur des pions alentour lorsqu'un nouveau pion est placé
    I : plateau, coordonnées du pion, couleur du pion
    O : plateau modifié
    '''
    for x in range(-1,2) : # Ajoute/soustrait à l'ordonnée pour chacune des cases à proximité
        for y in range(-1,2) : # Ajoute/soustrait à l'abscisse pour chacune des cases à proximité
            X=x1+x
            Y=y1+y
            X = max(1, min(7, X))
            Y = max(1, min(7, Y))
            if ChoisirIA.get() == 'Très difficile' or ChoisirIA.get() == 'Difficile' :
                if id(dictionnaire) == id(cases) :
                    if dictionnaire[X,Y][1]=='rouge' and couleur == 'bleu' : # Vérifie si la case est occupée par un pion rouge alors que le pion qui vient d'être placé est bleu
                        dictionnaire[X,Y]=(True,'bleu') # Change la couleur du pion dans le dictionnaire
                        #jouer_capture()
                        plateau.create_oval((X-1)*70+6, (Y-1)*70+6, (X-1)*70+68, (Y-1)*70+68, fill=couleur_1)
                    elif cases[X,Y][1]=='bleu' and couleur == 'rouge' : # Vérifie si la case est occupée par un pion bleu alors que le pion qui vient d'être placé est rouge
                        dictionnaire[X,Y]=(True, 'rouge')
                        plateau.create_oval((X-1)*70+6, (Y-1)*70+6, (X-1)*70+68, (Y-1)*70+68, fill=couleur_2)
                else : 
                    if dictionnaire[X,Y][1]=='rouge' and couleur == 'bleu' : # Vérifie si la case est occupée par un pion rouge alors que le pion qui vient d'être placé est bleu
                        dictionnaire[X,Y]=(True,'bleu') # Change la couleur du pion dans le dictionnaire
                        #jouer_capture()
                    elif cases[X,Y][1]=='bleu' and couleur == 'rouge' : # Vérifie si la case est occupée par un pion bleu alors que le pion qui vient d'être placé est rouge
                        dictionnaire[X,Y]=(True, 'rouge')
            else :  
                if dictionnaire[X,Y][1]=='rouge' and tour%2==0 : # Vérifie si la case est occupée par un pion rouge alors que le pion qui vient d'être placé est bleu
                    if id(dictionnaire) == id(cases) : 
                        plateau.create_oval((X-1)*70+6, (Y-1)*70+6, (X-1)*70+68, (Y-1)*70+68, fill=couleur_1) # Change la couleur du pion en bleu
                        jouer_capture()
                    dictionnaire[X,Y]=(True,'bleu') # Change la couleur du pion dans le dictionnaire
                elif cases[X,Y][1]=='bleu' and tour%2!=0 : # Vérifie si la case est occupée par un pion bleu alors que le pion qui vient d'être placé est rouge
                    if id(dictionnaire) == id(cases) : 
                        plateau.create_oval((X-1)*70+6, (Y-1)*70+6, (X-1)*70+68, (Y-1)*70+68, fill=couleur_2) # Change la couleur du pion en rouge
                        jouer_capture()
                    dictionnaire[X,Y]=(True, 'rouge') # Change la couleur du pion dans le dictionnaire
    return dictionnaire


# Appel initial
def minimax(board, depth, isMaximizing, Impossible):
    '''
    Utilise un algorithme minimax pour déterminer le meilleur coup de l'IA à une profonder de 2 plys
    I : board (l'état actuel de plateau au départ, du plateau simulé ensuite), depth (profondeur maximale), isMaximizing (booléen indiquant si c'est au tour de l'IA dans la simulation ou non), Impossible (booléen indiquant si la fonction d'évaluation est la plus difficile)
    O : Coordonnees du meilleur coup (clic[1], X2, Y2)
    '''
    global clic, cases, CoupsCalculés #, PionsCapturés
    global X2, Y2
    # Vérifiez si la profondeur maximale est atteinte ou si le jeu est terminé
    CoupsCalculés += 1
    #tour1.config(text = f"Coups calculés : {CoupsCalculés}")
    #fenetre.update() #Vous pouvez enlever le commentaire pour voir en temps réel le calcul des coups, peut créer des bugs si vous effectuez des actions pendant cette période

    #if depth == 1 and Impossible :
        #PionsCapturés = ScoreRouge - ancien_score
    if depth == 0 or check_partie_finie(board) :
        #if Impossible : Score = EvaluateHard(board)
        #else : 
        Score = Evaluate(board)
        return [Score, clic[1], X2, Y2]

    couleur = 'rouge' if isMaximizing else 'bleu'
    
    CoupsLegaux = {} # Initialise les coups légaux
    for i in board : # Parcourt toutes les cases
        CasesVerifiées=[] # Remet les cases vérifiées à 0 car on cherche les coups légaux à partir d'une autre case
        if board[i][1]==couleur :  # Regarde si la case est occupée par un pion bleu
            for x in range(-2,3) : # Parcourt toutes les ordonnées
                for y in range(-2,3) : # Parcourt toutes les abscisses pour chaque ordonnée
                    X=i[0]+x
                    Y=i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y)) # Empêche les valeurs négatives ou supérieures à 7
                    if (X,Y) in CasesVerifiées : continue # Saute la case si elle a déja été vérifiée
                    if board[X,Y][0]==False :
                        CasesVerifiées.append((X,Y)) #Ajoute la case aux cases vérifiées pour qu'elle ne soit pas comptée plusieurs fois (lorsque a ou b est négatif et est ramené à 1)
            CoupsLegaux[i]=CasesVerifiées

    #isMaximizing indique que c'est au tour de l'IA pour simuler le coup le plus favorable
    if isMaximizing:
        max_eval = float("-inf") # Le meilleur score est -infini au depart
        for start_coord in CoupsLegaux :
            for end_coord in CoupsLegaux[start_coord]: # Parcourt tous les coups legaux
                new_board = get_new_board(copy.deepcopy(board), start_coord, end_coord, 'rouge') # Simule le coup et crée un nouveau plateau
                evaluation = minimax(new_board, depth - 1, False, Impossible)[0] # Programme récursif pour calculer à la profondeur suivante
                if evaluation > max_eval: # Nouveau meilleur coup trouvé
                    max_eval = evaluation
                    clic[1] = start_coord
                    X2, Y2 = end_coord
        return [max_eval, clic[1], X2, Y2] #Renvoie le meilleur score et le coup pour l'avoir
    
    #Sinon, c'est au tour du joueur et il faut simuler le coup le moins favorable
    if not isMaximizing : 
        min_eval = float("inf") # Pire score est infini au depart
        for start_coord in CoupsLegaux :
            for end_coord in CoupsLegaux[start_coord]:
                new_board = get_new_board(copy.deepcopy(board), start_coord, end_coord, 'bleu')
                evaluation = minimax(new_board, depth - 1, True, Impossible)[0]
                if evaluation < min_eval: # Nouveau pire coup trouvé
                    min_eval = evaluation
        return [min_eval, clic[1], X2, Y2]
    
def CréerPionDebut() :
    '''
    Crée les pions de départ et actualise le dictionnaire cases en conséquence
    I : None
    O : None
    '''
    plateau.create_oval((1-1)*70+6, (1-1)*70+6, (1-1)*70+68, (1-1)*70+68, fill=couleur_1) #Crée les pions de départ
    plateau.create_oval((7-1)*70+6, (7-1)*70+6, (7-1)*70+68, (7-1)*70+68, fill=couleur_1)
    plateau.create_oval((7-1)*70+6, (1-1)*70+6, (7-1)*70+68, (1-1)*70+68, fill=couleur_2)
    plateau.create_oval((1-1)*70+6, (7-1)*70+6, (1-1)*70+68, (7-1)*70+68, fill=couleur_2)
    cases[1,1]=(True, 'bleu') # Change les valeurs de cases en conséquence
    cases[1,7]=(True, 'rouge')
    cases[7,1]=(True, 'rouge')
    cases[7,7]=(True, 'bleu')

def CréerCases(x1=2, y1=2, x2=490, y2=490) :
    '''
    Crée les cases de départ
    I : Coordonnées de départ
    O : None, mais affiche les cases
    '''
    global cases, tour #rend les variables globales
    cases={} # Crée le dictionnaire cases qui stoque des informations pour chaque case
    for x in range(1,8) : # Boucle pour les ordonnées
        for y in range(1,8) : # Boucle pour les abscisses
            cases[(x,y)]=(False, None) # Les cases sont vides par défaut
            case = plateau.create_rectangle(x1, y1, x1+70, y1+70, fill='#E3E3E3')
            x1+=70 # Ajoute 70px à x pour créer la case suivante
        y1+=70 # Ajoute 70px à y pour créer la ligne suivante
        x1=2 # Remet x1 à 2px

def ActualiserScoreEval (dictionnaire) :
    global ScoreBleu, ScoreRouge
    ScoreBleu = sum(1 for i in dictionnaire if dictionnaire[i][1] == 'bleu') # Ajoute un au score si la case est occupée par un pion bleu
    ScoreRouge = sum(1 for i in dictionnaire if dictionnaire[i][1] == 'rouge') # Ajoute un au score si la case est occupée par un pion rouge

def ActualiserScore(dictionnaire) :
    '''
    Permet de compter les pions et d'afficher le score
    I : Dictionnaire (simulé ou réel)
    O : None,  mais stocke les scores dans des variables globales et les affiche
    '''
    global ScoreBleu, ScoreRouge, NbCasesVides, CasesVides # Rend les variables globales
    ScoreBleu = sum(1 for i in dictionnaire if dictionnaire[i][1] == 'bleu') # Ajoute un au score si la case est occupée par un pion bleu
    ScoreRouge = sum(1 for i in dictionnaire if dictionnaire[i][1] == 'rouge') # Ajoute un au score si la case est occupée par un pion rouge
    NbCasesVides=49-ScoreBleu-ScoreRouge
    CasesVides=[i for i in dictionnaire if dictionnaire[i][0] == False] # Soustrait les deux scores au nombre de cases de départ pour obtenir le nombre de cases vides
    if ScoreRouge != 0 and ScoreBleu != 0 and NbCasesVides != 0 :
        ScoreBleuAffiché.config(text=f"Score {Joueur2} : {ScoreRouge}") # Affiche les scores
        ScoreRougeAffiché.config(text=f"Score {Joueur1} : {ScoreBleu}") # Affiche les scores

def Coup_Autorisé(x1, y1, x2, y2) :
    '''
    Verifie si un coup est autorisé et si il faut supprier le pion du premier clic ou non
    I : Coordonnées du pion de départ et celui du pion d'arrivée
    O : (Booléen indiquant si le coup est autorisé, Booléen indiquant si l'ancien pion doit être supprimé)
    '''
    if abs(x1-x2)<=2 and abs(y1-y2)<=2 : # Regarde si la distance entre les pions est 2 ou moins
        if abs(x1-x2)==2 or abs(y1-y2)==2 : # Regarde si la distance entre les pions est 2
            return (True, True) # Le deuxième True indique qu'il faut supprimer l'ancien pion
        else : return (True, False) # Coup légal sans suppression

def aUnCoupLegal(board, couleur):
    '''
    Compte le nombre de coups légaux du joueur
    I : Plateau simulé ou non, couleur du joueur
    O : Nombre de coups legaux
    '''
    global PionsAdverses
    PionsAdverses = []
    NbCoupLegaux=0 # Initialise le nombre de coups légaux 
    for i in board : # Parcourt toutes les cases
        CasesVerifiées=[] # Remet les cases vérifiées à 0 car on cherche les coups légaux à partir d'une autre case
        if couleur == 'bleu' :
                if board[i][1] == 'bleu' :
                    PionsAdverses.append(i)
        if couleur == 'rouge' :
            if board[i][1] == 'rouge' :
                PionsAdverses.append(i)
        if board[i][1]==couleur :  # Regarde si la case est occupée par un pion bleu
            for x in range(-2,3) : # Parcourt toutes les ordonnées
                for y in range(-2,3) : # Parcourt toutes les abscisses pour chaque ordonnée
                    X=i[0]+x
                    Y=i[1]+y
                    X = max(1, min(7, X))
                    Y = max(1, min(7, Y)) # Empêche les valeurs négatives ou supérieures à 7
                    if (X,Y) in CasesVerifiées : continue # Saute la case si elle a déja été vérifiée
                    if board[X,Y][0]==False :
                        NbCoupLegaux+=1
                        CasesVerifiées.append((X,Y)) #Ajoute la case aux cases vérifiées pour qu'elle ne soit pas comptée plusieurs fois (lorsque a ou b est négatif et est ramené à 1)
    return NbCoupLegaux

def CreerPion(event) :
    '''
    Crée un pion à partir d'un autre
    I : Coordonnées du clic
    O : None, affiche le nouveau pion sur le plateau, supprime éventuellement l'ancien et/ou éclaire le pion sélectionné pour montrer qu'il est sélectionné
    '''
    global clic, tour, ChoisirIA, X2, Y2, FonctionBloquée

    if FonctionBloquée and not(isinstance(event, str)) :  # Empêche la fenêtre de se bloquer ou de créer un pion quand l'IA réfléchit)
        return

    # ----------------------------------------------
    # = Enregistre les coordonnées du premier clic =
    # ----------------------------------------------

    if clic[0] == 1 : # Regarde si l'utilisateur en est à son premier clic
        global X
        global Y
        X,Y = min(int(event.x/70+1), 7), min(int(event.y/70+1), 7) # Attribue les coordonnées de la case
        if Case_Occupée(X,Y) : # Regarde si la case est occupée
            if (cases[X,Y][1] == 'bleu' and tour%2==0) or (cases[X,Y][1] == 'rouge' and tour%2!=0) : # Vérifie que le joueur a cliqué sur un pion de la bonne couleur
                clic[0] += 1 # Change la valeur de clic
                clic[1] = (X,Y) # Enregistre les coordonnées du premier clic
                if tour%2 == 0 :
                    plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill= eclaircir_couleur(couleur_1, 1.5)) # Eclaircit la case bleue pour montrer qu'elle est sélectionnée
                else : 
                    plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill= eclaircir_couleur(couleur_2, 1.5)) # Eclaircit la case rouge pour montrer qu'elle est sélectionnée

    else :
        if type(event) is not str :
            X2 = min(int(event.x/70+1), 7)
            Y2 = min(int(event.y/70+1), 7)

        # -------------------------------------------------------------------------------------------
        # = Change les coordonnées du premier clic si le joueur reclique sur une case de sa couleur =
        # -------------------------------------------------------------------------------------------

        if Case_Occupée(X2,Y2) and cases[X2,Y2][1]=='bleu' and tour%2 == 0 :
            plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill=couleur_1)
            clic[1] = (X2,Y2)
            plateau.create_oval((X2-1)*70+6, (Y2-1)*70+6, (X2-1)*70+68, (Y2-1)*70+68, fill=eclaircir_couleur(couleur_1, 1.5)) # Eclaircit la case bleue pour montrer qu'elle est sélectionnée
        elif Case_Occupée(X2,Y2) and cases[X2,Y2][1]=='rouge' and tour%2 != 0 :
            plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill=couleur_2)
            clic[1] = (X2,Y2)
            plateau.create_oval((X2-1)*70+6, (Y2-1)*70+6, (X2-1)*70+68, (Y2-1)*70+68, fill=eclaircir_couleur(couleur_2, 1.5)) # Eclaircit la case rouge pour montrer qu'elle est sélectionnée

        # -------------------------------------------------------------------------------
        # = Permet ou non à l'utilisateur de jouer à l'emplacement de son deuxième clic =
        # -------------------------------------------------------------------------------

        else :
            ChoisirIA.configure(state="disabled") # Empêche l'utilisateur de changer son choix avant la fin de la partie
            if not(Case_Occupée(X2,Y2)) and Coup_Autorisé(clic[1][0], clic[1][1], X2, Y2): # Regarde si la case est occupée et si le coup est autorisé
                if tour == Joueur : # Tour bleu
                    cases[X2,Y2]=(True, 'bleu') # Actualise le dictionnaire cases (occupé, couleur)
                    plateau.create_oval((X2-1)*70+6, (Y2-1)*70+6, (X2-1)*70+68, (Y2-1)*70+68, fill=couleur_1) # Crée un pion bleu
                    plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill=couleur_1) #Remet le pion bleu à sa couleur par défaut
                else : # Tour rouge
                    cases[X2,Y2]=(True, 'rouge') # Actualise le dictionnaire cases (occupé, couleur)
                    plateau.create_oval((X2-1)*70+6, (Y2-1)*70+6, (X2-1)*70+68, (Y2-1)*70+68, fill=couleur_2) # Crée un pion rouge
                    plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill=couleur_2) # Remet le pion rouge à sa couleur par défaut
                if Coup_Autorisé(clic[1][0], clic[1][1], X2, Y2)[1]== True : # CF Fonction : Coup_Autorisé(clic[1][0], clic[1][1], X2, Y2)[1] renvoie True s'il faut supprimer le pion du premier clic (lors d'un déplacement de 2 cases)
                    plateau.create_oval((clic[1][0]-1)*70+6, (clic[1][1]-1)*70+6, (clic[1][0]-1)*70+68, (clic[1][1]-1)*70+68, fill='#E3E3E3', outline='#E3E3E3') #Efface le pion graphiquement
                    cases[clic[1][0], clic[1][1]]=(False,None) # Efface le pion dans le dictionnaire
                
                if tour == Joueur : ChangerCouleurPions(cases, X2, Y2, 'bleu')
                elif tour == Adversaire : ChangerCouleurPions(cases, X2, Y2, 'rouge') #Change la couleur des pions alentour

                # --------------------------------------------------------------
                # = Regarde si la partie est finie par abscence de coup légaux =
                # --------------------------------------------------------------

                ActualiserScore(cases) # Actualise le score
                if ScoreBleu>0 and tour == Adversaire and NbCasesVides>0:
                    tour1.config(text = "La partie est finie.", fg = "black")
                    if not(aUnCoupLegal(cases, 'bleu')) :
                        for i in cases :
                            if cases[i][0] == False :
                                plateau.create_oval((i[0]-1)*70+6, (i[1]-1)*70+6, (i[0]-1)*70+68, (i[1]-1)*70+68, fill=couleur_2) # Remplit toutes les cases vides par des cases rouges
                                fenetre.update()
                                time.sleep(0.04)
                                cases[i] = True,'rouge'
                                ActualiserScore(cases)
                elif ScoreRouge>0 and tour == Joueur and NbCasesVides>0:
                    tour1.config(text = "La partie est finie.", fg = "black")
                    if not(aUnCoupLegal(cases, 'rouge')) :
                        for i in cases :
                            if cases[i][0] == False :
                                plateau.create_oval((i[0]-1)*70+6, (i[1]-1)*70+6, (i[0]-1)*70+68, (i[1]-1)*70+68, fill=couleur_1) # Remplit toutes les cases vides par des cases rouges
                                fenetre.update()
                                time.sleep(0.04)
                                cases[i] = True,'bleu'
                                ActualiserScore(cases)

                # --------------------------------------------
                # = Vérifie que la partie n'est pas terminée =
                # --------------------------------------------

                ActualiserScore(cases)
                if (ScoreRouge == 0 or ScoreBleu == 0 or NbCasesVides==0) :
                    if ScoreRouge>ScoreBleu :
                        ScoreRougeAffiché.config(text=f"Défaite {article_j1} {Joueur1} : {ScoreBleu} - {ScoreRouge}")
                        if not ContreIA : 
                            ScoreBleuAffiché.config(text=f"Victoire {article_j2} {Joueur2} : {ScoreRouge} - {ScoreBleu}")
                            jouermariovictoire()
                        else : 
                            ScoreBleuAffiché.config(text=f"Victoire de l'IA : {ScoreRouge} - {ScoreBleu}")
                            jouermariodefaite()
                        tour1.config(text = "La partie est finie.", fg = "black")
                    else :
                        if not ContreIA :
                            ScoreBleuAffiché.config(text=f"Défaite {article_j2} {Joueur2} : {ScoreRouge} - {ScoreBleu}")
                            jouermariovictoire()
                        else : 
                            ScoreBleuAffiché.config(text=f"Défaite de l'IA : {ScoreRouge} - {ScoreBleu}")
                            jouergta()
                        ScoreRougeAffiché.config(text=f"Victoire {article_j1} {Joueur1} : {ScoreBleu} - {ScoreRouge}")
                        tour1.config(text = "La partie est finie.", fg = "black")
                    fenetre.update()

                tour += 1 # Change le tour
                tour = tour % 2

                if not check_partie_finie(cases) : mise_a_jour() # Mets le texte à jour si la partie n'est pas terminée
                    
                # -----------------------------------------------
                # = Regarde si l'utilisateur joue contre une IA =
                # -----------------------------------------------
                
                if tour == Adversaire and ContreIA  == True and (not check_partie_finie(cases) or CasesVides !=0) :
                    FonctionBloquée = True
                    AdversaireIA.Jouer()
                    mise_a_jour()

                FonctionBloquée = False # Permet de bloquer l'exécution de la fonction si l'IA réfléchit, pour empêcher que la fenetre freeze
                clic[0]=1 # Remet le joueur suivant à son premier clic

def Case_Occupée(x,y):
    '''
    Regarde si la case est occupée
    I : Coordonnées de la case
    O : Booléen indiquant si la case est occupée
    '''
    return cases[x,y][0] # cases[x,y][0] contient l'occupation de la case

def ReinitialiserJeu() :
    ''''
    Réinitialise le jeu
    I : None
    O : None
    '''
    global tour, tourIA, FonctionBloquée, clic
    FonctionBloquée = False
    tour = 0 # Remet le nombre de tours passés à 0
    tourIA = 1
    clic = [1, None]
    ChoisirIA.configure(state="readonly") # Empêche l'utilisateur de changer l'IA en cours de partie
    CréerCases() # Efface le plateau
    CréerPionDebut() # Crée les pions du début
    ActualiserScore(cases) # Enlève le score de la partie d'avant
    mise_a_jour() # Actualise le texte de tour

def ChoisirDifficulté(event) :
    '''
    Choisit la difficulté de l'IA
    I : None (event est obligatoire mais ne sert ici à rien)
    O : None
    '''
    global ContreIA, AdversaireIA, Adversaire, Joueur, ancien_son

    if ChoisirIA.get() != "Pas d'IA" : 
        ContreIA = True
        if ChoisirIA.get() == 'Très facile' :
            AdversaireIA = IA('TrèsFacile')
            if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond() # On joue la nouvelle musique uniquement si elle n'est pas déjà en cours
        elif ChoisirIA.get() == 'Facile' :
            AdversaireIA = IA('Facile')
            if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond()
        elif ChoisirIA.get() == 'Moyen' :
            AdversaireIA = IA('Moyen')
            if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond()
        elif ChoisirIA.get() == 'Difficile' :
            AdversaireIA = IA('Difficile')
            if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond()
        elif ChoisirIA.get() == 'Très difficile' :
            AdversaireIA = IA('Très difficile')
            if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond()
    if ChoisirIA.get() == "Pas d'IA" :
        ContreIA = False
        if jouer_son and ChoisirIA.get() != ancien_son : jouer_fond()
    ancien_son = ChoisirIA.get() # On sauvegarde le nom de la musique (précédemment jouée)

def redblue(tour):
    """
    Renvoie le nom du joueur correspondant au tour
    I : Tour
    O : Nom de la couleur
    """
    if tour == Joueur :
        return Joueur1
    else:
        return Joueur2
    
def mise_a_jour():
    """
    Met le texte de tour à jour
    I : None
    O : None
    """
    global article_j1, article_j2, CoupsCalculés

    if check_partie_finie(cases) : 
        tour1.config(text = "La partie est finie.")
        return
    couleur1 = redblue(tour)
    article_j1 = "du" if Joueur1 == "Joueur 1" else "de" # Modifie l'article en fonction du nom des joueurs
    article_j2 = "du" if Joueur2 == "Joueur 2" else "de"
    if tour == Joueur :
        tour1.config(text=f"Au tour {article_j1} : {couleur1}", foreground = couleur_1)
        fenetre.update()
    if ContreIA == False and tour == Adversaire : 
        tour1.config(text=f"Au tour {article_j2} : {couleur1}", foreground = couleur_2)
        fenetre.update()
    elif ContreIA == True and tour == Adversaire :
        tour1.config(text="Calcul du meilleur coup...", foreground = couleur_2)
        fenetre.update()



def jouer_fond():
    """
    Permet à l'utilisateur de pouvoir jouer le son de fond
    I : None
    O : None
    """
    global jouer_son
    jouer_son = True # Permet de mettre à jour le son
    pygame.mixer.stop()
    pygame.mixer.init()
    if ChoisirIA.get() != "Pas d'IA" : 
        if ChoisirIA.get() == 'Très facile' :
            musicbot1()
        elif ChoisirIA.get() == 'Facile' :
            musicbot2()
        elif ChoisirIA.get() == 'Moyen' :
            musicbot3()
        elif ChoisirIA.get() == 'Difficile' :
            musicbot4()
        elif ChoisirIA.get() == 'Très difficile' :
            musicbot5()
    else : 
        son_fond = pygame.mixer.Sound(os.path.join(chemin_fichier, "musiquejazz.mp3"))
        channel = son_fond.play()
        channel.set_volume(0.25)  # Réglage du volume du son de fond à 25%
        bouton_jouer.pack_forget()  # Masquer le bouton "Jouer"
        bouton_arreter.pack()  # Afficher le bouton "Arrêter"
        changer_volume(scale_volume.get())

def arreter_fond():
    """
    Permet à l'utilisateur de pouvoir arreter le son de fond
    I : None
    O : None
    """
    global jouer_son
    jouer_son = False # Permet d'empêcher la mise à jour du son
    pygame.mixer.stop()
    bouton_arreter.pack_forget()  # Masquer le bouton "Arrêter"
    bouton_jouer.pack(side = tkinter.RIGHT)  # Afficher le bouton "Jouer"

loading = False

def fermer_attente():
    global loading
    loading = True
    attente.destroy()

def animer_gif(frame_number=0):
    if loading or frame_number >= num_frames :
        return
    label.configure(image=frames[frame_number])
    attente.after(30, animer_gif, (frame_number + 1))

jouer_lancement()
gifloading = os.path.join(chemin_fichier, "Attaxx2.gif")  # Remplace avec le chemin de ton fichier GIF
gif1 = Image.open(gifloading)
attente = tkinter.Tk()
attente.title("Attente...")
attente.geometry(f"{606}x190+{(attente.winfo_screenwidth()-600)//2}+{(attente.winfo_screenheight()-190)//2}")
attente.resizable(0, 0)
attente.iconbitmap(os.path.join(chemin_fichier, "waiting.ico"))

frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif1)]
num_frames = len(frames)

label = tkinter.Label(attente)
label.pack()

attente.after(2000, fermer_attente)
attente.after(0, animer_gif)

if lancer_jeu == True: 
    attente.mainloop()

if bon_mdp == True and lancer_jeu == True :
    fenetre = tkinter.Tk() # Crée la fenêtre
    fenetre.title("Projet ATTAXX") # Nomme la fenêtre
    fenetre.iconbitmap(os.path.join(chemin_fichier, "A.ico"))
    fenetre.geometry(f"{600}x{662}+{(fenetre.winfo_screenwidth()-600)//2}+{(fenetre.winfo_screenheight()-662)//2}") #Place la fenêtre au milieu de l'écran
    fenetre.resizable(0,0) # Empêche l'utilisateur de changer la taille de la fenêtre

    framescore=tkinter.Frame(fenetre) # crée une frame pour afficher le score, contient à la fois le score du J1 et du J2
    framescore.pack(pady = (7, 0))
    ScoreRougeAffiché = tkinter.Label(framescore, font="Open 13 bold", text=f"Score {Joueur1} : ", foreground=couleur_1)
    ScoreRougeAffiché.pack(side=tkinter.LEFT, padx = (50, 20))
    ScoreBleuAffiché = tkinter.Label(framescore, font="Open 13 bold",text=f"Score {Joueur2} : ", foreground=couleur_2)
    ScoreBleuAffiché.pack(side=tkinter.RIGHT, padx = (20, 50))

    tour1 = tkinter.Label(fenetre, font="Open 13 bold" )
    tour1.pack(pady=(0,8))

    plateau = tkinter.Canvas(fenetre, width = 491, height = 491, bg = '#FFDDC9') # Crée un fond de 491*491px et lui donne une couleur
    plateau.pack(padx = 20)
    plateau.bind('<Button-1>', CreerPion) # Attribue l'exécution de la fonction CreerPion au clic gauche
    frame2=tkinter.Frame(fenetre)
    frame2.pack(pady = (11, 0))
    ttk.Button(frame2, text = 'Rejouer', command = ReinitialiserJeu, cursor = "hand2").pack(side = tkinter.LEFT, padx = (130, 40)) # Crée le bouton Effacer
    ttk.Button(frame2, text = 'Quitter', command = fenetre.destroy, cursor = "hand2").pack(side = tkinter.RIGHT, padx = (40, 130)) # Crée le bouton Quitter
    ChoisirIA = ttk.Combobox(frame2, state='readonly', values=["Pas d'IA", 'Très facile', 'Facile', 'Moyen', 'Difficile', 'Très difficile'], justify="center") # Crée un menu déroulant et définit des valeurs
    ChoisirIA.pack(pady= (2,0)) # Le positionne à la même hauteur que les deux autres
    ChoisirIA.bind("<<ComboboxSelected>>", ChoisirDifficulté) # Exécute ChoisirDifficulté lorsqu'une des options est cliqué
    ChoisirIA.set("Pas d'IA") #Pas d'IA est la valeur par défaut
    CréerCases() # Crée les cases
    CréerPionDebut() # Crée les pions de départ
    ActualiserScore(cases) # Affiche le score de départ

    # Charger l'image
    imageplay = Image.open(os.path.join(chemin_fichier, "mute.png"))
    image = imageplay.resize((30, 30))  # Redimensionner l'image à la taille souhaitée

    # Convertir l'image pour tkinter
    photo = ImageTk.PhotoImage(image)

    # Charger l'image
    ipause = Image.open(os.path.join(chemin_fichier, "audio.png"))
    image = ipause.resize((30, 30))  # Redimensionner l'image à la taille souhaitée

    # Convertir l'image pour tkinter
    photop = ImageTk.PhotoImage(image)

    framesons=tkinter.Frame(fenetre)
    framesons.pack(pady = (5))
    scale_volume = tkinter.Scale(framesons, from_ = 0, to = 100, orient="horizontal", command=changer_volume)
    scale_volume.pack(side=tkinter.LEFT, padx = (0, 8))
    scale_volume.set(100)  # Réglage initial du volume à 100 (maximum)

    bouton_jouer = tkinter.Button(framesons, cursor="hand2", image=photo, text="Jouer", command=jouer_fond, bd=0, highlightthickness=0)
    bouton_jouer.pack(side = tkinter.RIGHT)

    bouton_arreter = tkinter.Button(framesons, cursor="hand2", image=photop, text="Arrêter", command=arreter_fond, bd=0, highlightthickness=0)
    bouton_arreter.pack_forget()  # Au départ, le bouton "Arrêter" est masqué

    mise_a_jour()
    fenetre.mainloop() #Lance l'affichage