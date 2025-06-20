def safe_divide(numerator, denominator):
    try:
        numerator_float = float(numerator)
        denominator_float = float(denominator)
        
        if denominator_float == 0:
            return "Error: Cannot divide by zero."
            
        return f"The result of the division is {numerator_float / denominator_float}"
        
    except ValueError:
        return "Error: Both numerator and denominator must be numbers."