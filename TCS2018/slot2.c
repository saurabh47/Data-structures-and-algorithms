/*
Find the Nth Term of the Sequence
0 0 2 1 4 2 6 3
Using:-
Tn = a + (n-1)d
here a=0;
*/
#include<stdio.h>

int main(){
	int n,d1=2,d2 =1;
	scanf("%d",&n);
	int tn=0;
	if (n%2==0)
	{	n=n/2; //it Gives n = 1,2,3 for even numbers 2,4,5,7
		tn= (n-1)*d2;
		
	}else{
		n=1+n/2; //it Gives n = 1,2,3,4 for odd numbers 1,3,5,7
		tn= (n-1)*d1;
	}

	printf("Nth term =%d\n",tn);



	return 0;
}
