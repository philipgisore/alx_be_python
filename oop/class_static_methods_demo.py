class Calculator:
    #Class attribute 
    calculation_type = "Arithmetic Opertaions"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculatin_type}")
        return a * b
    
