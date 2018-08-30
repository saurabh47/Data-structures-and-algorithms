#include<stdio.h>

void swap(int *a,int *b){
	int c=*a;
	*a = *b;
	*b = c;
}

int main(int argc,char *argv[]){
	if(argc!=3)
		return 0;

	int i1 = atoi(argv[1]);
	int i2 = atoi(argv[2]);

	/*int temp = i1;
	i1=i2;
	i2=i1;*/
	swap(&i1,&i2);

	printf("i1= %d,i2= %d\n",i1,i2);


	return 0;
}