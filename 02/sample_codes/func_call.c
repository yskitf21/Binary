#include <stdio.h>

void functionA() { printf("A\n"); }

void functionB() {
    printf("B\n");
    functionA();
}

int main() {
    printf("main\n");
    functionA();
    functionB();
    return 0;
}
