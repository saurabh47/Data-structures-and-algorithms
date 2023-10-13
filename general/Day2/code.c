#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc==1)
		return 0;
	int i=0,j=0,l=0,k=0;
	
	while(argv[1][i]!='\0'){
		l++;
		i++;
	}
	char out[l];
	//printf("Length =%d %s\n",l,argv[1]);
	for(j=l-1;j>=1;j--){
		char s = argv[1][j];
		int flag =1;
		for(i=j-1;i>=0;i--){
			if(s==argv[1][i]){
				flag =0;
				break;
			}
		}
		if(flag){
			//printf("c=%c\n",argv[1][j] );
			out[k]=argv[1][j];
			k++;
		}
	}
	out[k]=argv[1][0];

	while(k>=0){
		printf("%c",out[k]);
		k--;
	}
	printf("\n");
	return 0;
}