# Dhruv Patel
# 11/14/2022
# CAC190
# Problem 15
# ArithmeticOperation

# Class holding each function
class Arithmetic:

    # Method to call num1 and num2
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    # Functions to display each operation function.
    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1*self.num2
    
    def divide(self):
        return self.num1/self.num2
    
    def pow(self):
        return self.num1**self.num2

# main class to ask the user to enter two integers
def main():
    value1 = int(input('Please enter a number: '))
    value2 = int(input('Please enter a number: '))
    math = Arithmetic(value1, value2)

    # Prints each operation to the screen
    print('Sum:',math.add())
    print('Difference:', math.subtract())
    print('Product:', math.multiply())
    print('Quotient:',math.divide())
    print('Power:',math.pow())
main()