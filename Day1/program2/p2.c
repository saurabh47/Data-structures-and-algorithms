#include<stdio.h>
#include <stdlib.h>

int strlength(char *ptr){
	int count=0;
	while(*ptr!='\0'){
			count++;
			ptr++;
		}
	return count;
}

int main(int argc,char *argv[]){
	int index=0;
	if(argc!=3){
		printf("Error");
	}else{
		//int s = atoi(argv[2][0]);
		char *out;
		int l1 = strlength(argv[1]);
		int l2 = strlength(argv[2]);

		//printf("%d\n",strlength(argv[1]));

		out = (char*)malloc(l1*sizeof(char));
		//printf("\nLength of str1=%d str2=%d\n",l1,l2);
		for(int i=0;i<l1;i++){
			int flag =0;
			for(int j=0;j<l2;j++){
				//printf("\ni=%d j=%d\n",i,j);
				if(argv[1][i]==argv[2][j]){
					//printf("Equal\n");
					flag = 0;
					break;
				}else{
					flag = 1;
					//printf("%c",argv[1][i]);
				}
			}
			if(flag){
				out[index] = argv[1][i];
				index++;
				//printf("%c",argv[1][i]);
			}

		}

		printf("%s\n",out);
	}
	return 0;
}