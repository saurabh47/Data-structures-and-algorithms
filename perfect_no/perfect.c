#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc ==1){
		printf("Error\n");
		return 0;
	}

	int in = atoi(argv[1]);
	int n=in,i=1,j=0,fact[100];
	int sum = 0;
	while(i<n){
		if(n%i==0){
			fact[j]=i;
			j++;
		}
		i++;
	}
	i=0;
	while(i<j){
		sum = sum + fact[i];
		i++;
	}

	if(sum == in &&(in!=0))
		printf("Number is Perfect No.\n");
	else
		printf("Number is Not Perfect No.\n");

	return 0;
}