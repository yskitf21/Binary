#include <stdio.h>
#include <stdint.h>

int sum(int n){
    if(n<1){
        return 0;
    }
    else{
        int sum;
        int i;
        for(i = 1; i <= n; i++){
            sum += i;
        }
        return i;
    }
}

int main(void){
    int n = 10;
    printf("sum is %d\n", sum(n));
    return 0;
}