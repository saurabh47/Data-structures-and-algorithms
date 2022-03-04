#include<stdio.h>

int getInt();

int middleNumber();

int searchNumber();

int main(void)
{

    int array[] ={3,5,7,21,34,54,76,89,90,93,95,96};
    int size = 12;
    printf("enter integer to search in array");
    int search = getInt();
    int start = 0;
    int end=11; // length-1
    int foundIndex = searchNumber(array,search,start,end);
    if(foundIndex != -1){
        printf("Number found at %d", foundIndex);
        return 0;
    }
    printf("Number not found");
    return -1;
}

int searchNumber(int arr[],int target, int start, int end)
{
    int midIndex = middleNumber(start,end);
    int mid = arr[midIndex];
    int length=end-start+1;
    if(length>0){
        if(target == mid)
        {
            return midIndex;
        }else if(target < mid)
        {
            int newEnd = midIndex-1;
            return searchNumber(arr,target,start,newEnd);
        }
        else if(target > mid){
            int newStart = midIndex+1;
        return searchNumber(arr,target,newStart,end);
        }
    }
    return -1;
}

int middleNumber(int start,int end)
{
    return start + (end - start)/2;
}


int getInt()
{
    int x;
    scanf("%d",&x);
    return x;
}