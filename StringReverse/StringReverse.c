#include <stdio.h>

int sl(char *p)
{
    int l=0;
    while(*p!='\0')
    {
        l++;
        p++;
    }
    return l;
}

void main(int argc,char *argv[])

{
    
    char *s,r[100];
    int i;
    
    
   s=(argv[1]);
   
   int l=sl(s);
   int end=l-1;
   
   
  for(i=0;i<l;i++)
  {
      r[i]=s[end];
      end--;
      
  }
  r[i]='\0';
   
   printf("\n%s",r);
   
    
    
   
  
    getch();
}
