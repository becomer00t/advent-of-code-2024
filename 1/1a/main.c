#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdint.h>

// Used for allocation of the heap for the numbers
#define NUMBER_COUNT 1000

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}


int main() {
    FILE* fd;
    if ((fd = fopen("../input.txt", "r")) == NULL) {
        perror("failed to open input.txt");
        exit(1);
    }

    int* leftArray = (int*) malloc(NUMBER_COUNT * sizeof(int));
    int* rightArray = (int*) malloc(NUMBER_COUNT * sizeof(int));

    // Parse in the numbers
    for (size_t i = 0; i < NUMBER_COUNT; i++) {
        if (fscanf(fd, "%d   %d", &leftArray[i], &rightArray[i]) != 2) {
            perror("failed to read line");
            exit(1);
        }
    }

    // Sort the items
    qsort(leftArray, NUMBER_COUNT, sizeof(int), compare);
    qsort(rightArray, NUMBER_COUNT, sizeof(int), compare);

    int diff = 0;
    for (size_t i = 0; i < NUMBER_COUNT; i++) {
        diff += abs(leftArray[i] - rightArray[i]);
    }

    printf("diff: %d\n", diff);

    return 0;
}
