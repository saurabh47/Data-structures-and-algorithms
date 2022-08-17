#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc!=3)
		return 0;
	int a,b,S;
	a = atoi(argv[1]);
	b = atoi(argv[2]);

	for(S=a<b?a:b;S>=1;S--)
		if(a%S==0&&b%S==0)
			break;

	printf("HCF/GCD OF GIVEN TWO NO IS %d\n",S);

	return 0;
}