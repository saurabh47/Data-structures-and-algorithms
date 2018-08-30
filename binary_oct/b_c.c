#include<math.h>
#include<stdio.h>

int main(int argc,char *argv[]){
	if(argc!=2)
		return 0;
	int n,in = atoi(argv[1]);
	n=in;
	int dec=0,oct=0,i=0;

	while(n!=0){
		int r = n%10;
		dec=dec+r*pow(2,i);
		i++;
		n/=10;
	}
	printf("Decimal = %d",dec);
	i=0;
	while(dec!=0){
		int r = dec%8;
		printf("\nReminder = %d",r);
		oct = oct+r*pow(10,i);
		printf("\nOCT = %d",oct);
		dec/=8;
		i++;
	}

	printf("\nOctal Number = %d\n",oct);

	return 0;
}