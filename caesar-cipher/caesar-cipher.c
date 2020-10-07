#include <stdio.h>
#include <stdlib.h>

int main(){
    int n; 
    printf("Enter Input String Length: ");
    scanf("%d",&n);
    char upper[26];
    char lower[26];
    for(int i=0,m=65,l=97; i<26; i++){
        upper[i] = m++;
        lower[i] = l++;
    }
    char* s = (char *)malloc(10240000 * sizeof(char));
    printf("Enter Input String: ");
    scanf("%s",s);
    int k; 
    printf("Enter Key: ");
    scanf("%d",&k);
    for(int i=0; i<=n; i++){
      if(s[i]>=65 && s[i]<=90){
          int d = s[i] - 65;
          int rot = (d + k) % 26 ;
          s[i] = 65 + rot;
          
      }
        else if(s[i]>=97 && s[i]<=122){
            int d = s[i] - 97;
            int rot = (d + k) % 26;
            s[i] = 97 + rot;
        }
    }
    printf("Output %s",s);
    return 0;
}

/* 

Input 

11
ammj-igb
2

Output
cool-kid

*/
