//hexadecimal To Binary
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int hexadecimalToDecimal(char hexVal[]);
void decimalToBinary(int decimal);

int main(int argc, char *argv[])
{
    int strsize = strlen(argv[1]);
    char *cmdstring;
    cmdstring = malloc(strsize);
    int decimal;
    strcpy(cmdstring,argv[1]);
    decimal=hexadecimalToDecimal(cmdstring);
    decimalToBinary(decimal);
    return 0;

}

 // Function to convert hexadecimal to decimal
int hexadecimalToDecimal(char hexVal[])
{   
    int len = strlen(hexVal);
     
    // Initializing base value to 1, i.e 16^0
    int base = 1;
     
    int dec_val = 0;
     
    // Extracting characters as digits from last character
    for (int i=len-1; i>=0; i--)
    {   
        // if character lies in '0'-'9', converting 
        // it to integral 0-9 by subtracting 48 from
        // ASCII value.
        if (hexVal[i]>='0' && hexVal[i]<='9')
        {
            dec_val += (hexVal[i] - 48)*base;
                 
            // incrementing base by power
            base = base * 16;
        }
 
        // if character lies in 'A'-'F' , converting 
        // it to integral 10 - 15 by subtracting 55 
        // from ASCII value
        else if (hexVal[i]>='A' && hexVal[i]<='F')
        {
            dec_val += (hexVal[i] - 55)*base;
         
            // incrementing base by power
            base = base*16;
        }
    }
     
    return dec_val;
}
void decimalToBinary(int decimal){
    int binaryArr[1000];
    int i=0;
    while(decimal>0){
        binaryArr[i]=decimal%2;
        decimal=decimal/2;
        i++;
    }
    for(int j=i-1;j>=0;j--)
        printf("%d",binaryArr[j]);
}
