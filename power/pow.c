#include<stdio.h>

int main(){

	int x,p,out=1;
	printf("Enter the No and its power\n");
	scanf("%d %d",&x,&p);

	for (int i = 1; i <=p; ++i)
	{
		out = x*out;
	}

	printf("%d^%d=%d\n",x,p,out);
	return 0;
}