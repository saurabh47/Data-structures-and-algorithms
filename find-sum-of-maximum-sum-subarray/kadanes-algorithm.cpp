/*

This is O(N) in time complexity.

*/

#include<bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int>& arr) {
    int curr_sum=0, max_sum=INT_MIN;
    for(int i=0; i<arr.size();i++) {
        curr_sum += arr[i];
        max_sum = max(max_sum, curr_sum);
        if(curr_sum < 0)
            curr_sum=0;
    }
    return max_sum;
}

int main() {
    vector<int> arr{2,-3,4,5,-1};
    int res = maxSubArray(arr);
    cout<<"Sum of Maximum sum subarray is "<<res<<"\n";
}