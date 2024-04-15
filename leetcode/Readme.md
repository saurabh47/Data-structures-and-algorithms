## Leetcode

### Resources

Bit manipulation: https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently/

### [Problem 1. Two Sum](https://leetcode.com/problems/two-sum/)

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### [Problem 2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

#### [Problem 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string s, find the length of the longest substring without repeating characters.

```
input : "abcabcbb"
output : 3
Explanation : The answer is "abc", with the length of 3.
```

```
input : "bbbbb"
output : 1
Explanation : The answer is "b", with the length of 1.
```

### [Problem 4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

hint: sort the array and find the median

### [Problem 5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string s, return the longest palindromic substring in s.

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Explanation: "aba" is a palindrome, "bab" is a substring.
```

### [Problem 6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

Given a string s and an integer numRows, convert s into a zigzag pattern. More formally, convert s into a rows x numRows grid by placing each character in s in one of the rows, going from top to bottom row by row. Then, read the zigzag pattern from left to right. The characters in each row are read from left to right and the characters are concatenated to form a string.

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R
```

### [Problem 7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

```
Input: x = 123
Output: 321
```

### [Problem 8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

```
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
            ^
Step 3: "42" ("42" is read in)
              ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
```

### [Problem 9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Given an integer x, return true if x is a palindrome integer.

```
Input: x = 121
Output: true

Explanation: From left to right, it reads 121. From right to left, it becomes 121. Therefore it is a palindrome.
```

### [Problem 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

A container with water is given. The container can be filled with water. The container has a length and width. The container can hold water up to the height of the container. Find two vertical lines, which together with the x-axis forms a container, such that the container contains the most water.

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### [Problem 12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

Given an integer, convert it to a roman numeral.

```
Input: num = 3
Output: "III"

Explanation: The number 3 is written in Roman numerals as "III".
```

### [Problem 13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Given a roman numeral, convert it to an integer.

```
Input: s = "III"
Output: 3
Explanation: The numeral III is a representation of the number 3.
```

### [Problem 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

Explanation: The longest common prefix is "fl".
```

### [Problem 15. 3Sum](https://leetcode.com/problems/3sum/)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: The triplets are: [-1, 0, 1], [-1, -1, 2]
```

### [Problem 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

```
Input: s = "()"
Output: true
```

### [Problem 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Explanation: The linked list is [1,1,2,3,4,4].

```

### Problem 26. Remove Duplicates from Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```

### Problem 27. Remove Element (https://leetcode.com/problems/remove-element/)

Given an integer array nums and an integer val, remove all occurrences of val "in nums" in-place. The relative order of the elements may be changed.

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
```

### [Problem 28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

```
Input: haystack = "hello", needle = "ll"
Output: 2

Explanation: The first occurrence of "ll" is at index 2.
```

### Problem 29. Divide Two Integers (https://leetcode.com/problems/divide-two-integers/)

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
```

### [Problem 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Explanation: The target value is present at index 4.
```

### [Problem 35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

A sorted array of distinct integers is given. Find the index of the target value. If the target value is not found, return the index where it would be if it were inserted in order.

```
Input: nums = [1,3,5,6], target = 5
Output: 2
Explanation: 5 exists in nums and its index is 2.
```

### [Problem 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: The groupings are as follows:
"ate", "eat", and "tea" are all anagrams of each other, so they all belong to the same group.
"nat" and "tan" are anagrams of each other, so they all belong to the same group.
"bat" is not an anagram of any other word, so it its own group.
```

### [Problem 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Solved with 3 different approaches

1. Brute Force
2. Divide and Conquer
3. Kadane's Algorithm

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### [Problem 55. Jump Game](https://leetcode.com/problems/jump-game/)

Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you can reach the last index.

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### [Problem 58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

### [Problem 75. Sort Colors](https://leetcode.com/problems/sort-colors/)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Explanation: The output is the array in the correct order.
```

### [Problem 80 Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
```

### [Problem 83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

```
Input: head = [1,1,2]
Output: [1,2]

Explanation: The linked list is 1 -> 1 -> 2. After removing the duplicates, it is now 1 -> 2.
```

#### [Problem 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

hint: sort the array from the end

### [Problem 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
```

### [Problem 122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

### [Problem 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### [Problem 128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### [Problem 143. Reorder List](https://leetcode.com/problems/reorder-list/)

Given the head of a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Explanation: The reordered list is [1,4,2,3].
```

### [Problem 151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string s, reverse the order of the words.

```
Input: s = "the sky is blue"
Output: "blue is sky the"
Explanation: The words are reversed.
```

### [Problem 154. Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

- [4,5,6,7,0,1,4] if it was rotated 4 times.
- [0,1,4,4,5,6,7] if it was rotated 7 times.

```
Input: nums = [4,5,6,7,0,1,4]
Output: 0
Explanation: The original array was [0,1,4,4,5,6,7] rotated 4 times.
The smallest element is 0.
```

### [Problem 160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

```
Input: headA = [4,1,8,4,5], headB = [5,0,1,8,4,5]
Output: [8,4,5]
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
```

### [Problem 167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

(similar to problem 1)
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### [Problem 169. Majority Element](https://leetcode.com/problems/majority-element/)

Given an array nums of size n, return the majority element.

```
Input: nums = [3,2,3]
Output: 3
Explanation: The majority element is 3.
```

