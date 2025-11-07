class Grandparent:
    def show_grandparent(self):
        print("This is the Grandparent class.")

class Parent(Grandparent):
    def show_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is the Child class.")

# Create object of Child class
obj = Child()

# Access methods from all classes
obj.show_grandparent()
obj.show_parent()
obj.show_child()
