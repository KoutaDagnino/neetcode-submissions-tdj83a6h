class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while True:
            x = numbers[left] + numbers[right]
            
            if x == target:
                return [left+1, right+1]

            elif x < target:
                if right == left+1:
                    right +=1
                else:
                    left += 1
            elif x > target:
                if left == right-1:
                    left -= 1
                else:
                    right -= 1

            