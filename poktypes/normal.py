
from pokemon import *

class Normal(Pokemon):
    def __init__(self, nom, attaque, type="Normal", défense=0, lvl=0, pv=100):
        super().__init__(nom, type, attaque, défense, lvl, pv)

