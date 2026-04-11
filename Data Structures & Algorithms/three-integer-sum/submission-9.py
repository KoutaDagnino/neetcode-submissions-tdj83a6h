class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        result=[]
        x_prev=None
        for ind,x in enumerate(numbers):
            if x == x_prev:
                continue
            else:
                target = -x
                left = ind+1
                right = len(numbers) - 1
                pairs = []
                while left < right:
                    curr = numbers[left] + numbers[right]

                    if curr == target:
                        pairs.append([numbers[left],numbers[right]])

                        left_val = numbers[left]
                        right_val = numbers[right]
                        while left < right and numbers[left] == left_val:
                            left += 1
                        while left < right and numbers[right] == right_val:
                            right -= 1

                    elif curr < target:
                        left += 1
                    else:
                        right -= 1

                for pair in pairs:
                    result.append(sorted([x]+pair))
                x_prev=x
        return result

            

