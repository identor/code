#include <stdio.h>
#include <stdlib.h>

#define IN 1
#define OUT 0

int main() {
    int state = OUT, c = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            state = IN;
        } else {
            if (state == IN) {
                putchar(' ');
                state = OUT;
            }
            putchar(c);
        }
    }
    return EXIT_SUCCESS;
}
