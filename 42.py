# Better solution --> TC: O(n) & SC: O(n)
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



# Optimul solution --> TC: O(n) & SC: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
          print(0)
          exit()
        else:
          l = 0
          r = len(height) - 1
          left_max = 0
          right_max = 0
          total = 0
        
          while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
              total += left_max - height[l]
              l += 1
            else:
              total += right_max - height[r]
              r -= 1
        return total
  
