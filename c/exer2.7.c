/* Write a function invert(x,p,n) that returns x with the n bits 
 * that begin at position p inverted (i.e., 1 changed into 0 and 
 * vice versa), leaving the others unchanged.
 */
#include <stdlib.h>
#include <stdio.h>

unsigned int getbits(unsigned x, int p, int n);
unsigned int setbits(unsigned int x, int p, int n, unsigned int y);
unsigned int invert(unsigned x, int p, int n);
void b_print(unsigned int x);
void b_println(unsigned int x);

main() {
    unsigned int x = ~0, y = 07;
    b_println(x);
    b_println(y);
    b_println(setbits(x, 4, 3, y));
    b_println(invert(x, 2, 2));
    return EXIT_SUCCESS;
}

/* getbits: get n bits from position p */
unsigned int getbits(unsigned x, int p, int n) {
    return (x >> (p+1-n)) & ~(~0 << n);
}

/* setbits: set n bits from position p of x by the bits of y */
unsigned int setbits(unsigned int x, int p, int n, unsigned int y) {
    return ((~(getbits(~0,p,n) << p-n+1) & x))
        + ((getbits(y,n-1,n) << p-n+1));
}

/* invert: returns the inverted bits of x from position p to n */
unsigned int invert(unsigned int x, int p, int n) {
    return setbits(x, p, n, ~getbits(x, p, n));
}

/* b_print: prints all the bits of x */
void b_print(unsigned int x) {
    int i;
    const int intbits = sizeof(int) * 8;
    for (i = 0; i < intbits; ++i) {
        if (getbits(x, intbits-1-i, 1)) {
            putchar('1');
        } else {
            putchar('0');
        }
    }
}

/* b_print: prints all the bits of x and a '\n' */
void b_println(unsigned int x) {
    b_print(x);
    putchar('\n');
}
