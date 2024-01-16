# Exo 1 : Prémice 

from time import sleep

class Robot():

    def __init__(self, name = "Polux"):

        self.__name = name
        self.__state = "On"
        self.__tauxcharge = 20
        self.__vitess = 10
        self.depl = False

    @property
    def name(self):
        print("Name :", self.__name)
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def state(self):
        return self.__state
    
    @property
    def tauxcharge(self):
        return(self.__tauxcharge)
    
    @property
    def vitess(self):
        return(self.__vitess)
    
    def allumer(self):
        self.__state = "On"
        print("Je me suis allumé :)")
    
    def eteindre(self):
        self.__state = "Off"
        print("Je m'éteins :-( ")
    
    def charge(self):
        while self.__tauxcharge <  100:
            self.__tauxcharge = self.__tauxcharge + 10
            if self.__tauxcharge >  100:
                self.__tauxcharge = 100
            print("Le taux de charge est a ",self.__tauxcharge,"%" )
            sleep(1)
    
    def move(self, vitess):

        if vitess < 5:
            vitess = 5

        coef =  vitess * 0.5

        if coef > 60 :
            coef = 60
            
        if self.__tauxcharge - coef >0:

            self.__vitess = vitess
            self.depl = True
            self.__tauxcharge = self.__tauxcharge - coef

        else:

            self.__vitess = 0
            self.depl = False
            print("Pour cause de charge épuisé, je ne peux me déplacer :()")

    def stopmove(self):

        self.__vitess = 0
        self.depl = False

    def globalState(self):

        print("Nom :", self.__name)
        print("Etat :", self.__state)
        print("Taux de charge :",self.__tauxcharge)
        print("Vitesse :",self.__vitess)
        print("En deplacement :",self.depl)

a = Robot()
a.move(50)

a.charge()
a.move(56)

val = a.vitess
print(val)
a.stopmove()

a.eteindre()
a.globalState()

