#include <stdio.h>
#include <stdlib.h>

#define MAXLINE 1000

int nextline(char line[], int maxline);
void reverse(char s[]);

/* print the longest input line */
int main() {
    int len, max;
    char line[MAXLINE];
    char longest[MAXLINE];

    while ((len = nextline(line, MAXLINE)) > 0) {
        reverse(line);
        printf("%s\n", line);
    }
    return EXIT_SUCCESS;
}

/* nextline: read a line into s, return length */
int nextline(char s[], int lim) {
    int c, i;
    for (i=0; i < lim-1 && (c=getchar()) != EOF && c != '\n'; ++i) {
        s[i] = c;
    }

    s[i] = '\0';
    return i;
}

/* reverse: reverses s, given s is null terminated */
void reverse(char s[]) {
    int len, i;
    char r[MAXLINE];
    for (len = 0; s[len] != '\0'; ++len)
        r[len] = s[len];
    for (i = 0; i < len; ++i) {
        s[i] = r[len-1-i];
    }
    s[i] = '\0';
}
