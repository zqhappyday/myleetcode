'''
经典题目，当初是通过这个题目学会了双指针
这题只要想到到了双指针就一点也不难
这题同样可以使用二分法来做，速度会快很多
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        res  = 0
        leftmax = 0
        rightmax = 0
        while right > left + 1 :
            if height[left] <= height[right]:
                leftmax = max(height[left],leftmax)
                if height[left + 1] <= leftmax:
                    res = leftmax - height[left+1] + res
                left += 1
            else:
                rightmax = max(height[right],rightmax)
                if height[right-1] <= rightmax:
                    res += rightmax - height[right-1] 
                right -= 1
        return res
