#include <stdio.h>

long long get_card_number(void);
int validate_card(long long card_number);

int main(void) {
    long long card_number = get_card_number();
    
    if (validate_card(card_number)) {
        printf("Valid card number.\n");
    } else {
        printf("Invalid card number.\n");
    }

    return 0;
}

// Function to get a valid credit card number from the user
long long get_card_number(void) {
    long long card_number;
    do {
        printf("Enter credit card number: ");
        scanf("%lld", &card_number);
    } while (card_number <= 0);
    return card_number;
}

// Function to validate the credit card number using Luhn's algorithm
int validate_card(long long card_number) {
    int sum = 0;
    int alternate = 0;

    // Process each digit from right to left
    while (card_number > 0) {
        int digit = card_number % 10; // Get the last digit
        card_number /= 10; // Remove the last digit

        // If alternate is 1, we need to multiply this digit by 2
        if (alternate) {
            digit *= 2;
            // If the result is greater than 9, add the digits of the result
            if (digit > 9) {
                digit = (digit % 10) + 1; // Add the digits of the product
            }
        }

        sum += digit; // Add the digit (or modified digit) to the sum
        alternate = !alternate; // Toggle alternate
    }

    // Check if the sum is a multiple of 10
    return (sum % 10 == 0);
}