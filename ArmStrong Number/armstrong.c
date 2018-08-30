#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[]){

	if(argc!= 2){
		printf("Error\n");
		return 0;
	}


	int n = atoi(argv[1]);
	printf("Given No is %d\n",n);
	int len=0;
	int no =n;
	int out=0;
	while(no!=0){
		no=no/10; 
		len++;
	}
	printf("Length = %d\n",len);

	no = n;
	while(no!=0){
		int rem = n%10;
		int val = 1;
		for(int i=0;i<len;i++){
			val = rem*val;
		}
		out = out +val;
		no/=10;
	}
	if(out==n){
		printf("No is Armstrong\n");
	}else{
		printf("No is Not Armstrong\n");
	}


	return 0;
}
