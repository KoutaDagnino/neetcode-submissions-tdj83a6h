class Solution:
    def trap(self, height: List[int]) -> int:
        water_h = {i:[h,1000] for i,h in enumerate(height)}

        curr_h = 0
        for i,h in enumerate(height):
            if h > curr_h:
                curr_h = h
            water_h[i] = [h, curr_h]

        print(water_h)

        curr_h = 0
        result = 0
        for i in range(len(height)):
            h = height[-i-1]
            if h > curr_h:
                curr_h = h
            water_h[len(height)-i-1] = [h, min(curr_h, water_h[len(height)-i-1][1])]
            result += min(curr_h, water_h[len(height)-i-1][1]) - h
        
        return result
        
            
