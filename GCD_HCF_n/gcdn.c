#include<stdio.h>
#define MAX 100000
int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	int S =MAX;

	for(int i=1;i<argc;i++){
		int a,b;
		a=atoi(argv[i]);
		S = a<S?a:S;
	}
	printf("Small No = %d\n",S);
	int flag = 1;
	for(S;S>=1;S--){
		for(int i=1;i<argc;i++){
			int n = atoi(argv[i]);
			printf("n=%d S=%d\n",n,S );
			if(n%S!=0){
				flag=0;
				break;
			}
		}
		if(flag)
			break;
		flag=1;
	}
	printf("HCF OF THE ARRAY IS %d\n",S);



	return 0;
}