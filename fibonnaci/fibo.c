#include<stdio.h>

int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	int t1=1,t2=1,sum = 0;
	int in = atoi(argv[1]);
	int tnext=1;

	for(int i=1;i<=in;i++){
		t1= t2;
		t2= tnext;
		tnext = t1+t2;
		printf("%d ",t1);
	}
	printf("\nNth term=%d\n",t1);

	return 0;
}