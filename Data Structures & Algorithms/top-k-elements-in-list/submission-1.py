class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {x:nums.count(x) for x in nums}
        _, freq_sorted = zip(*sorted(zip(list(freq_dic.values()), list(freq_dic.keys()))))
        return list(freq_sorted)[len(freq_dic.values())-k:]