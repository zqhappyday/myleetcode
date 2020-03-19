#题目是出奇的简单，没什么好说的
#给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#注意:
#假设字符串的长度不会超过 1010。

class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = {}
        res = 0
        k = 0
        for i in s:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for i in f:
            if f[i]%2 == 0:
                res = res + f[i]
            else:
                res = f[i] - 1 + res
                k = 1
        return (res + k)
