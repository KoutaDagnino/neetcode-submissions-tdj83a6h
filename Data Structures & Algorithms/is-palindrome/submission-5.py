class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x for x in s if x.isalnum()]
        for i in range(len(s)):
            if s[i].isalpha() and s[-i-1].isalpha():
                if s[i].lower()!=s[-i-1].lower():
                    return False
            elif s[i].isalpha()==False and s[-i-1].isalpha()==False:
                if s[i]!=s[-i-1]:
                    return False
            else:
                return False
        return True