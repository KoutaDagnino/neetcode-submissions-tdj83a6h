class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_list = [target-n for n in nums]
        common = [x for i,x in enumerate(nums) if x in diff_list[:i]+diff_list[i+1:]]
        return sorted([i for i,x in enumerate(nums) if x in common])