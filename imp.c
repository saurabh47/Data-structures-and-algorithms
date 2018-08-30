
/*
String Length Function without using string.h library
*/
int strlength(char *ptr){
	int count=0;
	while(*ptr!='\0'){
			count++;
			ptr++;
		}
	return count;
}