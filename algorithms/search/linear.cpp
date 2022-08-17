//
//  linear_search.cpp
//
//  Created by Mahesh Jamdade on 17/08/22.
//

#include <iostream>

int search(int x, int arr[], int size){
    for(int i=0;i<size;i++){
        if(arr[i]==x){
            /* Why do we return 0 ?
            0 = success
            any other number  = failure
            see https://youtu.be/gR6nycuZKlM?t=2159
            */
            return 0;
        }
    }
    return 1;
}

int main(int argc, const char * argv[]) {
   int array[] = {2,4,57,6,86,72,83,74,87,97,98,9,8,19,89,91,39,80};
    int size = sizeof(array) / sizeof(array[0]);
    int numberToSearch =-14;
   int result = search(numberToSearch, array, size);
   std::cout << ((result != 0)? "number not found " : "number found ")<< std::endl;
   return result;
}




