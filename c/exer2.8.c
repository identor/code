/* Write a function rightrot(x,n) that returns the value of the 
 * integer x rotated to the right by n positions.
 */
#include <stdlib.h>
#include <stdio.h>

unsigned int getbits(unsigned x, int p, int n);
unsigned int setbits(unsigned int x, int p, int n, unsigned int y);
unsigned int invert(unsigned x, int p, int n);
unsigned int rightrot(unsigned x, int n);
void b_print(unsigned int x);
void b_println(unsigned int x);

main() {
    unsigned int x = ~0, y = 07;
    b_println(x);
    b_println(y);
    b_println(getbits(x, 0, 1));
    b_println(setbits(x, 4, 3, y));
    b_println(invert(x, 2, 2));
    b_println(rightrot(y, 1));
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

/* rightrot: returns x rotated to the right by n */
unsigned int rightrot(unsigned int x, int n) {
    int intbits = sizeof(int) * 8;
    return (x >> n) + setbits(0, intbits-1, n, getbits(x, n-1, n)); 
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
