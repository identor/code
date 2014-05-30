/* Write an alternative version of squeeze(s1,s2) that deletes 
 * each character in s1 that matches any character in the string s2.
 */
#include <stdio.h>
#include <stdlib.h>

enum bool {false, true};

void squeeze(char s1[], char s2[]);

int main() {
    char s1[] = "alivealert";
    char s2[] = "aeii";
    squeeze(s1, s2);
    puts(s1);
    return EXIT_SUCCESS;
}

/* squeeze: delete all characters from s1 matching any character 
 * in s2 
 */
void squeeze(char s1[], char s2[]) {
    int i, j, k;
    int match = false;
    for (i = j = 0; s1[i] != '\0'; i++) {
        for (k = 0; s2[k] != '\0'; k++) {
            if (!match && s1[i] == s2[k]) {
                match = true;
            } 
        }
        if (match) {
            match = false;
        } else {
            s1[j++] = s1[i];
        }
    }
    s1[j] = '\0';
}

