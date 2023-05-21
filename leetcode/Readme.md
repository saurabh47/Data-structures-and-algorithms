## Leetcode

### [Problem 1. Two Sum](https://leetcode.com/problems/two-sum/)

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
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

### [Problem 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

A container with water is given. The container can be filled with water. The container has a length and width. The container can hold water up to the height of the container. Find two vertical lines, which together with the x-axis forms a container, such that the container contains the most water.

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
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
### [Problem 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
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

### [Problem 191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
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

### [Problem 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
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





