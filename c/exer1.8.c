#include <stdio.h>
#include <stdlib.h>

int main() {
    int c, nl, bl, sp;

    c = nl = bl = sp = 0; 
    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            ++nl;
        } else if (c == '\t') {
            ++bl;
        } else if (c == ' ') {
            ++sp;
        }
    }
    printf("%d %d %d\n", nl, bl, sp); 
    return EXIT_SUCCESS;
}
