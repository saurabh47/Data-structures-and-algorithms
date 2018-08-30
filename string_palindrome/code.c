#include<stdio.h>
#include<string.h>

int getLen(char *p){
	int l=0;
	while(*p!='\0'){
		p++;
		l++;
	}
	return l;
}

int main(int argc,char *argv[]){

	if(argc==1){
		printf("Error\n");
		return 0;
	}
	//printf("Length L = %d\n",getLen(argv[1]));

	int i=0,flag=0;
	int L = getLen(argv[1]),j = L-1;
	while(i<=L/2){
		if(argv[1][i]!=argv[1][j]){
			flag =1;
			break;
		}
		i++;
		j--;
	}

	

	if(flag){
		printf("Given string is Not Palindrome\n");
	}else{
		printf("Given string is Palindrome\n");
	}

	return 0;
}