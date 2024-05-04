# Problem. 2640. Find Prefix Score (Medium): https://leetcode.com/problems/find-prefix-score/
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        scores = []
        max_num = 0
        conv_score = 0
        for i in range(len(nums)):
            if(nums[i] > max_num):
                max_num = nums[i]
            score = nums[i]+ max_num
            conv_score += score
            scores.append(conv_score)
        return scores

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(Solution().findPrefixScore(nums)) # [2, 5, 9, 14, 20]
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(Solution().findPrefixScore(nums)) # [2, 5, 9, 14, 20, 27, 35, 44, 54, 65]
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(Solution().findPrefixScore(nums)) # [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230]
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    print(Solution().findPrefixScore(nums)) # [2, 5, 9, 14, 20, 27, 35, 44, 54, 65, 77, 90, 104, 119, 135, 152, 170, 189, 209, 230, 252, 275, 299, 324, 350, 377, 405, 434, 464, 495, 527]
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    print(Solution().findPrefixScore(nums)) # [2, 5, 9, 14, 20, 27