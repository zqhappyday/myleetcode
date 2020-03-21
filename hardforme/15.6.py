'''
17.16. 按摩师
动态规划问题，从小偷到按摩师，第二次栽了，虽然是个easy题但对我来说
还是个hard类型
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
'''
class Solution:
    def massage(self, nums: List[int]) -> int:
        a,b=0,0
        for n in nums:
            b,a=max(a+n,b),b
        return b
#这代码从各个意义上都比我强得多。。。