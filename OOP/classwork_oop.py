# create a class name calculator, which takes num1 and num2 as args
# define 4 mothods, add, subtract, multiply, and divide
# all methods should be called by object and print the results

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.num3 = 5

    def add(self):
        print(f"the sum of the two numbers is: {self.num1 + self.num2}")

    def subtract(self):
        print(f"the sum of the two numbers is: {self.num1 - self.num2}")

    def multiply(self):
        print(f"the sum of the two numbers is: {self.num1 * self.num2}")

    def divide(self):
        print(f"the sum of the two numbers is: {self.num1 / self.num2}")



calculation_a = Calculator(1, 4)
calculation_b = Calculator(4, 7)
calculation_c = Calculator(44, 77)

calculation_a.add()
calculation_b.multiply()
calculation_c.divide()


          