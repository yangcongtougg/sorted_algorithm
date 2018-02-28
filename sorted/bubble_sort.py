# _*_ coding: utf-8 _*_
# @Time     :2018/2/28 11:34
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    冒泡排序,从小到大排序以及增加了两种优化
"""


# 基本的冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 两两比较只需要进行n-1次
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 改进版本1
# 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
# 用一个标记记录这个状态即可。
def bubble_sort1(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = 1
        for j in range(n - 1 - i):  # 内循环比较的次数i级递减
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 0
        if flag:
            break
    return arr


# 改进版本2
# 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort2(arr):
    n = len(arr)
    k = n
    for i in range(n - 1):
        flag = 1
        for j in range(0, k - 1):  # 这里没有循环的递减i，而是根据数据交换的位置给定一个i
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 发生位置交换的是j+1的位置
                flag = 0
                k = j + 1
        if flag:
            break
    return arr


# test

a = [123, 2334, 4, 5, 6456, 23421, 6776, 8, 990, 123909, 1, 0]

bubble_sort2(a)
print(a)
