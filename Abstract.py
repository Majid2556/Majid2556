from abc import ABC,abstractmethod

class Car(ABC):


    @abstractmethod
    def horn(self):
        return "Horning"

class pride(Car):
    
    def horn(self):

        return "pride is horning"

pride141 = pride()
print(pride141.horn())