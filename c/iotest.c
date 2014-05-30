#include <stdio.h>
#include <stdlib.h>

int main() {
    int c;
    while ((c = getchar()) != EOF) {
        printf("Code: %d\n", c);
    }
    return EXIT_SUCCESS;
}

