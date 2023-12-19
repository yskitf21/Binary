#include "tigress.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// 1からnまでの和を計算する関数
int sum(int n) {
    if (n < 1) {
        return 0;
    } else {
        int total = 0;
        int i;
        for (i = 1; i <= n; i++) {
            total += i;
        }
        return total;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    int n = atoi(argv[1]);
    printf("sum(%d) = %d\n", n, sum(n));
    return 0;
}