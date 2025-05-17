def multiply_strings(s1, s2):
    try:
        # Convert strings to integers
        num1 = int(s1)
        num2 = int(s2)
        # Calculate the product
        product = num1 * num2
        return product
    except ValueError:
        return "Invalid input. Please provide valid numeric strings."

# Example usage
s1 = str(input("Enter first number:"))

s2 = str(input("Enter second number:"))
print("Product:", multiply_strings(s1, s2))