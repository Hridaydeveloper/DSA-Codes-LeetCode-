class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        else:
            left_max = []
            max_height = height[0]
            for i in range(len(height)):
                max_height = max(max_height, height[i])
                left_max.append(max_height)

            max_height = height[-1]
            right_max = []
            for i in range(len(height)-1,-1,-1):
                max_height = max(max_height, height[i])
                right_max.append(max_height)
            right_max.reverse()
            
            i = 0
            j = 0
            total = 0
            while i < len(left_max):
                min_height = min(left_max[i], right_max[j])
                water = min_height - height[i]
                total += water
                i += 1
                j += 1
        return total
  
