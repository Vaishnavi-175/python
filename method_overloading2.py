class MathOperations:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Sum of three numbers:", a + b + c)
        elif a is not None and b is not None:
            print("Sum of two numbers:", a + b)
        elif a is not None:
            print("Single value:", a)
        else:
            print("No arguments provided.")

# Create an object
obj = MathOperations()

# Different calls to the same method
obj.add()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)
