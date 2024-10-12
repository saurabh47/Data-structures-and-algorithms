// Problem 962. Maximum Width Ramp (Medium): https://leetcode.com/problems/maximum-width-ramp/
/**
 * @param {number[]} nums
 * @return {number}
 */

// Brute Force
var maxWidthRamp = function (nums) {
    var maxWidth = 0;
    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] <= nums[j]) {
                maxWidth = Math.max(maxWidth, j - i)
            }
        }
    }
    return maxWidth;
};


// Sliding window approach

var maxWidthRamp = function(nums) {
    let maxRight = Array.from({ length: nums.length });
    for(var i = nums.length - 1; i > -1; i--){
        if(i == nums.length - 1){   
            maxRight[i] = nums[i];
        }else{
            maxRight[i] = Math.max(nums[i],maxRight[i + 1]);
        }
    }

    left = 0
    var maxWidth = 0;
    for(var right = 0; right < nums.length; right++){
        while(nums[left] > maxRight[right]){
            left += 1
        }
        maxWidth = Math.max(maxWidth,right - left )
    }
    return maxWidth;
};