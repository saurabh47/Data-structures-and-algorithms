/*Count No. of days between Two dates
*/
#include<stdio.h>
#include<stdlib.h>

const int monthDays[12] = {31, 28, 31, 30, 31, 30,
                           31, 31, 30, 31, 30, 31};

//int date[3];
void getDate(char *day,int *date){
	char data[5];
	
	int i=0,j=0;

	while(*day!= '\0'){
		if(*day=='/'){
			data[i]='\0';
			i=0;
			date[j]=atoi(data);
			j++;
		}else{
			data[i]=*day;
			i++;
		}
		day++;
	}
	date[2]=atoi(data);
	/*for (int i = 0; i < 3; ++i)
	{
		printf("%d\n",date[i]);
	}*/
	//return date;
}

int countLeapYears(int *d)
{
    int years = d[2];
    printf("Year=%d\n",years );
 
    // Check if the current year needs to be considered
    // for the count of leap years or not
    if (d[1] <= 2)
        years--;
 
    // An year is a leap year if it is a multiple of 4,
    // multiple of 400 and not a multiple of 100.
    return years / 4 - years / 100 + years / 400;
}

int getDifference(int *dt1,int *dt2)
{
    // COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'
 
    // initialize count using years and day
    printf("D1=%d M1=%d y1 =%d \n",dt1[0],dt1[1],dt1[2]);
    printf("D2=%d M2=%d y2 =%d \n",dt2[0],dt2[1],dt2[2]);
    long int n1 = dt1[2]*365 + dt1[0];
 
    // Add days for months in given date
    for (int i=0; i<dt1[1] - 1; i++)
        n1 += monthDays[i];
 	
    // Since every leap year is of 366 days,
    // Add a day for every leap year
    n1 += countLeapYears(dt1);
 	
 	printf("No d1=%ld\n",n1);
    // SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'
 
    long int n2 = dt2[2]*365 + dt2[1];
    for (int i=0; i<dt2[1] - 1; i++)
        n2 += monthDays[i];
    n2 += countLeapYears(dt2);
    printf("No d2=%ld\n",n2);
 
    // return difference between two counts
    return (n2 - n1);
}


int main(int argc,char *argv[]){


	if(argc!=3){
		printf("Error\n");
		return 0;
	}
	/*int d1=getDate(argv[1])[0];
	int m1=getDate(argv[1])[1];
	int y1=getDate(argv[1])[2];

	int d2=getDate(argv[2])[0];
	int m2=getDate(argv[2])[1];
	int y2=getDate(argv[2])[2];*/

	int day1[3],day2[3]; 
	getDate(argv[1],day1);
	getDate(argv[2],day2);

	printf("No of Days=%d\n",getDifference(day1,day2));



	
	



	return 0;

}




	/*char *day = argv[1];
	char d1[3],m1[3],y1[5];
	int di1,mi1,yi1;
	int i=0,j=0;
	while(i<2){
		d1[j] = day[i];
		i++;
		j++;
	}
	d1[2]='\0';
	j=0;
	i=3;
	while(i<5){
		m1[j] =day[i];
		i++;
		j++;
	}
	j=0;
	i=6;
	m1[2]='\0';
	while(i<10){
		y1[j]=day[i];
		i++;
		j++;
	}
	//y1[4]='\0';
	
	printf("D1=%d\n",atoi(d1));
	printf("M1=%d\n", atoi(m1));
	printf("Y1=%d\n", atoi(y1));*/
