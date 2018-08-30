#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc!=4)
		return 0;

	int a,b,c,S;
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	c = atoi(argv[3]);

	S=a<b?a:b;
	S=S<c?S:c;
	//printf("Small = %d \n",S);
	for(S;S>=1;S--)
		if(a%S==0&&b%S==0&&c%S==0)
			break;
	printf("HCF/GCF OF 3 No. is %d\n",S);

	return 0;
}