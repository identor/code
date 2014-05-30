#include <stdio.h>
#include <stdlib.h>

#define IN 1
#define OUT 0

int main() {
    int c = 0, state = OUT, nc = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (state == IN) {
                printf("%d ", nc);
                nc = 0;
            }
            state = OUT;
        } else {
            ++nc;
            state = IN;
        }
    }
    putchar('\n');
    return EXIT_SUCCESS;
}
