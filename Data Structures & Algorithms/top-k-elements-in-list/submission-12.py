class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {-nums.count(x):[] for x in set(nums)}

        for x in set(nums):
            freq_dic[-nums.count(x)]+=[x]

        tot = 0
        result = []
        for count in sorted(freq_dic.keys()):
            if len(result)<k:
                result+=freq_dic[count]

        return result
