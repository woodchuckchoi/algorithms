#include <stdio.h>
#include <stdlib.h>

int power(int num, int power) {
    if (power == 0) return 1;
    int out = 1;
    for (int i = 0; i < power; i++) {
        out *= num;
    }
    return out;
}

short toNth(int num, int nth) {
    int size = 1;

    while (1) {
        if (num < power(nth, size)) {
            break;
        }
        size += 1;
    }

    int* out = (int*)malloc(sizeof(int)*size);

    int index = size-1;
    while (num > 0) {
        out[index] = num % nth;
        index -= 1;
        num = num/nth;
    }
    
    for (int i = 0; i < size; i++) {
        printf("%d", out[i]);
    }

    printf("\n");

    for (int i = 0; i < size/2; i++) {
        if (out[i] != out[size-1-i]) {
            return 0;
        }
    }
    return 1;

}

int main() {
    int start = 10;
    while (1) {
        printf("Checking out %d...\n", start);
        if (toNth(start, 2) && toNth(start, 8) && toNth(start, 10)) {
            break;
        }
        start += 1;
    }
    printf("%d is the number!\n", start);
    return 0;
}