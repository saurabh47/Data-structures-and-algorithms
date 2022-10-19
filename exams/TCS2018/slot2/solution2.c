
#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    if(n<2){
        int k=0;
        printf("%d",k);
    }
    else{
        if(n%2==0){
            int k=(n-2)/2;
            printf("%d",k);
        }
        else{
            printf("%d",n-1);
        }
        
    }
    return 0;
}
