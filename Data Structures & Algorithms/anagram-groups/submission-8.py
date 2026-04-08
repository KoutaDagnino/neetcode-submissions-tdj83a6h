class Solution:
    def isAnagram(self,str1, str2):
        return "".join(sorted(str1))=="".join(sorted(str2))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped=[]
        while strs:
            str1 = strs[0]
            grouped.append([str1])
            strs.pop(0)
            for str2 in strs[:]:
                if self.isAnagram(str1,str2):
                    grouped[-1].append(str2)    
                    strs.pop(strs.index(str2))
        return grouped
