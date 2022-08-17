
#include <stdio.h>
#include<string.h>

int main (int argc,char *argv[]) {
   int i = 0;
   char c;
   char str[100];
   
  gets(str);
 
     
   
  for(i=0;str[i]!='\0';i++)
  {
      if(i==0)
      str[i]=toupper(str[i]);
      else if(str[i]==32)
      str[i+1]=toupper(str[i+1]);
  
  }
   
   printf("%s",str);
   

   return(0);
}
