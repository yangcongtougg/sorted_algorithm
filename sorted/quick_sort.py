# _*_ coding: utf-8 _*_
# @Time     :2018/3/6 10:10
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    快速排序：(从序列的第一个值开始)直接确定元素应该所在的位置,两个指针来夹击，low指针，high指针，low指针左边都应比待确定元素小，high指针右边应该比
    待确定元素大，然后移动两个指针，一旦中间有不符合规则的障碍，随即交换两个指针的值。确定好之后把序列分为两部分，按照相同的方式再处理这两部分。
"""
from random import randint


def quick_sort(arr, first, last):
    """快排的时间复杂度为n*2，每次切分的时候后没有二分出来
        最优为nlogn

    """
    if first >= last:
        return
    mid_value = arr[first]  # 基准值
    low_point = first
    high_point = last

    while low_point < high_point:  # 下面两段代码交替执行，只要两个指针没有相交，会循环下去一层循环控制指针，一层循环控制交换

        # high_point 左移
        while low_point < high_point and arr[high_point] >= mid_value:  # 有相同的数的时候左移或者右移只能其中一个包含等号、把相等的元素控制在同一侧。
            high_point -= 1
        arr[low_point] = arr[high_point]
        # low_point += 1

        # low_point 右移
        while low_point < high_point and arr[low_point] < mid_value:
            low_point += 1
        arr[high_point] = arr[low_point]
        # high_point -= 1

        # 从循环退出的时候，low=high
        arr[low_point] = mid_value

        # 左半部分
        quick_sort(arr, first, low_point - 1)  # 切片之后会产生新的列表，但是快排希望是在原有的列表上操作，所以不用切片,操作指针
        # 右半部分
        quick_sort(arr, low_point + 1, last)


if __name__ == "__main__":
    a = [randint(0, 100) for i in range(10)]
    quick_sort(a, 0, len(a) - 1)
    print(a)
