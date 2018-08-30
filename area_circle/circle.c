#include<stdio.h>
#define PI 3.14
int main(int argc,int *argv[]){

	if(argc==1){
		printf("Error\n");
		return 0;
	}

	int r = atoi(argv[1]);

	float area = (float) PI*r*r;

	printf("Area of Circle is %.2f\n",area);

	return 0;

}