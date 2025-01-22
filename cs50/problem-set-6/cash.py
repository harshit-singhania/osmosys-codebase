def main():
    change = 0

    # Prompt user for change owed until a valid input is received
    while change < 1:
        try:
            change = int(input("Change owed: "))
            if change < 1:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            change = 0  # Reset change to 0 to continue the loop

    # Calculate the minimum number of coins
    coins = 0

    # Calculate the number of quarters (25 cents)
    coins += change // 25
    change %= 25

    # Calculate the number of dimes (10 cents)
    coins += change // 10
    change %= 10

    # Calculate the number of nickels (5 cents)
    coins += change // 5
    change %= 5

    # Calculate the number of pennies (1 cent)
    coins += change

    # Print the total number of coins
    print(coins)

if __name__ == "__main__":
    main()