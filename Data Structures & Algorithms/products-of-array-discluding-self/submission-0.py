class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        prod_nozero=1
        for x in nums:
            prod*=x
            if x!=0:
                prod_nozero*=x

        output=[]
        for i,x in enumerate(nums):
            if x == 0:
                if 0 in nums[:i]+nums[i+1:]:
                    output.append(0)
                else:
                    output.append(prod_nozero)
            else:
                output.append(int(prod/x))

        return output