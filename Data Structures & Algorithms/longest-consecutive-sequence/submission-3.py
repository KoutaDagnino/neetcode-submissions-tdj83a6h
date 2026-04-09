class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        result=0
        for x in sorted_nums:
            x0=x
            length=1
            while x0+1 in sorted_nums:
                length+=1
                x0+=1
                sorted_nums.remove(x0)
            if length>result:
                result = length
        return result

            