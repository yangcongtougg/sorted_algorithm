# _*_ coding: utf-8 _*_
# @Time     :2018/3/1 17:11
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    实现二叉树和二叉树的添加

    理论上应该实现节点类和树的类
"""


class Node(object):
    """节点类"""

    def __init__(self, item):  # 树的节点上要保存数据，也就是要保存item
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = None  # 首先要创建root节点

    def add(self, item):  # 树的添加

        """添加数据往最后添加 实现完全二叉树的添加，找到添加数据的位置,一层一层的遍历，判断左孩子和右孩子是否存在数据
            遍历的方案使用广度优先遍历(横向遍历)，遍历的数据结构使用的是队列(广度遍历及层层遍历后，对节点依次进行判断
            左右孩子的情况，右边补充，左边读取，左边孩子都有的情况下抛弃)
        """

        node = Node(item)  # 首先构建节点
        if self.root is None:
            self.root = node
            return

        queue = []
        queue.append(self.root)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item)  # 打印元素
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    """深度遍历有三种方式存在
    三种遍历方式没有从right开始的方式，遍历方法树及子树的嵌套，依次按照顺序进行
    1、从root开始遍历root、left、right 先序遍历
    2、从left开始遍历left、root、right 中序遍历
    3、从left开始遍历left、right、root 后序遍历
    """





if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
