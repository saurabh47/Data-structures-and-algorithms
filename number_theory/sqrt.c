#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(int argc,char *argv[]){

	if(argc==1){
		printf("Error\n");
		return 0;
	}

	int n;
	n= atoi(argv[1]);
	float i=0.00;
	while(i*i<=n){
		printf("\ni= %f",i);
		i+=0.001;
	}
	i-=0.001;

	printf("Sqaure Root of Given No is %.4f\n",i);
	printf("Using squrt=%lf\n",sqrt(n));
	return 0;
}
