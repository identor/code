#include <stdio.h>
#include <stdlib.h>

#define MAXLINE 1000

int nextline(char line[], int maxline);
void copy(char to[], char from[]);

/* print the longest input line */
int main() {
    int len, max;
    char line[MAXLINE];
    char longest[MAXLINE];

    max = 0;
    while ((len = nextline(line, MAXLINE)) > 0) {
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    }
    if (max > 0) {  /* there was a line */
        printf("Size: %d\n%s", max, longest);
    }
    return EXIT_SUCCESS;
}

/* nextline: read a line into s, return length */
int nextline(char s[], int lim) {
    int c, i;
    for (i=0; i < lim-1 && (c=getchar()) != EOF && c != '\n'; ++i) {
        s[i] = c;
    }
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

/* copy: copy 'from' into 'to'; assume it is big enough */
void copy(char to[], char from[]) {
    int i;
    i = 0;
    while ((to[i] = from[i]) != '\0') {
        ++i;
    }
}
