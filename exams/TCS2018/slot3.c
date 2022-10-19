/*
Problem Statement:-
1)Given three input as STDIN
2)Next input is given on Newline
3)For first word: Replace all characters that is Vowels with #
4)For Second Word: Replace all characters that is Consonant with $
5)For Third Word: Convert word into Upper case
for Example:-
Input:-
saurabh
mahesh
pamu
output:-
s##r#bh$a$e$$PAMU
*/
#include<stdio.h>

int main(){

	char in[3][20];
	int length[3];
	int i;
	for(i=0;i<=2;i++){
		scanf("%[^\n]%*c", in[i]);
		/*You can also use this for Reding the input
		int j =-1;
		while(in[i][j]!='\n'){
			j++;
			scanf("%c",&in[i][j]);
		}
		length[i]=j;
		in[i][j]='\0';*/
	}

	/*for(i=0;i<=2;i++){
		printf("%s\n", in[i]);
	}*/

	//Condition for First word Replace all Vowels With #
	i=0;
	while(in[0][i]!='\0'){
		if(in[0][i]=='a'||in[0][i]=='e'||in[0][i]=='i'|| in[0][i]=='o'||in[0][i]=='u'){
			in[0][i]='#';
		}
		i++;
	}
	//Condition for Second Word Replace all Consonant with $
	i=0;
	while(in[1][i]!='\0'){
		if(in[1][i]!='a'&& in[1][i]!='e'&& in[1][i]!='i'&& in[1][i]!='o'&& in[1][i]!='u'){
			in[1][i]='$';
		}
		i++;
	}

	//Condition for Third word Convert All charters to Uppercase
	i=0;
	while(in[2][i]!='\0'){
		if(in[2][i]>='a'&&in[2][i]<='z'){
			in[2][i]=in[2][i]-32;
		}
		i++;
	}
	for(i=0;i<=2;i++){
		printf("%s", in[i]);
	}
	printf("\n");
	/*scanf("%[^\n]%*c", in[0]);
	printf("%s\n", );*/
	return 0;

}
