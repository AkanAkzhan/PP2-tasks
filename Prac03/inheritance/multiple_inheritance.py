#1
class Father:
    def skill1(self):
        print("Father: Driving")

class Mother:
    def skill2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

#2
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    pass

#3
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    def show(self):
        super().show()
        print("C")
