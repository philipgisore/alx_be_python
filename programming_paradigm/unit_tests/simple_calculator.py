class SimpleCalculator:
    """A simple calculator that supports basic arithmetic operations."""
    
    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b
    
    def divide(self, a, b): 
        """Retun the division of a by b. returns None if b is zero."""
        if b == 0:
            return None
        return a / b