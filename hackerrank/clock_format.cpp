/*
 * File: clock_format.cpp
 * File Created: Monday, 22nd August 2022 9:25:16 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Tuesday, 23rd August 2022 8:32:05 am
 * Modified By: Mahesh Jamdade
 * -----
 * Copyright 2022 - 2022 Widget Media Labs
 */


#include<iostream>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string toStr(int x);

string timeConversion(string s) {
 int hours,minutes,seconds=0;
 hours = stoi(s.substr(0,2));
 minutes = stoi(s.substr(3,2));
 seconds = stoi(s.substr(6,2));
 string meridian = s.substr(8,2);
// cout<<"hours="<<hours<<"minutes="<<minutes<<"seconds="<<seconds<<endl;
 if(meridian.compare("AM")==0){
    if(hours<12){
        return toStr(hours)+":"+toStr(minutes)+":"+toStr(seconds);        
    }else if(hours==12){
        if(minutes==0){
            if(seconds==0){
                return "00:00:00";
            }else{
                hours=0;
                return toStr(hours)+":"+toStr(minutes)+":"+toStr(seconds);   
            }
        }else{
            hours=0;
            return toStr(hours)+":"+toStr(minutes)+":"+toStr(seconds);   
        }
    }
 }else{
     if(hours<12){
         hours+=12;
            return toStr(hours)+":"+toStr(minutes)+":"+toStr(seconds);   
     }else{
            return toStr(hours)+":"+toStr(minutes)+":"+toStr(seconds);   
     }
 }
 return s; 
}

string toStr(int x){
    if(x<10){
      return  "0"+to_string(x);
    }else{
      return to_string(x);
    }
}

int main()
{

    string s="12:01:00AM";

    string result = timeConversion(s);

    cout << result << "\n";

    return 0;
}
