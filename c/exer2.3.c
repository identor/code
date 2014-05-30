/*
 * Write a function htoi(s), which converts a string of 
 * hexadecimal digits  (including an optional 0x or 0X) into 
 * its equivalent integer value. The allowable digits are 0
 * through 9, a through f, and A through F.
 */
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

enum bool {false, true};

int htoi(char s[]);
int ishexdigit(char s);
int hexval(char s);

int main() {
    return htoi("F");
    return EXIT_SUCCESS;
}

int htoi(char s[]) {
    int i, h;
    h = 0;
    if (s[0] == '0' && (s[1] == 'x' || s[1] == 'X')) {
        i = 2;
    } else {
        i = 0;
    }
    while (ishexdigit(s[i])) {
        h = h * 16 + (hexval(s[i++]));
    }
    return h;
}

int ishexdigit(char s) {
    return isdigit(s) 
        || (s >= 'A' && s <= 'F') 
        || (s >= 'a' && s <= 'f');
}

int hexval(char s) {
    if (isdigit(s)) {
        return s - '0';
    } else if (s >= 'A' && s <= 'F') {
        return 10 + s - 'A';
    } else if (s >= 'a' && s <= 'f') {
        return 10 + s - 'a';
    } else {
        return -1;
    }
}
