def get_card_number():
    while True:
        try:
            card_number = int(input("Enter credit card number: "))
            if card_number > 0:
                return card_number
        except ValueError:
            continue  # If input is not a valid integer, prompt again

def validate_card(card_number):
    sum = 0
    alternate = False

    # Process each digit from right to left
    while card_number > 0:
        digit = card_number % 10  # Get the last digit
        card_number //= 10  # Remove the last digit

        # If alternate is True, we need to multiply this digit by 2
        if alternate:
            digit *= 2
            # If the result is greater than 9, add the digits of the result
            if digit > 9:
                digit = (digit % 10) + 1  # Add the digits of the product

        sum += digit  # Add the digit (or modified digit) to the sum
        alternate = not alternate  # Toggle alternate

    # Check if the sum is a multiple of 10
    return sum % 10 == 0

def main():
    card_number = get_card_number()
    
    if validate_card(card_number):
        print("Valid card number.")
    else:
        print("Invalid card number.")

if __name__ == "__main__":
    main()