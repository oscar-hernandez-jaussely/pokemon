
from poktypes.feu import Feu

from poktypes.eau import Eau

from poktypes.normal import Normal

from poktypes.terre import Terre



Arcanin = Feu("Arcanin", 110, défense=80)

Roucool = Normal("Roucool", 45, défense=40)

Carapuce = Eau("Carapuce", 48, défense=65)

Salamèche = Feu("Salamèche", 52, défense=43)

Sablaireau = Terre("Sablaireau", 100, défense=110)

pokemon_list = [Arcanin, Roucool, Carapuce, Salamèche, Sablaireau]

