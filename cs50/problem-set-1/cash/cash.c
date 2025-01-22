#include <stdio.h>

int main(void) {
    int change;

    // Prompt user for change owed until a valid input is received
    do {
        printf("Change owed: ");
        // Check if the input is an integer and greater than 0
        if (scanf("%d", &change) != 1 || change < 1) {
            // Clear the input buffer
            while (getchar() != '\n');
            change = 0; // Reset change to 0 to continue the loop
        }
    } while (change < 1);

    // Calculate the minimum number of coins
    int coins = 0;

    // Calculate the number of quarters (25 cents)
    coins += change / 25;
    change %= 25;

    // Calculate the number of dimes (10 cents)
    coins += change / 10;
    change %= 10;

    // Calculate the number of nickels (5 cents)
    coins += change / 5;
    change %= 5;

    // Calculate the number of pennies (1 cent)
    coins += change;

    // Print the total number of coins
    printf("%d\n", coins);

    return 0;
}