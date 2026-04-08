class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {nums.count(x):[] for x in set(nums)}

        for x in set(nums):
            freq_dic[nums.count(x)]+=[x]

        result = []
        for key in sorted(freq_dic.keys()):
            result += freq_dic[key]

        return result[-k:]
