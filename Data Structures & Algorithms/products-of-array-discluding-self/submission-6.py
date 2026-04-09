class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        output = [0]*N

        prefix = 1
        for i in range(N):
            output[i] = prefix
            prefix*=nums[i]
        
        postfix = 1
        for i in range(N):
            output[-i-1]*=postfix
            postfix*=nums[-i-1]

        return output