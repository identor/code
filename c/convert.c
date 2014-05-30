#include <stdio.h>
#include <stdlib.h>

#define UPPER 300
#define LOWER 0
#define STEP 20

int main() {
    int fahr;
    printf("%3c%8c\n", 'F', 'C');
    for (fahr = UPPER; fahr >= LOWER; fahr -= STEP) {
        float celc = (5.0/9.0) * (fahr-32);
        printf("%3d%8.2f\n", fahr, celc);
    }
    return EXIT_SUCCESS;
}

