/*
 * File: bubble.cpp
 * File Created: Saturday, 20th August 2022 12:29:29 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Saturday, 20th August 2022 1:16:24 pm
 * Modified By: Mahesh Jamdade
 * -----
 */


/*
In bubble sort we compare the first element with the next element and swap them,
if the first element is greater than the second element.
We repeat the above process until we reach the end of array.
We repeat the above process 0-n-1 times.

where n is the size of the array.

With each iteration we reduce the size of the array to be iterated by 1.
since them max item is at the end of the array.
*/

#include<iostream>

int * bubbleSort(int array[], int size);
int * swap(int array[], int low, int high);
void print(int array[], int size);
bool canSwap(int array[], int low, int high);

int main(int argc, char *argv[]){
    int array[] = {3, 13, 16, 20, 14, 26, 32, 41, 47,3, 49, 49, 51, 39, 55, 54, 13, 56, 56, 50, 57, 60,63,12, 32, 3, 18, 68, 58, 77, 31, 27, 55, 69, 11, 80, 81, 83, 83, 87, 88, 91, 91, 93, 93, 94, 94, 98, 98, 99};
    int size = sizeof(array) / sizeof(array[0]);
    int *sortedArray = bubbleSort(array, size);
    print(sortedArray,size);
    return 0;

}

int * bubbleSort(int array[], int size){
    for(int i=size-1;i>0;i--){
        for(int j=0;j<i;j++){
            if(canSwap(array,j,j+1)){
                array = swap(array,j,j+1);
            }
        }
        // std::cout<<"i="<<i<<" ";
        // print(array,size);
    }
    return array;
}

void print(int array[], int size){
    for(int i=0;i<size;i++){
        std::cout<<array[i]<<" ";
    }
    std::cout<<std::endl;
}

// if the element at index low is greater than the element at index high then swap them
// return true if the swap can be done else return false
bool canSwap(int array[], int low, int high){
    if(array[low]>array[high]){
        return true;
    }
    return false;
}

int * swap(int array[], int low, int high){
    int temp = array[low];
    array[low] = array[high];
    array[high] = temp;
    return array;
}