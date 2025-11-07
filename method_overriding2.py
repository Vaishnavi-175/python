class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

# Create objects
a = Animal()
d = Dog()

# Call the sound method
a.sound()  # Calls parent class method
d.sound()  # Calls child class overridden method
