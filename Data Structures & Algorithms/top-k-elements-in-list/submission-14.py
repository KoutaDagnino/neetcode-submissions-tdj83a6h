class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {} 
        for x in set(nums):
            freq = nums.count(x)
            
            if -freq not in freq_dic:
                freq_dic[-freq] = []                

            freq_dic[-freq]+=[x]

        result = []
        for count in sorted(freq_dic.keys()):
            if len(result)<k:
                result+=freq_dic[count]

        return result
