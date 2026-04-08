class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = ["".join(sorted(string)) for string in strs]

        sorted_dic = {sorted_list[i]:[] for i,string in enumerate(strs)}

        for i,string in enumerate(strs):
            sorted_dic[sorted_list[i]] += [string]

        return list(sorted_dic.values())

