#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// Function prototypes
int count_letters(const char *text);
int count_words(const char *text);
int count_sentences(const char *text);
int calculate_index(int letters, int words, int sentences);

int main(void) {
    // Get input text from the user
    char text[1000]; // Buffer to hold the input text
    printf("Text: ");
    fgets(text, sizeof(text), stdin); // Read a line of text

    // Count letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate the Coleman-Liau index
    int index = calculate_index(letters, words, sentences);

    // Print the grade level
    if (index < 1) {
        printf("Before Grade 1\n");
    } else if (index >= 16) {
        printf("Grade 16+\n");
    } else {
        printf("Grade %d\n", index);
    }

    return 0;
}

// Function to count letters in the text
int count_letters(const char *text) {
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            count++;
        }
    }
    return count;
}

// Function to count words in the text
int count_words(const char *text) {
    int count = 0;
    bool in_word = false;
    for (int i = 0; text[i] != '\0'; i++) {
        if (isspace(text[i])) {
            in_word = false;
        } else if (!in_word) {
            in_word = true;
            count++;
        }
    }
    return count;
}

// Function to count sentences in the text
int count_sentences(const char *text) {
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            count++;
        }
    }
    return count;
}

// Function to calculate the Coleman-Liau index
int calculate_index(int letters, int words, int sentences) {
    float L = (float)letters / words * 100;
    float S = (float)sentences / words * 100;
    return (int)round(0.0588 * L - 0.296 * S - 15.8);
}