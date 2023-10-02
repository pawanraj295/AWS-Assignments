class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Output: "Buddy says Woof!"

class Parent1:
    def speak(self):
        return "Hello from Parent1"

class Parent2:
    def speak(self):
        return "Hi from Parent2"

class Child(Parent1, Parent2):
    pass

child_instance = Child()
print(child_instance.speak())  # Output: "Hello from Parent1"

class Grandparent:
    def greet(self):
        return "Hello from Grandparent"

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child_instance = Child()
print(child_instance.greet())  # Output: "Hello from Grandparent"
