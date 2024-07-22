class Cat:

    def Eat(self):
        print("Cat Eating")

class kitty(Cat):

    def Eat(self):
        print("kitty Eating")

C = Cat()
K = kitty()

C.Eat()
K.Eat()