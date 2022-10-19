#include<bits/stdc++.h>

using namespace std;

bool static comp(string s1, string s2) {
    char c1 = s1[s1.size()-1], c2 = s2[s2.size()-1];
    return (int)c1 < (int)c2;
}

string sortSentence(string s) {
    int n=s.size();
    vector<string> v;
    string ans="", str="";
    for(int i=0; i<n-1; i++) {
        str+=s[i];
        if(s[i+1] == ' ') {
            i++;
            v.push_back(str);
            str="";
        }
    }
    str+=s[s.size()-1];
    v.push_back(str);

    sort(v.begin(), v.end(), comp);

    for(auto x : v) {
        string s = x.substr(0, x.size()-1);
        ans+=s;
        ans+=" ";
    }
    return ans.substr(0, ans.size()-1);
}

int main() {
    string ans = sortSentence("is2 sentence4 This1 a3");
    cout<<"After Sorting, the sentence becomes : " << ans<<"\n";
}