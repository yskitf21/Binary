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

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int square(int n) {
    int cnt = 0;
    int result = 1;
    while (cnt < 2) {
        result *= n;
        cnt++;
    }
    return result;
}

int func_switch(int choice, int n) {
    switch (choice) {
    case 1:
        return fact(n);
    case 2:
        return fib(n);
    case 3:
        return square(n);
    default:
        return 0;
    }
}

int main(void) {
    int choice;
    int n;
    printf("1. Factorial\n2. Fibonacci\n3. Square\n");
    printf("Choose an option: ");
    scanf("%d", &choice);
    printf("Enter a value for n: ");
    scanf("%d", &n);
    int result = func_switch(choice, n);
    printf("Result: %d\n", result);
    return 0;
}
