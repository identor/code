#include <stdio.h>
#include <stdlib.h>

#define OUT 0
#define QUOTE 1
#define COMMENT 2

/* 
 * Write a program to check a C program for 
 * rudimentary syntax errors like unmatched
 * parentheses, brackets, and braces. Don't
 * forget about quotes, both single and
 * double, escape sequences, and comments.
 */
int main() {
    int state = OUT;
    int c, prev, quote;
    c = prev = quote = -1;
    /* balance variables */
    int parenthesis, bracket, brace;
    parenthesis = bracket = brace = 0;
    /* flags */
    int backslash, prematureclose;
    backslash = prematureclose = 0;
    while ((c = getchar()) != EOF) {
        if (state == OUT) {
            if (c == '\'' || c == '\"') {
                quote = c;
                state = QUOTE;
            }
            if (c == '*' && prev == '/') {
                state = COMMENT;
            }
            if (c == '(') {
                ++parenthesis;
            }
            if (c == ')') {
                --parenthesis;
            }
            if (c == '[') {
                ++bracket;
            }
            if (c == ']') {
                --bracket;
            }
            if (c == '{') {
                ++brace;
            }
            if (c == '}') {
                --brace;
            }
        } else if (state == COMMENT) {
            if (c == '/' && prev == '*') {
                state = OUT;
            }
        } else if (state == QUOTE) {
            if (quote == c) {
                state = OUT;
            }
            if (prev == '\\') {
                state = QUOTE;
            }
            if (backslash && quote == c) {
                state = OUT;
            }
        }
        /* for flags */
        if (parenthesis < 0 || brace < 0 || bracket < 0) {
            prematureclose = 1;
        }
        if (prev == '\\' && c == '\\') {
            backslash = 1;
        }
        prev = c; /* change previous character to current */
    }
    printf("Note: non-zero result -> Balance Error.\n");
    printf("PARENTHESIS: %d, BRACE: %d, BRACKET: %d\n",
            parenthesis, brace, bracket);
    if (prematureclose) {
        printf("Premature close Error!\n");
    } else {
        printf("No other error.\n");
    }
    return EXIT_SUCCESS;
}
