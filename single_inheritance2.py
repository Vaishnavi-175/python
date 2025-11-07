class Parent:
    def display_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def display_child(self):
        print("This is the Child class.")

# Create object of Child class
obj = Child()

# Access methods from both Parent and Child
obj.display_parent()
obj.display_child()
