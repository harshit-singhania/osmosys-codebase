#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function to calculate the score of a word
int calculate_score(const char *word);

int main(void) {
    char player1_word[100];
    char player2_word[100];

    // Prompt Player 1 for their word
    printf("Player 1, enter your word: ");
    scanf("%s", player1_word);

    // Prompt Player 2 for their word
    printf("Player 2, enter your word: ");
    scanf("%s", player2_word);

    // Calculate scores
    int player1_score = calculate_score(player1_word);
    int player2_score = calculate_score(player2_word);

    // Determine the winner
    if (player1_score > player2_score) {
        printf("Player 1 wins!\n");
    } else if (player2_score > player1_score) {
        printf("Player 2 wins!\n");
    } else {
        printf("Tie!\n");
    }

    return 0;
}

// Function to calculate the score of a word
int calculate_score(const char *word) {
    int score = 0;
    // Define the point values for each letter
    int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // Calculate the score for the word
    for (int i = 0; word[i] != '\0'; i++) {
        char letter = toupper(word[i]); // Convert to uppercase
        if (letter >= 'A' && letter <= 'Z') {
            score += points[letter - 'A']; // Add the corresponding points
        }
    }

    return score;
}