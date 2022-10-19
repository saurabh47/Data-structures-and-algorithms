#include<stdio.h>

int main(int argc,char *argv[]){

	if(argc !=3){
		printf("Error\n");
		return 0;
	}

	int b = atoi(argv[1]);
	int h = atoi(argv[2]);
	float area = (float) (0.5)*b*h;

	printf("Area of Triangle is %.2f\n",area);

	return 0;
}
