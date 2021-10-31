#include<bits/stdc++.h>
using namespace std;

int longestConsecutive(vector<int> nums) {
    set<int> num_set;
    for (int num : nums) {
        num_set.insert(num);
    }

    int longestStreak = 0;

    for (int num : num_set) {
        if (num_set.find(num-1) == num_set.end()) {
            int currentNum = num;
            int currentStreak = 1;

            while (num_set.find(currentNum+1) != num_set.end()) {
                currentNum += 1;
                currentStreak += 1;
            }

            longestStreak = max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
}

int main() {
    vector<int> arr{100,4,200,1,3,2};
    int ans = longestConsecutive(arr);
    cout<<"Longest Consecutive Sequence is "<<ans<<"\n";
}