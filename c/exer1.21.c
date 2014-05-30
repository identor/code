#include <stdio.h>
#include <stdlib.h>

#define OUT 0
#define IN 1
#define ENTAB 4

int main() {
    int c;
    int state = OUT;
    int space = 0;
    while ((c = getchar()) != EOF) {
        if (space == ENTAB && state == IN) {
            putchar('\t');
            space = 0;
        }
        if (c == ' ') {
            state = IN;
            ++space;        
        } else {
            while (space > 0) {
                putchar(' ');
                --space;
            }
            state = OUT;
            putchar(c);
        }
    }
    return EXIT_SUCCESS;
}
