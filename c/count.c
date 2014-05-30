#include <stdio.h>
#include <stdlib.h>

int main() {
    long nc = 0;
    while (getchar() != EOF) {
        ++nc;
    }
    printf("Input file size: %ld", nc);
    return EXIT_SUCCESS;
}
