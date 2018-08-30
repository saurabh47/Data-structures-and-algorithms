#include<stdio.h>

int main(int argc,char *argv[]){
	int i=0;
	int val=argv[1][0];	  // 65-A Z-90 97-a 122-z
	char c;
	printf("%c",val);
	while(argv[1][i]!='\0'){
		val=argv[1][i];		
		if(val>=97 && val <=122){  // small letter
		    int k=val-32; //ascii val of caps char
			c=k;  // get char for that ascii
			argv[1][i]=c;				
		}
		if(val>=65 && val<=90){ // capital letter		
			int k=val+32;	//ascii value of small char
			c=k;
			argv[1][i]=c;
		}
		i++;	
	}
	printf("\n%s",argv[1]);			
	
return 0;
}
