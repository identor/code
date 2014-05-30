/* Write a function rightrot(x,n) that returns the value of the 
 * integer x rotated to the right by n positions.
 */
#include <stdio.h>

unsigned int getbits(unsigned x, int p, int n);
unsigned int setbits(unsigned int x, int p, int n, unsigned int y);
unsigned int invert(unsigned x, int p, int n);
unsigned int rightrot(unsigned x, int n);
unsigned int bitcount(unsigned x);
void b_print(unsigned int x);
void b_println(unsigned int x);

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

/* bitcount: count 1 bits in x */
/*unsigned int bitcount(unsigned x) {
    int b;
    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}*/
unsigned int bitcount(unsigned x) {
    int b = 0;
    while ((!(b+=x&01)&&0) || (x >>= 1))
        ; 
    return b;
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
