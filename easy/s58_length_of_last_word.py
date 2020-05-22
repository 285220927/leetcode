"""
  * @FileName: s58_length_of_last_word.py
  * @Author:   zzc
  * @Date:     2020年01月30日 10:24:03
  * @Version   V1.0.0
"""

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。

示例:
输入: "Hello World"
输出: 5
"""


class Solution:
    @staticmethod
    def length_of_last_word_1(s: str):
        return len(s.rstrip().split(' ')[-1])


if __name__ == '__main__':
    print(Solution.length_of_last_word_1("a "))
