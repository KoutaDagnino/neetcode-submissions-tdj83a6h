class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            nums=set(nums)
            passed = {x:False for x in nums}
            result=0
            for x0 in nums:
                if passed[x0]==False:
                    length=1
                    passed[x0]=True
                    if (x0+1) in nums and (x0-1) in nums:
                        length+=2
                        x1=x0+1
                        x2=x0-1
                        passed[x1]=True
                        passed[x2]=True
                        while (x1+1) in nums:
                            length+=1
                            x1+=1
                            passed[x1]=True
                        while x2-1 in nums:
                            length+=1
                            x2-=1
                            passed[x2]=True
                    elif x0+1 in nums and x0-1 not in nums:
                        length+=1
                        x1=x0+1
                        passed[x1]=True
                        while x1+1 in nums:
                            length+=1
                            x1+=1
                            passed[x1]=True
                    elif x0+1 not in nums and x0-1 in nums:
                        length+=1
                        x2=x0-1
                        passed[x2]=True
                        while x2-1 in nums:
                            length+=1
                            x2-=1
                            passed[x2]=True
                    if length>result:
                        result = length
            return result

            