
#include<stdio.h>

int main(int argc,char *argv[]){
	if(argc == 1)
		return 0;
	
	for(int i=1;i<argc;i++){
		if(argv[i][0]>=97&&argv[i][0]<=127){
			argv[i][0] = argv[i][0] -32;		
		}
	}	
	
	for(int i=1;i<argc;i++){
		printf("%s ",argv[i]);
	}
	

}
