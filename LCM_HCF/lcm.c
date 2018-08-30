#include<stdio.h>

int main(){

	int a,b,L,i,MAX;

	printf("Enter the Two Numbers\n");
	scanf("%d%d",&a,&b);

	for(L=a>b?a:b;L<=a*b;L=L+(a>b?a:b)){
		printf("%d\n",L);
		if(L%a==0&&L%b==0)
			break;
	}

	printf("LCM of Given No = %d\n",L);


	return 0;
}