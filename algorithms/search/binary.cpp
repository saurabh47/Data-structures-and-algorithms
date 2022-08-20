#include<iostream>

/// recursive method
int binarySearch(int array[],int x,int low,int high){
    int mid = low+(high-low)/2;
    std::cout<<"mid="<<mid<<"low="<<low<<"high="<<high<<std::endl;
    int lengthOfArray = high-low+1;
    if(lengthOfArray>0){
        if(x==array[mid]){
            return mid;
        }
        else if(x<array[mid]){
            return binarySearch(array,x,low,mid-1);
        }
        else if(x>array[mid]){
            return binarySearch(array,x,mid+1,high);
        }else{
            // not found
            return -1;
        }
    }
        return -1;
}

/// iterative method

int binarySearchIterative(int array[],int x,int low,int high){
    int length = high-low+1; 
    while(length>0){
        int mid = low+(high-low)/2;
        if(x==array[mid]){
            return mid;
        }
        else if(x<array[mid]){
            high = mid-1;
        }
        else if(x>array[mid]){
            low = mid+1;
        }
        length = high-low+1;
    }
    return -1;
}

int main(int argc, char * argv[]){
    std::cout<<"enter number to search in a sorted array:";
    int numberToSearch;
    int hardCodedArray[] = {3,6, 7 , 34 , 35 , 54 , 56 , 65, 67};
    std::cin>>numberToSearch;
    int array[50];
    int size=0;
    if(argc>1){
        size = argc-1;
        for(int i=0;i<size;i++){
            array[i]= atoi(argv[i+1]);
        }
    }else{
        size = sizeof(hardCodedArray)/sizeof(hardCodedArray[0]);
        for(int i=0;i<size;i++){
            array[i] = hardCodedArray[i];
        }
    }
    int low=0;
    int high = size-1;
    // int result = binarySearch(array,numberToSearch,low,high);
    int result = binarySearchIterative(array,numberToSearch,low,high);

    if(result < 0){
        std::cout<<"number not found";
    }
    else{
        std::cout<<"number found at "<<result<<" position";
    }
    return 0;
}

// 1 2 3 4 5 6
// 0 1 2 3 4 5