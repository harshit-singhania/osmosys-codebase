#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void encrypt(char *plaintext, int key);

int main(int argc, char *argv[])
{
    // Check for correct number of command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert the key from string to integer
    int key = atoi(argv[1]);

    // Check if the key is a positive integer
    if (key < 0)
    {
        printf("Key must be a non-negative integer.\n");
        return 1;
    }

    // Prompt user for plaintext
    char plaintext[100];
    printf("plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // Encrypt the plaintext
    encrypt(plaintext, key);

    return 0;
}

void encrypt(char *plaintext, int key)
{
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Check if the character is an uppercase letter
        if (isupper(c))
        {
            // Encrypt uppercase letters
            char encrypted_char = ((c - 'A' + key) % 26) + 'A';
            printf("%c", encrypted_char);
        }
        // Check if the character is a lowercase letter
        else if (islower(c))
        {
            // Encrypt lowercase letters
            char encrypted_char = ((c - 'a' + key) % 26) + 'a';
            printf("%c", encrypted_char);
        }
        else
        {
            // Non-alphabetic characters remain unchanged
            printf("%c", c);
        }
    }
    printf("\n");
}