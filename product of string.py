def multiply_strings(s1, s2):
    try:
        
        num1 = int(s1)
        num2 = int(s2)
        
        product = num1 * num2
        return product
    except ValueError:
        return "Invalid input. Please provide valid numeric strings."


s1 = str(input("Enter first number:"))

s2 = str(input("Enter second number:"))
print("Product:", multiply_strings(s1, s2))

