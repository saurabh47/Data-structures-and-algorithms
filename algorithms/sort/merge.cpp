/*
 * File: merge.cpp
 * File Created: Saturday, 20th August 2022 3:58:59 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Saturday, 20th August 2022 8:08:12 pm
 * Modified By: Mahesh Jamdade
 * -----
 */


/*
Merge Sort is a Divide and Conquer algorithm.
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

ref:  https://www.youtube.com/watch?v=gR6nycuZKlM&t=7460s
 */

#include<iostream>

void print(int array[], int size);
int* mergeSort(int array[],int low, int high);
int * mergeHalves(int array1[], int array2[],int size1,int size2);

int main(int argc, char *argv[]){

    int array[]={3,5,1,2,4,8,6,7,9,234,123,12,54,23,121,54,76,879,56};
    int size = sizeof(array)/sizeof(array[0]);
    std::cout<<"size="<<size<<std::endl;
    int* sortedArray = mergeSort(array,0,size-1);
    print(sortedArray,size);
    return 0;
}

void print(int array[], int size){
    for(int i=0;i<size;i++){
        std::cout<<array[i]<<" ";
    }
    std::cout<<std::endl;
}

int* mergeSort(int array[],int low, int high){
    int size = high-low+1;
    // std::cout<<"low: "<<low<<" high: "<<high<<"size="<<size<<std::endl;
    if(size==1){
        int *b = new int[1];
        std::copy(array+low, array+low+1, b);
        return b;
    }else{
        int mid = low + (high-low)/2;
        // sort left half
        int* leftHalf = mergeSort(array,low,mid);
        // print(array,size);
        // sort right half
        int* rightHalf = mergeSort(array,mid+1,high);
        int size1 = mid-low+1;
        int size2 = high-mid;
        return mergeHalves(leftHalf,rightHalf,size1,size2);
    }
    return array;
}

int* mergeHalves(int array1[], int array2[],int size1,int size2){
    int leftIndex=0;
    int rightIndex=0;

    // final size of merged array
    int combinedSize = size1+size2;
    int* resultingArray = (int*) calloc(combinedSize, sizeof(int*));
    // std::cout<<"array1=";
    // print(array1,combinedSize);
    // std::cout<<"array2=";
    // print(array2,combinedSize);
    int i=0;
    while(i<combinedSize){
        if(array1[leftIndex]<array2[rightIndex] && leftIndex<size1){
            resultingArray[i] = array1[leftIndex];
            leftIndex++;
        }else if(array1[leftIndex]>array2[rightIndex] && rightIndex<size2){
            resultingArray[i] = array2[rightIndex];
            rightIndex++;
        }else{
            // one of the array has ended
            if(leftIndex<size1){
                resultingArray[i] = array1[leftIndex];
                leftIndex++;
            }
            if(rightIndex<size2){
                resultingArray[i] = array2[rightIndex];
                rightIndex++;
            }
        }
        i++;
    }
        return resultingArray;
}
