
class Pokemon:
    def __init__(self, nom, type, attaque, défense=0, lvl=0, pv=100): 
        self.__nom = nom
        self.type = type
        self.__pv = pv
        self.lvl = lvl
        self.attaque = attaque
        self.défense = défense

    def get_all(self):
        print (
            "Nom : " + self.__nom + "\n" + "Type : " + self.type + "\n" + "PV : " + str(self.__pv) + "\n" + "Niveau : " + str(self.lvl) + "\n" + "Attaque : " + str(self.attaque) + "\n" + "Défense : " + str(self.défense)
        )
    
    def set_pv(self, valeur):
        if type(valeur) == int:
            self.__pv = valeur
        else:
            return
        
    def get_pv(self):
        return self.__pv
    
    def get_nom(self):
        return self.__nom


        
