class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}

        freq_group = [[] for i in range(len(nums))]

        for x in set(nums):
            count = nums.count(x)
            freq_dic[x]=count
            freq_group[count-1]+=[x]

        result=[]
        for i in range(len(freq_group)):
            if len(result)<k:
                result+=freq_group[-i-1]

        return result
