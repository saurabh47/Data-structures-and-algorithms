/*
  to find sum of digits of a number
  without using any type of loop
*/

#include <stdio.h>

int main()
{   
    int n;
    int sum=0;
    scanf("%d",&n);
    label:
    if(n!=0){
        int temp = n%10;
        n = n /10;
        sum += temp;
    }
    if(sum >= 10 && n==0){
        n=sum;
        sum=0;
        goto label;
    }
    if(sum <10 && n!=0){
        goto label;
    }
    if(sum<10 &&  n==0){
        goto lab;
    }
    goto label;
    lab:
    printf("sum = %d",sum);
    return 0;
}
