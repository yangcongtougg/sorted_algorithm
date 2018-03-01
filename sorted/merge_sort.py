# _*_ coding: utf-8 _*_
# @Time     :2018/3/1 12:46
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    归并排序，利用递归分治来进行实现
"""


def merge_sort(arr):
    """拆分的过程，及递归退出条件"""

    n = len(arr)
    mid = n // 2
    if n <= 1:
        return arr  # 仅有一个元素的时候直接返回

    # left right 采用归并排序后形成的新的有序的列表
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    """直到merge_sort有返回值的时候，下面的代码才会执行(有返回值的时候下面也是递归执行)，相当于先拆分最后进行排序合并(新列表上操作)"""

    left_point, right_point = 0, 0  # 进行两两比较时的操作指针
    result = []

    while left_point < len(left_arr) and right_point < len(right_arr):  # 两两比较的循环控制条件，指针完成左右两个列表的遍历
        if left_arr[left_point] <= right_arr[right_point]:  # 这里的条件判断+一个=号就保证了归并排序的稳定性
            result.append(left_arr[left_point])
            left_point += 1
        else:
            result.append(right_arr[right_point])
            right_point += 1
    result += left_arr[left_point:]  # 切片操作越界的话不会报错会返回空列表，包含了上面的while循环控制条件的范围
    result += right_arr[right_point:]
    return result


# 归并排序操作的是新列表，空间上需要额外的开销
if __name__ == "__main__":
    arr = [123, 3123, 123123123, 45, 9, 0, 0, 6, 454, 23432547, 657463453, 4645, 12, 21, 3, 43078, 2346767]
    print(arr)  # 没变
    new_arr = merge_sort(arr)
    print(arr)  # 没变
    print(new_arr)  # 新列表
