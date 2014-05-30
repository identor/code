#include <stdio.h>
#include <stdlib.h>

#define IN 1
#define OUT 0

int main() {
    int c = 0, state = OUT;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (state == IN) {
                putchar('\n');
            }
            state = OUT;
        } else {
            state = IN;
            putchar(c);
        }
    }
    return EXIT_SUCCESS;
}
