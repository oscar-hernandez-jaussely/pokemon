
from pokemon import Pokemon

class Feu(Pokemon):
    def __init__(self, nom, attaque, type="Feu", défense=0, lvl=0, pv=100):
        super().__init__(nom, type, attaque, défense, lvl, pv)

