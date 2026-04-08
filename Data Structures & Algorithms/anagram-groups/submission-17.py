class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = ["".join(sorted(string)) for string in strs]

        sorted_dic = {}

        for i,string in enumerate(strs):
            if sorted_list[i] not in sorted_dic:
                sorted_dic[sorted_list[i]] = [string]
            else:
                sorted_dic[sorted_list[i]] += [string]

        return list(sorted_dic.values())

