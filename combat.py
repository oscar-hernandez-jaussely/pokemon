
from itertools import cycle
import p_list
from p_list import *
import time
import random

class Combat():

    global players

    def __init__(self):
        self.winner = ""
        self.looser = ""
        self.attack_value = 1     

    # Permet de choisir un pokémon parmi ceux disponibles
    def pokemon_choice(self): 
        print("\n Sélectionnez un pokémon : \n ")
        for ele in pokemon_list:
            pok = ele
            print(pok.get_nom(), "\n",  "de type ",  pok.type, "\n", "attaque = ", pok.attaque, "\n", "défense = ", pok.défense)
            print("\n")
        time.sleep(1)
        pokemon_select = input("Choisissez un pokémon  :  \n")
        global players
        players = [0, 1]
        global pokemon_selected
        if pokemon_select == "Arcanin" or pokemon_select == "arcanin":
            pokemon_selected = Arcanin
            players.pop(0)
            players.insert(0, Arcanin)
            players.pop(1)
            players.insert(1, random.choice(pokemon_list))
            if players[1] == Arcanin:
                while players[1] == Arcanin:
                    players.pop(1)
                    players.insert(1, random.choice(pokemon_list))
            ennemy_selected = players[1]
        elif pokemon_select == "Carapuce" or pokemon_select == "carapuce":
            pokemon_selected = Carapuce
            players.pop(0)
            players.insert(0, Carapuce)
            players.pop(1)
            players.insert(1, random.choice(pokemon_list))
            if players[1] == Carapuce:
                while players[1] == Carapuce:
                    players.pop(1)
                    players.insert(1, random.choice(pokemon_list))
            ennemy_selected = players[1]
        elif pokemon_select == "Roucool" or pokemon_select == "roucool":
            pokemon_selected = Roucool
            players.pop(0)
            players.insert(0, Roucool)
            players.pop(1)
            players.insert(1, random.choice(pokemon_list))
            if players[1] == Roucool:
                while players[1] == Roucool:
                    players.pop(1)
                    players.insert(1, random.choice(pokemon_list))
            ennemy_selected = players[1]
        elif pokemon_select == "Salamèche" or pokemon_select == "salamèche":
            pokemon_selected = Salamèche
            players.pop(0)
            players.insert(0, Salamèche)
            players.pop(1)
            players.insert(1, random.choice(pokemon_list))
            if players[1] == Salamèche:
                while players[1] == Salamèche:
                    players.pop(1)
                    players.insert(1, random.choice(pokemon_list))
            ennemy_selected = players[1]
        elif pokemon_select == "Sablaireau" or pokemon_select == "sablaireau":
            pokemon_selected = Sablaireau
            players.pop(0)
            players.insert(0, Sablaireau)
            players.pop(1)
            players.insert(1, random.choice(pokemon_list))
            if players[1] == Sablaireau:
                while players[1] == Sablaireau:
                    players.pop(1)
                    players.insert(1, random.choice(pokemon_list))
            ennemy_selected = players[1]
        else:
            return
        print("Vous avez choisi " + pokemon_selected.get_nom() + "\n")
        print("Le pokémon adverse est " + ennemy_selected.get_nom() + "\n")
        C.players_define()

    def players_define(self):
        self.players = cycle(players)
        self.currentplayer = players[0]
        self.ennemy = players[1]
        C.attack_multiplier()

    # Vérifie si l'un des deux pokémon est K.O, et met fin au combat
    def ko_check(self):
        if self.currentplayer.get_pv() <= 0:
           print("Ce pokémon est K.O \n")
           print (self.ennemy.get_nom() , "remporte le combat !\n")
           self.winner = self.ennemy.get_nom()
           self.looser = self.currentplayer.get_nom()
           return
        elif self.ennemy.get_pv() <= 0:
            print("Le pokémon ennemi est K.O \n")
            print(self.currentplayer.get_nom() , "remporte le combat ! \n")
            self.winner = self.currentplayer.get_nom()
            self.looser = self.ennemy.get_nom()
        else:
            C.attack_menu()

    # Renvoie le nom du vainqueur
    def get_winner(self):
        return self.winner
    
    # Renvoie le nom du perdant
    def get_looser(self):
        return self.looser

    # Récupère le type des deux pokémon et multiplie la valeur de l'attaque en fonction
    def attack_multiplier(self):
        if self.currentplayer.type == "Eau" and self.ennemy.type == "Feu" :
            self.attack_value = self.currentplayer.attaque * 2
        elif self.currentplayer.type == "Eau" and self.ennemy.type == "Terre" :
            self.attack_value = self.currentplayer.attaque * 0.5
        elif self.currentplayer.type == "Feu" and self.ennemy.type == "Eau" :
            self.attack_value = self.currentplayer.attaque * 0.5
        elif self.currentplayer.type == "Feu" and self.ennemy.type == "Terre" :
            self.attack_value = self.currentplayer.attaque * 2
        elif self.currentplayer.type == "Terre" and self.ennemy.type == "Eau" :
            self.attack_value = self.currentplayer.attaque * 2
        elif self.currentplayer.type == "Terre" and self.ennemy.type == "Feu" :
            self.attack_value = self.currentplayer.attaque * 0.5
        elif self.currentplayer.type == "Normal" and self.ennemy.type == "Eau" :
            self.attack_value = self.currentplayer.attaque * 0.75
        elif self.currentplayer.type == "Normal" and self.ennemy.type == "Feu" :
            self.attack_value = self.currentplayer.attaque * 0.75
        elif self.currentplayer.type == "Normal" and self.ennemy.type == "Terre" :
            self.attack_value = self.currentplayer.attaque * 0.75
        else:
            self.attack_value = self.currentplayer.attaque
        C.attack_menu()
        
    # Génère le menu d'action
    def attack_menu(self):
        print("Que doit faire {} ? \n".format(self.currentplayer.get_nom()))
        print("Attaquer  -  Fuir \n")
        move_choice = input("'attaquer' 'fuir' \n")
        if move_choice == 'attaquer':
            C.attack()
        elif move_choice == 'fuir':
            print("Vous prenez la fuite \n")
            return
        
    # Génère l'attaque avec les valeurs modifiées
    def attack(self):
        if not self.attack_value == 0:
            Combat.damage(self)
        else:
            print("Cette attaque est inefficace \n")

    # Génère les dégâts de l'attaque
    def damage(self):
        self.ennemy.set_pv(self.ennemy.get_pv() - int(self.attack_value))
        print ("Vous infligez {} points de dégâts à {} \n".format(self.attack_value, self.ennemy.get_nom()))
        C.ko_check()
 
    # Récupère l'ensemble des infos sur le pokémon actuel
    def get_player_infos(self):
        return self.currentplayer.get_all()
    
    # Récupère l'ensemble des infos sur le pokémon ennemi
    def get_ennemy_infos(self):
        return self.ennemy.get_all()


C = Combat()

