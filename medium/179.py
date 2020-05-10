'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
示例 1:
输入: [10,2]
输出: 210
------------------------
其实就是定义了一组新的大小关系，将传统的大小变为了 由x+y > y+x 定义x，y的顺序
这样一来，使用普通的排序算法就都能解决，复杂度为O(nlgn)
官方题解使用了sorted函数，其中的KEY值如何使用有点没看懂。。 
'''
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

作者：LeetCode
链接：https://leetcode-cn.com/problems/largest-number/solution/zui-da-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
-----------------------
关于sortde函数的使用：
i = ['3','5','6','9','0']
class newaddkey(str):
    def __lt__(x,y):
        return x+y > y+x
t = sorted(i,key=newaddkey)
print(t)
运行结果为 ['9', '6', '5', '3', '0']
进行修改试探后发现：
    1，函数__lt__不可修改名称，否则会返回None，默认升序排列
    2，str为继承的父类，查阅资料后得知str里有某个函数使得这一程序可以运行，所以str不可删除
    
'''