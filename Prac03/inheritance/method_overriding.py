#1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):   # <- overriding
        print("Bark")


#2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()   
        print("Bark")

