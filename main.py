
import time

from combat import *
from p_list import *

def Launch_game():
    print("\n ------- Pokemon - Special Python Edition ------- \n")
    time.sleep(1)
    LaunchGame = input("Voulez vous lancer une partie ? 'oui' non' ")
    if LaunchGame == "oui":
        C.pokemon_choice()
    elif LaunchGame == "non":
        return   


Launch_game()

