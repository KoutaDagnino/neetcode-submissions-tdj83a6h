class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_num = sorted(nums)
        result=[]
        for i,x in enumerate(sort_num):
            target = -x
            numbers = sort_num[:i]+sort_num[i+1:]

            left = 0
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
                if sorted([x]+pair) not in result:
                    result.append(sorted([x]+pair))
        return result

            

