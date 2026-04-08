class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_list = [target-n for n in nums]
        common = [x for i,x in enumerate(nums) if x in diff_list[:i]+diff_list[i+1:]][0]
        print(common)
        if nums.index(common)!=diff_list.index(common):
            return sorted([nums.index(common),diff_list.index(common)])
        else:
            diff_list.pop(diff_list.index(common))
            return sorted([nums.index(common),diff_list.index(common)+1])