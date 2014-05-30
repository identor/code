#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

#define BYTE_SIZE 8

/* Write a program to determine the ranges of char, short, 
 * int, and long variables, both signed and unsigned, by 
 * printing appropriate values from standard headers and 
 * by direct computation. Harder if you compute them: 
 * determine the ranges of the various floating-point 
 * types.
 */
int main() {
    printf("<char>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            CHAR_BIT, CHAR_MAX, CHAR_MIN);
    printf("<unsigned char>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            CHAR_BIT, UCHAR_MAX, CHAR_MIN);
    printf("<signed char>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            CHAR_BIT, SCHAR_MAX, SCHAR_MIN);
    putchar('\n');
    printf("<short>\n");
    int sbit = sizeof(short) * BYTE_SIZE;
    printf("size: %d bits, max: %d, min: %d\n",
            sbit, SHRT_MAX, SHRT_MIN);
    printf("<unsigned short>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            sbit, USHRT_MAX, 0);
    printf("<signed short>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            sbit, SHRT_MAX, SHRT_MIN);
    putchar('\n');
    printf("<int>\n");
    int intbit = sizeof(int) * BYTE_SIZE;
    printf("size: %d bits, max: %d, min: %d\n",
            intbit, INT_MAX, INT_MIN);
    printf("<unsigned int>\n");
    printf("size: %d bits, max: %u, min: %d\n",
            intbit, UINT_MAX, 0);
    printf("<signed int>\n");
    printf("size: %d bits, max: %d, min: %d\n",
            intbit, INT_MAX, INT_MIN);
    putchar('\n');
    printf("<long>\n");
    int lbit = sizeof(long) * BYTE_SIZE;
    printf("size: %d bits, max: %ld, min: %ld\n",
            lbit, LONG_MAX, LONG_MIN);
    printf("<unsigned long>\n");
    printf("size: %d bits, max: %lu, min: %d\n",
            lbit, ULONG_MAX, 0);
    printf("<signed long>\n");
    printf("size: %d bits, max: %ld, min: %ld\n",
            lbit, LONG_MAX, LONG_MIN);
    putchar('\n');
    printf("<float>\n");
    int fbit = sizeof(float) * BYTE_SIZE;
    printf("size: %d bits, max: %.0f, min: %.0f\n",
            fbit, FLT_MAX, FLT_MIN);
    printf("mantissa: %d, max_decimal_digits: %d\n",
            FLT_MANT_DIG, FLT_DIG);
    putchar('\n');
    printf("<double>\n");
    int dbit = sizeof(double) * BYTE_SIZE;
    printf("size: %d bits, max: %.0f, min: %.0f\n",
            dbit, DBL_MAX, DBL_MIN);
    printf("mantissa: %d, max_decimal_digits: %d\n",
            DBL_MANT_DIG, DBL_DIG);
    return EXIT_SUCCESS;
}
