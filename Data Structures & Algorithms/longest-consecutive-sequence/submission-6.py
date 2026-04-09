class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        result=0
        for x in nums:
            x0=x
            length=1
            while x0+1 in nums:
                length+=1
                while x0 in nums:
                    nums.remove(x0)
                x0+=1
            if length>result:
                result = length
        return result

            