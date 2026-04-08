class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {x: nums.count(x) for x in set(nums)}

        freq_group = [[] for i in range(len(nums))]

        for x in set(nums):
            count = freq_dic[x]
            freq_group[count-1]+=[x]

        print(freq_group)

        result=[]
        for i in range(len(freq_group)):
            if len(result)<k:
                result+=freq_group[-i-1]

        return result
