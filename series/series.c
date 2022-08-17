/*
given input n it prints first n elements of this series
2,6,6,12,12,12,20,20,20,20,30,30,30,30,30....
*/

#include <stdio.h>

int main()
{
    int n,diff=2,val=0,count=0;
    printf("enter n:");
    scanf("%d",&n);
    for(int i=0;i<n;i++){
    	val=val+diff;
    	for (int j = 0; j <= i && count!=n; j++)
    	{
	       	printf("%d ",val);
	       	count=count+1;
    	}
       	diff=diff+2;
    }

    return 0;
}
