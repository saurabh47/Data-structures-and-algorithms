#include <stdio.h>

int power(int no,int p){
	int out =1;
	
	for(int i=0;i<p;i++){
		out = no*out;
	}
	return out;
}

int main(int argc, char const *argv[])
{
	if(argc!=4){
		printf("Error\n");
		return 0;
	}

	int n1 = atoi(argv[1]);
	int b1 = atoi(argv[2]);
	int b2 = atoi(argv[3]);
	int out[100];
	int no= 0,pow = 0;

	//printf("\n number = %d base1 = %d base2 = %d\n",n1,b1,b2);


	if(b1!=10){
		//Convert into decimal
		while(n1!=0){
			int rem = n1%10;
			//printf("\nreminder = %d n1 = %d",rem,n1);
			no= rem*power(b1,pow)+no;
			n1=n1/10;
			pow++;
		}
		//printf("\n base =%d no = %d\n",b1,no);
	}else{
		no =n1;
	}

	int i = 0;
	while(no!=0){
		//printf("i =%d\n",i);
		out[i] = no%b2;
		no = no/b2;
		i++;
	}
	i--;

	while(i>=0){
		//printf("i =%d\n",i);
		printf("%d",out[i]);
		i--;
	}
	printf("\n");


	return 0;
}