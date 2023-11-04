#include <stdio.h>

int fact(int n) {
    if (n <= 0) {
        return 1;
    }
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    fact(5);
    return 0;
}