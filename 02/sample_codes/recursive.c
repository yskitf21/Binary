#include <stdio.h>

void f(int n) {
    if (n <= 0)
        return;
    printf("Recursive call: %d\n", n);
    f(n - 1);
}

int main() {
    printf("This is main function.\n");
    f(3);
    return 0;
}
