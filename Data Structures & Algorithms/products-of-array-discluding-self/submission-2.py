class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        left_right = [1]
        right_left = [1]

        for i in range(N):
            left_right.append(nums[i]*left_right[-1])
            right_left.append(nums[-i-1]*right_left[-1])
        
        print(left_right,right_left)

        output=[]
        for i in range(N):
            output.append(left_right[i]*right_left[N-i-1])
        return output