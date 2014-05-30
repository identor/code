#include <stdio.h>
#include <stdlib.h>

int main() {
    int c = 0, i;
    int ndigit[256];
    for (i = 0; i < 256; ++i) {
        ndigit[i] = 0;
    }
    while ((c = getchar()) != EOF) {
       ++ndigit[c];
    }
    printf("%3s %3s %5s\n", "HEX", "DEC", "COUNT");
    for (i = 0; i < 256; ++i) {
        if (ndigit[i] > 0) {
            printf("%3x %3d %5d\n", i, i, ndigit[i]);
        }
    }
    return EXIT_SUCCESS;
}
