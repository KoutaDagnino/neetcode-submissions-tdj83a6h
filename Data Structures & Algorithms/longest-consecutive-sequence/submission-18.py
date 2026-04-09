class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        passed = {x:False for x in nums}
        result=0
        for x0 in nums:
            if passed[x0]==False:
                length=1
                passed[x0]=True
                x1=x0+1
                x2=x0-1
                while x1 in nums:
                    passed[x1]=True
                    length+=1
                    x1+=1
                while x2 in nums:
                    passed[x2]=True
                    length+=1
                    x2-=1
                if length>result:
                    result = length
        return result

        