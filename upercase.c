#include <stdio.h>
 
void upper_string(char []);
 
int main(int argc,char *argv[])
{
   char string[100];
   // = argv[1];

   printf("Enter a string to convert it into upper case\n");
   gets(string);
 
   upper_string(string);
 
   printf("The string in upper case: %s\n", string);
 
   return 0;
}
 
void upper_string(char *s) {
   int c = 0;
   while (*s != '\0') {
      if (*s >= 'a' && *s <= 'z') {
         *s = *s - 32;
         s++;
         //printf("%u\n", s);

      }
   }
}