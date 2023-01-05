## Leetcode

#### [Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)

```
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
```
#### [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

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

### [215 Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Explanation: The 2nd largest element is 5.
```

### [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Explanation: "aba" is a palindrome, "bab" is a substring.
```

### [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Explanation:
P   A   H   N
A P L S I I G
Y   I   R
```

### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

```
Input: x = 123
Output: 321
```

### [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

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

### [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

```
Input: nums = [1,2,3,1]
Output: true
```

### [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```
Input: s = "anagram", t = "nagaram"
Output: true
```







