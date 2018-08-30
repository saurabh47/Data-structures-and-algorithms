#include<stdio.h>

int main(){

	int n,space,p=1,q=1,s,val2;
	int tc[100];
	printf("Enter the values\n");
	scanf("%d",&n);

	//printf("%d\n",5/2);
	for(int i=0;i<n;i++){
		scanf("%d",&tc[i]);
	}
	for(int i=1;i<=n;i++){
		printf("i= %d %d\n",i,tc[i-1]);
		int cent = tc[i-1]/2+1;
		int z = cent-1;
		for(int j=1;j<=tc[i-1];j++,q=1){
			if(j<=cent){
				int val = j;
				for(space=1;space<=cent-j;space++){
						printf(" ");
					}
				while(q<=j){
						printf("%d ",val);
						val+=2;
						val2=val-2;
					q++;
				}
			printf("\n");
		}else{
			val2 = val2-1;
			q=1;
			for(space=1;space<=j-cent;space++){
				printf(" ");
			}
			while(q<=z){
				printf("%d ",val2);
				val2+=2;
				q++;
			}
			z--;
			printf("\n");
		}
	}

	}

	return 0;

}