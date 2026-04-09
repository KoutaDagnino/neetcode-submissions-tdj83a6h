class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        passed = {x: False for x in nums}
        result = 0

        for x0 in nums:
            if not passed[x0]:
                length = 1
                passed[x0] = True

                for step in (1, -1):
                    x = x0 + step
                    while x in nums:
                        length += 1
                        passed[x] = True
                        x += step

                result = max(result, length)

        return result