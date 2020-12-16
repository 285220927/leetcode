"""
  * @FileName: s303_range-sum-query-immutable.py
  * @Author:   zzc
  * @Date:     2020年12月05日 12:22:11
  * @Version   V1.0.0
"""

"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 
提示：
0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法
"""

"""
-2 0 3 -5 2 -1
-2 -2 1 -4 -2 -3
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        if not nums:
            return
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i - 1] + nums[i]

    def sumRange(self, i, j):
        if not self.nums:
            return 0
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    print(NumArray([-2, 0, 3, -5, 2, -1]).sumRange(2, 5))
