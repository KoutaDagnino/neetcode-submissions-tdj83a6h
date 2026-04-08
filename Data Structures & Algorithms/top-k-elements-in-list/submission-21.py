class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}

        freq_group = [[] for i in range(len(nums))]

        for num in nums:
            freq_dic[num] = 1 + freq_dic.get(num, 0)
        
        for x, count in freq_dic.items():
            freq_group[count-1]+=[x]

        result=[]
        for i in range(len(freq_group)):
            if len(result)<k:
                result+=freq_group[-i-1]

        return result
