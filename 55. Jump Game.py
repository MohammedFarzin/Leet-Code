from collections import defaultdict
from typing import Dict, List

class Solution:
    def canJump(self, nums) -> bool:
        jump = 0

        for n in nums:
            if jump < 0:
                return False
            elif n > jump:
                jump = n
            
            jump -= 1

        return True
    

nums = [2, 3, 1, 1, 4]

solution = Solution()
print(solution.canJump(nums))

