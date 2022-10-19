#include<stdio.h>

int fact(int n){

	if(n==0){
		return 1;
	}else{
		return n*fact(n-1);
	}
}

int main(int argc,char *argv[]){
	if(argc==1)
		return 0;

	int n = atoi(argv[1]);

	printf("Factorial of %d is %d\n",n,fact(n));

	return 0;
}