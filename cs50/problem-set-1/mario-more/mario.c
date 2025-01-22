#include <stdio.h>

int main(void) {
    int height;

    // Prompt user for the height of the pyramid
    do {
        printf("Enter the height of the pyramid (1-8): ");
        scanf("%d", &height);
    } while (height < 1 || height > 8);

    // Generate the pyramid
    for (int i = 0; i < height; i++) {
        // Print spaces for the left side
        for (int j = 0; j < height - i - 1; j++) {
            printf(" ");
        }
        // Print hashes for the left side
        for (int k = 0; k <= i; k++) {
            printf("#");
        }
        // Print spaces between the two columns of hashes
        printf("  ");
        // Print hashes for the right side
        for (int k = 0; k <= i; k++) {
            printf("#");
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}