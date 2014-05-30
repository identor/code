#include <stdio.h>
#include <stdlib.h>

#define MAXLINE 1000

int nextline(char line[], int maxline);

/* print the longest input line */
int main() {
    int len, max;
    char line[MAXLINE];
    char longest[MAXLINE];

    while ((len = nextline(line, MAXLINE)) > 0) {
        if (len > 80) {
            printf("%s", line);
        }
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
