#include <stdio.h>
#include <stdlib.h>

int main() {
    int c;
    while ((c = getchar()) != EOF) {
        if (c == '\\') {
            putchar('\\');
            putchar('\\');
        } else if (c == '\t') {
            putchar('\\');
            putchar('t');
        } else if (c == '\b') {
            putchar('\\');
            putchar('b');
        } else {
            putchar(c);
        }
    }
    return EXIT_SUCCESS;
}
