/* In a two's complement number system, x &= (x-1) deletes the 
 * rightmost 1-bit in x. Explain why. Use this observation to 
 * write a faster version of bitcount.
 * Answer: The assignment operation is more compact, the compact
 * assignment operation is used and eliminated the for loop in the
 * program.
 */
#include <stdlib.h>
#include <stdio.h>
#include "bits.h"

/* This only contains a tester check "bits.h" */
main() {
    /* */
    unsigned int x = 05555;
    b_println(x);
    printf("x: %d", bitcount(x));
    return EXIT_SUCCESS;
}
