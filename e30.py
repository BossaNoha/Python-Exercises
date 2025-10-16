class Calculator:
    def add(self, numA, numB):
        result = numA + numB
        return result
    
    def subtract(self, numA, numB):
        result = numA - numB
        return result
    
    def multiply(self, numA, numB):
        result = numA * numB
        return result
    
    def divide(self, numA, numB):
        if numB != 0: result = numA/numB
        else: result = "Unable"
        return result
    
    

calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.subtract(10, 4)) # 6
print(calc.multiply(3, 7))  # 21
print(calc.divide(8, 2))    # 4.0
print(calc.divide(5, 0))    # Cannot divide by zero
