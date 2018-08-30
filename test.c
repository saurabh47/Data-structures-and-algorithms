#include<stdio.h>
#include<stdlib.h>

int main(){
	//printf("\nHello World\n");
	
/*int *i,*j;

	j=i;

	*i =1;
	i++;
	*i =2;
	i++;
	*i= 3;

	i[3]=4;

	for(int k=0;k<=3;k++)
		printf("i= %d\n",j[k]);*/

	/*int *i;

	i = (int*)malloc(5*sizeof(int));
	int k = 09;
	int p = k;
	i[0] = 2500055;
	i[1] = 1;
	i[2] = 2;
	i[3] = 3;
	i[4] = 4;
 	for(int j=0;j<5;j++){
		printf("%d\n",p);
	}
*/	//int j;
	//scanf("%d ",&j);
	void *p;
	int a = 10;
	float b =1.2;
	char c ='a';
	p=&a;
	printf("a=%d\n",*(int*)p);
	p=&b;
	printf("b=%.2f\n",*(float*)p);

	return 0;
}