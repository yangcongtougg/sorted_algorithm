# _*_ coding: utf-8 _*_
# @Time     :2018/3/6 10:10
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    快速排序：(从序列的第一个值开始)直接确定元素应该所在的位置,两个指针来夹击，low指针，high指针，low指针左边都应比待确定元素小，high指针右边应该比
    待确定元素大，然后移动两个指针，一旦中间有不符合规则的障碍，随即交换两个指针的值。确定好之后把序列分为两部分，按照相同的方式再处理这两部分。
"""


def quick_sort(arr):
    n = len(arr)
    mid_value = arr[0]  # 基准值
    low_point = 0
    high_point = n - 1

    while low_point < high_point:  # 下面两段代码交替执行，只要两个指针没有相交，会循环下去一层循环控制指针，一层循环控制交换

        # high_point 左移
        while low_point < high_point and arr[high_point] >= mid_value:  # 有相同的数的时候左移或者右移只能其中一个包含等号、把相等的元素控制在同一侧。
            high_point -= 1
        arr[low_point] = arr[high_point]
        low_point += 1

        # low_point 右移
        while low_point < high_point and arr[low_point] < mid_value:
            low_point += 1
        arr[high_point] = arr[low_point]
        high_point -= 1
