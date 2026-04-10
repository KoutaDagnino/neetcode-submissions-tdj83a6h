class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,x in enumerate(numbers):
            y = target - x
            if y<=numbers[-1]:
                queue = True
                start = 0
                end = len(numbers)-1
                for j in range(len(bin(len(numbers)))-2):
                    print(start,end)
                    midpoint = (start+end)//2
                    if y == numbers[start] and start!=i:
                        return sorted([start+1,i+1])
                    elif y == numbers[midpoint] and midpoint!=i:
                        return sorted([midpoint+1,i+1])
                    elif y == numbers[end] and end!=i:
                        return sorted([end+1,i+1])
                    if numbers[midpoint] < y:
                        start = midpoint+1
                    elif numbers[midpoint] > y:
                        end = midpoint-1