#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc==1){
		printf("Error\n");
		return 0;
	}

	int in = atoi(argv[1]);
	int n = in,rev=0;
	while(n!=0){
		int rem = n%10;
		rev = rev*10+rem;
		n/=10;
	}
	if(in==rev){
		printf("Given No is Palindrome\n");
	}else{
		printf("Given No is Not Palindrome\n");
	}

	return 0;
}