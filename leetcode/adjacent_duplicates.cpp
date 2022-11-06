### cpp equivalent of https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#include<iostream>
#include<stack>

using namespace std;
class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> stack;
        std::string result = "";
        for(int i=0; i< s.size(); i++){
            if(stack.empty() == 0){
                if(stack.top() != s[i]){
                    stack.push(s[i]);
                }else{
                    stack.pop();
                }
            }else{
                stack.push(s[i]);
            }
        }
        while(!stack.empty()){
            char c = stack.top();
            stack.pop();
            result += c;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

int main(){
    Solution s = Solution();
    std::string result = s.removeDuplicates("abbaca");
    std::cout<<result<<std::endl;
    return 0;
}