'''
最开始的思路就是下面这个思路，但是没想到堆（主要是不会。。）
然后考虑下堆排序的问题，针对hp的排序，试过sort(),试过自己写，结果发现
堆和sort()显著高于我写的，，，虽然自己写的复杂的应该一样。。
所以结论是不要重复造轮子
'''




class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans