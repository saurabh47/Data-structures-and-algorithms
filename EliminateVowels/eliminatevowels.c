#include<stdio.h>

int main(int argc,char *argv[]){

	char arr[100];	
	
	int k=0;
	for(int i=0;argv[1][i]!='\0';i++){	
		if((argv[1][i]=='a') || (argv[1][i]=='e') || (argv[1][i]=='i') || (argv[1][i]=='o') || (argv[1][i]=='u')){}
		else{
			arr[k]=argv[1][i];									
			k++;	
		}
	}

	int z=0;
	while(arr[z]!='\0'){
		printf(" %c",arr[z]);
		z++;	
	}


	return 0;
}
