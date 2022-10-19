#include<stdio.h>

enum bool{false,true};

enum bool isprime(int m){
		int count=0;
		if(m==1 || m==0)
			return false;
		for(int i=2;i<=m;i++){
			if(m%i==0){
				count++;
			}
		}
		if(count<=1)
			return true;
		else
			return false;
} 

int main(int argc,char *argv[]){
	int m = atoi(argv[1]);
	int n = atoi(argv[2]);
	int sum=0; 
	for(int i=m;i<=n;i++){
		int result = isprime(i);
		if(result==true) // no is prime	
			sum= sum+i;
		}
		printf("sum=%d",sum);
	return 0;  	
}
