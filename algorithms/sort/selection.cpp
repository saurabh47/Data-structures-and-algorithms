/*
 * File: selection.cpp
 * File Created: Saturday, 20th August 2022 11:57:07 am
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Saturday, 20th August 2022 12:24:55 pm
 * Modified By: Mahesh Jamdade
 * -----
 */



/*
In selection sort we iterate the list to find the smallest element of the array and
then swap it with the first element of the last iteration.
We repeat the above process for the next element and so on.
Until we reach the end of the array.
*/

#include<iostream>

int * selectionSort(int array[], int size);
int * swap(int array[], int low, int high);
int smallestIndex(int array[],int low,int size);

int main(int argc, char * argv[]){
    int array[] = {3,6,5,2,7,1,345,3,12,43,534,123,1243,23534,12311,3242,4534,121,122,4};
    int size = sizeof(array) / sizeof(array[0]);
    int *sortedArray = selectionSort(array, size);
    for(int i=0;i<size;i++){
        std::cout<<sortedArray[i]<<" ";
    }
    return 0;
}

int * selectionSort(int array[], int size){
    int low=0;
    while(low<size){
        int index = smallestIndex(array,low,size);
        array = swap(array,low,index);
        low++;
    }
    return array;
}

// returns the index of the smallest element in the array
int smallestIndex(int array[],int low,int size){
    int smallest = low;
    for(int i=low;i<size;i++){
        if(array[i]<array[smallest]){
            smallest = i;
        }
    }
    return smallest;
}

// swaps the elements at index low and index high for the given array
int * swap(int array[], int low, int high){
    int temp = array[low];
    array[low] = array[high];
    array[high] = temp;
    return array;
}