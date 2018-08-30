#include<stdio.h>
#define MAX 1000

void fibonacci(int n);
void prime(int n);

int main(){
	int n;
	printf("Enter The No of the Term to Find In the Series\n");
	scanf("%d",&n);

	if(n%2==0){
		prime(n/2);

	}else{
		fibonacci(n/2+1);
	}

	return 0;
}

void fibonacci(int n){
	int t1=1,t2=1,term=1;

	for(int i=2;i<n;i++){
		t1=t2;
		t2= term;
		term =t1+t2;
	}

	printf("%d\n",term);

}

void prime(int n){

	int count = 0;

	for(int i=2;i<MAX;i++){
		int flag =0;
		for(int j=2;j<i;j++){
			if(i%j==0){
				flag =1;
				break;
			}
		}
		if(flag == 0){
			count++;
		}

		if(count==n){
			printf("%d\n",i);
			break;
		}
	}

}