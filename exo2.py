
from exo import Robot

#* Réutiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
#* Un humain doit posséder un sexe attribuable à sa création
#* Un humain doit pouvoir manger un ou plusieurs aliments
#* Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps*
#* Un Cyborg doit être une combinaison d'un humain et d'un robot
#* Bonus : ajouter une méthode fun au Cyborg

from time import sleep

class Humain():
    def __init__(self, sex = "M", name = "Heracles"):

        self.__sex = sex # Man is 0 | Women is 1
        self.__name = name
        self.__imc = 20
        self.__need_digestion = False
    
    @property
    def sex(self):
        print("Sex :",self.__sex)
        return self.__sex
    @sex.setter
    def sex(self, sex):
        self.__sex = sex
    
    @property
    def name(self):
        print("Name :",self.__name)
        return self.__name
    @name.setter
    def name(self, string):
        self.__name = string
    
    @property
    def imc(self):
        print("IMC :",self.__imc)
        return self.__imc
    @imc.setter
    def imc(self, val):
        self.__imc = val
    
    @property
    def need_digestion(self):
        print("Need digestion ? :",self.__need_digestion)
    
    def eat(self, foods):
        
        if self.__need_digestion == False:

            if type(foods) == list:
                for food in foods:
                    print(food + " has been eaten")
                self.__need_digestion = True

            elif foods.isalpha():
                print(foods + " has been eaten")
                self.__need_digestion = True

            else:
                print("Enter a string value or a valid aliment")

        else:
            print("You have already eat. PLS digest before another eat")
        
    def digest(self):
        if self.__need_digestion == True:
            print("Food digest")
            self.__imc = self.__imc + 2
            self.__need_digestion = False
        else:
            print("Eat before digest")

class Cyborg(Humain, Robot):

    def __init__(self, nom):
        Humain.__init__(self,name = nom)
        Robot.__init__(self, name = nom)
    
    def mind_hacking(self):
        print()
        print("\nI read in your minds and ...")
        sleep(2)
        print("\n         YOU ARE GAY\n")

if __name__ =="__main__":
    Robocop = Cyborg(nom = "Robocop")
    Robocop.globalState()

    Robocop.eat(["Pomme", "Banane"])
    Robocop.eat("Banane")

    Robocop.digest()
    Robocop.charge()

    Robocop.mind_hacking()
