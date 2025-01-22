#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CANDIDATES 100
#define MAX_NAME_LENGTH 50

// Structure to hold candidate information
typedef struct
{
    char name[MAX_NAME_LENGTH];
    int votes;
} candidate;

// Function prototypes
void vote(candidate candidates[], int candidate_count, int voter_count);
void print_winner(candidate candidates[], int candidate_count);

int main(int argc, char *argv[])
{
    // Check for valid number of candidates
    if (argc < 2)
    {
        printf("Usage: ./plurality candidate1 candidate2 ...\n");
        return 1;
    }

    // Initialize candidates
    int candidate_count = argc - 1;
    candidate candidates[MAX_CANDIDATES];

    for (int i = 0; i < candidate_count; i++)
    {
        strcpy(candidates[i].name, argv[i + 1]);
        candidates[i].votes = 0; // Initialize votes to 0
    }

    // Get number of voters
    int voter_count;
    printf("Number of voters: ");
    scanf("%d", &voter_count);

    // Conduct voting
    vote(candidates, candidate_count, voter_count);

    // Print the winner
    print_winner(candidates, candidate_count);

    return 0;
}

void vote(candidate candidates[], int candidate_count, int voter_count)
{
    for (int i = 0; i < voter_count; i++)
    {
        char name[MAX_NAME_LENGTH];
        printf("Vote: ");
        scanf("%s", name);

        // Check if the vote is valid
        int valid_vote = 0;
        for (int j = 0; j < candidate_count; j++)
        {
            if (strcmp(candidates[j].name, name) == 0)
            {
                candidates[j].votes++;
                valid_vote = 1;
                break;
            }
        }

        // If the vote is invalid, notify the user
        if (!valid_vote)
        {
            printf("Invalid vote.\n");
            i--; // Decrement i to allow re-voting
        }
    }
}

void print_winner(candidate candidates[], int candidate_count)
{
    int max_votes = 0;

    // Find the maximum number of votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max_votes)
        {
            max_votes = candidates[i].votes;
        }
    }

    // Print the winner(s)
    printf("Winner(s): ");
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max_votes)
        {
            printf("%s ", candidates[i].name);
        }
    }
    printf("\n");
}