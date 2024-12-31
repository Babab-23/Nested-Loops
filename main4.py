def decimal_to_binary(decimal_number):
    # Check if the number is 0
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    is_negative = False

    # Handle negative numbers
    if decimal_number < 0:
        is_negative = True
        decimal_number = abs(decimal_number)

    # Convert to binary
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2

    # Add a negative sign if the original number was negative
    if is_negative:
        binary_number = "-" + binary_number

    return binary_number

# Get user input
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"Binary representation: {binary_number}")
