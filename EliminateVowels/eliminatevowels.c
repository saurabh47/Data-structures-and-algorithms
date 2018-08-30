#include<stdio.h>

int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	char arr[100];	
	
	int k=0;
	for(int i=0;argv[1][i]!='\0';i++){	
		if((argv[1][i]=='a') || (argv[1][i]=='e') || (argv[1][i]=='i') || (argv[1][i]=='o') || (argv[1][i]=='u')){}
		else{
			arr[k]=argv[1][i];									
			k++;	
		}
	}

	printf("%s\n", arr);

	return 0;
}
