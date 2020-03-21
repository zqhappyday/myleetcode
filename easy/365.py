'''
这题官方题解的写法很舒服，如果是我来写的话，估计会写出一堆if else
数学解法的思路也很奇特
虽然划分在medium，但个人觉得划分在easy会好些
深度搜索那个解法就算了，总耗时7777ms，简直非人类
'''
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
'''
https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/
'''