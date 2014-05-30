#include <stdio.h>
#include <stdlib.h>

void printspace(int n);

int main() {
    int c;
    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            printspace(4);
        } else {
            putchar(c);
        }
    }
    return EXIT_SUCCESS;
}

/* insertspace: inserts n spaces */
void printspace(int n) {
    while (n > 0) {
        putchar(' ');
        --n;
    }
}
