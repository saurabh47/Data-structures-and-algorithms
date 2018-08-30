#include<stdio.h>
#include<math.h>

int main(int argc,char *argv[]){
	if(argc==1)
		return 0;
	int in = atoi(argv[1]);
	int n,i=0;
	n=in;
	int dec=0,bin = 0;
	while(n!=0){
		int r = n%10;
		dec= r*pow(8,i)+dec;
		n/=10;
		i++;
	}
	printf("Decimal = %d\n",dec);

	i=0;
	while(dec!=0){
		int r = dec%2;
		bin = bin +r*pow(10,i);
		dec/=2;
		i++;
	}
	printf("Binary = %d\n",bin);

	return 0;
}