#include <stdio.h>
#include <stdlib.h>

/* 
 * Write a loop equivalent to the for loop above without using
 * && or ||.
 */
int main() {
    const int lim = 1000;
    char s[lim];
    int i, c;
    for (i=0; (i < lim-1) == ((c=getchar()) != '\n') == (c != EOF); ++i) {
        s[i] = c;
    }
    s[i] = '\0';
    printf("%s", s);
    return EXIT_SUCCESS;
}
