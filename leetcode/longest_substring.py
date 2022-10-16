def lengthOfLongestSubstring(self,s):
    count = 0;
    back = 0
    front = 0
    array = []
    while(front < len(s)):
        if(s[front] not in array):
            array.append(s[front])
            print(array)
            front += 1
            count = max(count, len(array))
        else:
            array.remove(s[back])
            back += 1
    return(max(count, len(array)))

lengthOfLongestSubstring("abcabcbb")