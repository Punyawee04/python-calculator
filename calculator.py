class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        b=abs(b)
        for i in range((b+1)-1):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        aabs,babs=abs(a),abs(b)
        while aabs >= babs:
            aabs = self.subtract(babs, aabs)
            result += 1
        if (a<0) != (b<0) :
            result=-result
        return result
    
    def modulo(self, a, b):
        a_negative = a < 0 
        b = abs(b)
        a = abs(a)
        while a >= b:
            a = a-b
        if a_negative:
            a = -a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))