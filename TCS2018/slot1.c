/*
For the Sequence:-
1 1 2 3 4 9 8 27
find the nth term
*/
#include<stdio.h>

int power(int n,int p){
	int out=1;
	
	for(int i=1;i<=p;i++){
		out=out*n;
		//printf("%d\n",x);
	}
	return out;
}

int main(int argc,char *argv){
	
	int n;
	scanf("%d",&n);

	int out;
	int num;

	if(n%2==0){
		num = 3;
		int p =(n-1)/2;
		out = power(num,p);
		
	}else{
		num = 2;
		int p =n/2;
		out = power(num,p);
	}
	printf("%d\n",out);
	printf("4^3=%d\n",power(2,3) );
	return 0;
}