### [Problem 189. Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation: After rotating the array by 3 steps to the right, we get [5,6,7,1,2,3,4].
```

### [Problem 191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

### [Problem 202. Happy Number](https://leetcode.com/problems/happy-number/)

Write an algorithm to determine if a number n is happy.

```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

### [Problem 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Explanation: The linked list is 1 -> 2 -> 3 -> 4 -> 5. After reversing the linked list, the linked list becomes 5 -> 4 -> 3 -> 2 -> 1.
```

### [Problem 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

### [Problem 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Given an integer array nums and an integer k, return the kth largest element in the array.

```

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Explanation: The 2nd largest element is 5.

```

### [Problem 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```

Input: nums = [1,2,3,1]
Output: true

```

### [Problem 234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given the head of a singly linked list, return true if it is a palindrome.

```
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
```

### [Problem 237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

### [Problem 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

```

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: The array of the products of all other elements is [24,12,8,6]. The product of all the elements of nums is 24. So, for each index i in nums, we have nums[i] = 24 / nums[i].

```

### [Problem 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings s and t , write a function to determine if t is an anagram of s.

```

Input: s = "anagram", t = "nagaram"
Output: true
Explanation: Both s and t contain all the same letters, in the same frequency, so they are anagrams.
```

### [Problem 268. Missing Number](https://leetcode.com/problems/missing-number/)

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

### [Problem 274. H-Index](https://leetcode.com/problems/h-index/)

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return compute the researcher's h-index.

```
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: The researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations.
```

### [Problem 338. Counting Bits](https://leetcode.com/problems/counting-bits/)

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
number --> binary --> count of 1
0      -->   000  -->       0
1      -->   001  -->       1
2      -->   010  -->       1
3      -->   011  -->       2
4      -->   100  -->       1
5      -->   101  -->       2
```

### [Problem 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

```

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. In this case, the answer is [1,2] because both 1 and 2 appear twice, and 1 comes before 2.

```

### [Problem 380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

Design a data structure that supports all following operations in average O(1) time.

- insert(val): Inserts an item val to the set if not already present.
- remove(val): Removes an item val from the set if present.
- getRandom: Returns a random element from the current set of elements. Each element must have the same probability of being returned.

### [Problem 383. Ransom Note](https://leetcode.com/problems/ransom-note/)

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

```
Input: ransomNote = "aa", magazine = "aab"
Output: true
Explanation: ransomNote is "aa" and magazine is "aab", so ransomNote can be constructed from magazine.
```

### [Problem 392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

```
Input: s = "abc", t = "ahbgdc"
Output: true

Explanation: The string "abc" is a subsequence of "ahbgdc".
```

### [Problem 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### [Problem 451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string. If there are multiple answers, return any of them.

```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once. The answer can be "eetr" as well.
```

### [Problem 525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

### [Problem 704. Binary Search](https://leetcode.com/problems/binary-search/)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

### [Problem 706. Design HashMap](https://leetcode.com/problems/design-hashmap/)

Design a HashMap without using any built-in hash table libraries.

```
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
```

### [Problem 771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Explanation: All the stones are jewels, you have 3 jewels.
```

### [Problem 876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Given the head of a singly linked list, return the middle node of the linked list.

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

### [Problem 997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge. If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

```
Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
Explanation: The town judge is the person labeled 3. Everyone trusts 3 except for 3, and no one trusts 3.
```

Hint:

# The idea is to calculate incoming and outgoing edges

# for each person in the trust. Judge is a a person with n-1 incming edge and 0 outgoing edge.

explanation: https://www.youtube.com/watch?v=QiGaxdUINJ8

### [Problem 1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)

```
Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

### [Problem 1209. Remove all adjacent Duplicates II ]

```
Input : s = "deeedbbcccbdaa", k = 3
Output : "aa"
Explanation :
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
```

### [Problem 1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

```
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
```

### [Problem 1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.

```

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

```

### [Problem 1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

```

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

```

#### [Problem 1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

```

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:

- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
  You can take all the boxes of the first and second types, and one box of the third type.
  The total number of units will be = (1 _ 3) + (2 _ 2) + (1 \* 1) = 8.

```

#### [Problem 1859. Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)

```

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

```

### [Problem: 1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

```

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

```

### [Problem: 2220. (Easy): Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/)

```

You are given two numbers a and b. You need to find the number of bits you need to flip to convert a to b. Note: All given integers are in binary form.

```

Input: a = 10, b = 20
Output: 4
Explanation:
a = 01010
b = 10100
As we can see, the bits of a that need to be flipped are 01010. If we flip these bits, we get 10100, which is b. Hence, the number of bits that need to be flipped is 4.

```

```

```

```

X >> Y means x is shifted to the right by y bits. This is equivalent to dividing x by 2^y.
e.g 8 >> 1 = 4 (1000 >> 1 = 0100)

### [Problem 2640. (Medium) Find the score of all prefixes](https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array)

```
Input: nums = [2,3,7,5,10]
Output: [4,10,24,36,56]
Explanation:
For the prefix [2], the conversion array is [4] hence the score is 4
For the prefix [2, 3], the conversion array is [4, 6] hence the score is 10
For the prefix [2, 3, 7], the conversion array is [4, 6, 14] hence the score is 24
For the prefix [2, 3, 7, 5], the conversion array is [4, 6, 14, 12] hence the score is 36
For the prefix [2, 3, 7, 5, 10], the conversion array is [4, 6, 14, 12, 20] hence the score is 56
```
