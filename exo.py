# Exo 1 : Prémice 

from time import sleep

class Robot():

    def __init__(self, name = "Polux"):

        self.__name = name
        self.__state = "On"
        self.__battery = 20
        self.__mvt_state = False
        self.__vitess = 10

    @property
    def name(self):
        print("Name :", self.__name)
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def vitess(self):
        return(self.__vitess)
    @vitess.setter
    def vitess(self, vite):
        self.__vitess= vite

    @property
    def state(self):
        return self.__state
    
    @property
    def tauxcharge(self):
        return(self.__battery)
    
    @property
    def mvt_state(self):
        return(self.__mvt_state)
    
    def allumer(self):
        self.__state = "On"
        print("I'm ON")
    
    def eteindre(self):
        self.__state = "Off"
        print("I'm OFF")
    
    def charge(self):
        while self.__battery <  100:
            self.__battery = self.__battery + 10
            if self.__battery >  100:
                self.__battery = 100
            print("Battery : ",self.__battery,"%" )
            sleep(1)
    
    def move(self, vitess):

        if vitess < 5:
            vitess = 5

        coef =  vitess * 0.5

        if coef > 60 :
            coef = 60

        if self.__battery - coef >0:

            self.__vitess = vitess
            self.__mvt_state = True
            self.__battery = self.__battery - coef

        else:

            self.__vitess = 0
            self.__mvt_state = False
            print("Not enough energy. Pls charge more or slow down")

    def stopmove(self):

        self.__vitess = 0
        self.__mvt_state = False

    def globalState(self):

        print("Name :", self.__name)
        print("State :", self.__state)
        print("Battery :",self.__battery)
        print("Speed :",self.__vitess)
        print("Moving ? :",self.__mvt_state)

if __name__ =="__main__":

    walle = Robot()
    walle.move(50)

    walle.charge()
    walle.move(56)

    walle.stopmove()

    walle.eteindre()
    walle.globalState()

