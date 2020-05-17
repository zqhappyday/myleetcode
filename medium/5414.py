'''
5414. 收藏清单
给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。
请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
----------------------
如果说5413感觉有点作弊的话，那么这题就是妥妥的取巧作弊了，从复杂度来看，思路至少是O(n^3)的
复杂度，说起来定义集合子集的方法还是不好写的，但PYTHON自带的方法后，感觉复杂度应该没下降但还是通过了
'''
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        f = favoriteCompanies
        n = len(f)
        res = []
        for i in range(n):
            f[i] = set(f[i])
        for i in range(n):
            rt = 0
            for j in range(n):
                if j == i :
                    continue
                if f[i].issubset(f[j]) :
                    rt = 1
            if rt == 0:
                res.append(i)
        return res