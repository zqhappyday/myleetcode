'''
1296. 划分数组为连续数字的集合
给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
如果可以，请返回 True；否则，返回 False。
---------------------------------------------------
使用collections进行字典创建，这种情况下使用不存在的key会返回0,可以避免KeyError
s = collections.Counter(nums)
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = collections.Counter(nums)
        ordered_nums = sorted(s)
        for num in ordered_nums:
            occ = s[num]
            if s[num] > 0:
                for i in range(num + 1, num + k):
                    if s[i] >= occ:
                        s[i] -= occ
                    else:
                        print(i,s[i])
                        return False
        return True

'-------------------'
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        if len(nums)%k != 0:
            return False
        nums.sort()
        f = {}
        for i in nums:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        for i in f:
            a = f[i]
            if a > 0:
                r = range(i,i+k)
                for j in r:
                    try:
                        f[j] -= a
                    except:
                        return False
        for i in f:
            if f[i] > 0 :
                return False
        return True