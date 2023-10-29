#include <stdio.h>

int main() {
    int n;
    int a1 = 1;
    int a2 = 1;
    int sum = 0;
    int next = 0;

    printf("Enter the num ( > 0): ");
    scanf("%d", &n);
    if (n <= 0) {
        printf("Invalid input\n");
        return 1;
    } else if (n == 1) {
        sum = a1;
    } else if (n == 2) {
        sum = a1 + a2;
    } else {
        sum = a1 + a2; // 初めの2項の和
        for (int i = 3; i <= n; ++i) {
            next = a1 + a2;
            sum += next;
            a1 = a2;
            a2 = next;
        }
    }

    printf("The sum of fib(1) ~ fib(%d) = %d\n", n, sum);

    return 0;
}
