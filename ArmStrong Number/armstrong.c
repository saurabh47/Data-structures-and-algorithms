int lengthh(char *string)
{
    int l=0;
    while(*string!='\0')
    {
        string++;
        l++;
    }
    return l;
}

int main(int argc,char*argv[])
{
    
    argv[1];
    
    int i=0,j=0,len,flag=0;
    
   
    len=lengthh(argv[1]);
    
    j=len-1;
    
  
    
    while(i<(len/2))
    {
        if(argv[1][i]!=argv[1][j])
        {
            flag=1;
            break;
        }
        i++;
        j--;
        
    
    
    if(flag==0)
    printf("Its a plaindrome");
    else
    printf("its not");
    
    
    return 0;
}

