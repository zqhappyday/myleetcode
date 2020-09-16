'''
5413. 重新排列句子中的单词
「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。
------------------------------
重新定义排序规则的题目，和179是同一种思路，同一种写法，话说这题刚开始想着用计数排序，
但看到长度限制就放弃了
答案公布后看看答案复杂度是多少
'''
class LargerNumKey(str):
    def __lt__(x, y):
        return len(x) < len(y)
class Solution:
    def arrangeWords(self, text: str) -> str:
        thelist = text.split(" ")
        thelist[0] = thelist[0].lower()
        thelist = sorted(thelist, key=LargerNumKey)
        thelist[0] = thelist[0].capitalize()
        res = " ".join(thelist)
        return res