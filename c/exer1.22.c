#include <stdio.h>
#include <stdlib.h>

#define OUT 0
#define IN 1
#define FOLD 40

int main() {
    int c;
    int state = OUT;
    int n = 0;
    while ((c = getchar()) != EOF) {
        ++n;
        if (c == '\n') {
            putchar(c);
            n = 0;
        } else if (n == FOLD) {
            n = 0;
            putchar('\n');
            state = OUT;
        } else {
            if (c == '\t' || c == ' ') {
                state = IN;
            } else {
                if (state == IN) {
                    n = 0;
                    putchar('\n');
                }
                state = OUT;
                putchar(c);
            }
        }
    }
    return EXIT_SUCCESS;
}
