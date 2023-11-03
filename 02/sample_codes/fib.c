#include <stdio.h>

int fib(int n) {
    int a1 = 1;
    int a2 = 1;
    int result = 0;

    if (n == 1) {
        result = a1;
    } else if (n == 2) {
        result = a1 + a2;
    } else {
        for (int i = 3; i <= n; ++i) {
            result = a1 + a2;
            a1 = a2;
            a2 = result;
        }
    }
    return result;
}

int main() {
    int n = 9;
    printf("fib(%d) = %d\n", n, fib(n));
    return 0;
}
