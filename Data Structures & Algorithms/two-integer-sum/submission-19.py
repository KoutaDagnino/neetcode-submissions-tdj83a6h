class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {x:i for i,x in enumerate(nums)}
        for i,x in enumerate(nums):
            diff = target-x
            if diff in dic and dic[diff]!=i:
                return [i,dic[diff]]