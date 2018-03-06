# _*_ coding: utf-8 _*_
# @Time     :2018/3/2 14:59
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************

    使用二分查找，要求是查找的序列首先应该是排序之后的序列,并支持下标索引
    二分查找只能作用到有序的list上


"""


def binary_search(arr, item):
    """二分查找,递归方式简便
        复杂度logn
    """
    n = len(arr)
    if n > 0:
        mid_point = n // 2
        if arr[mid_point] == item:
            return True
        elif item < arr[mid_point]:
            return binary_search(arr[:mid_point], item)
        else:
            return binary_search(arr[mid_point + 1:], item)
    return False


def binary_search_2(arr, item):
    """二分查找非递归版本
        主要起始位置的下标来确定中间元素
    """
    n = len(arr)
    first_point = 0
    last_point = n - 1
    while first_point <= last_point:
        mid_point = (first_point + last_point) // 2
        if arr[mid_point] == item:
            return True
        elif item < arr[mid_point]:
            last_point = mid_point - 1
        else:
            first_point = mid_point+1
    return False


if __name__ == '__main__':
    a = [0, 0, 3, 6, 9, 12, 21, 45, 123, 454, 3123, 4645, 43078, 2346767, 23432547, 123123123, 657463453]
    print(binary_search(a, 43078))
    print('*'*23)
    print(binary_search_2(a, 2))
