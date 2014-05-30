#include <stdio.h>
#include <stdlib.h>

#define OUT 0
#define IN 1
#define NO_QUOTE -1

int main() {
    int c;
    int state = OUT;
    int quote = NO_QUOTE;
    while ((c = getchar()) != EOF) {
        if (c == '\'' || c == '\"') {
            if (quote == NO_QUOTE) {
                quote = c;
            } else if (quote == c) {
                quote = NO_QUOTE;
            }
        }
        if (c == '/' && quote == NO_QUOTE) {
            if ((c = getchar()) == '*') {
                state = IN;
            } else {
                putchar('/');
                putchar(c);
            }
        } else {
            if (state == IN) {
                if (c == '*') {
                    if ((c = getchar()) == '/') {
                        state = OUT;
                    } else {
                        printf("*/");                       
                    }
                }
            } else {
                putchar(c);
            }
        }
    }
    return EXIT_SUCCESS;
}
