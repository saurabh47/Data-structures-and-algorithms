#include<stdio.h>
int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	int n = atoi(argv[1]);
	int i=2;
	while(i<argc){
		if(n==atoi(argv[i])){
			printf("Number Found at %d\n",i-1);
			return 0;
			//break;
		}
	i++;
	}
	printf("Number Not found\n");

return 0;
}
