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
            print(cur_node.item, end='')  # 打印元素
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    """深度遍历有三种方式存在
    三种遍历方式没有从right开始的方式，遍历方法树及子树的嵌套，依次按照顺序进行、按照规则撞到南墙再回头
    1、从root开始遍历root、left、right 先序遍历
    2、从left开始遍历left、root、right 中序遍历
    3、从left开始遍历left、right、root 后序遍历
    
    无论是什么序遍历，都是去打印相对的根节点,不要想太多简化问题，只不过是先处理左半部分还是右半部分的子树的问题
    
    """

    def preorder(self, root_node):  # 先序遍历,只要代码涉及到递归的话都是异常简单的，先序循环遍历都是在转换跟，需要把root传进去

        if root_node is None:  # 不是根或子根节点的话直接退出
            return
        print(root_node.item, end='')
        self.preorder(root_node.lchild)
        self.preorder(root_node.rchild)

    def inorder(self, root_node):  # 中序遍历
        if root_node is None:
            return
        self.inorder(root_node.lchild)
        print(root_node.item, end='')
        self.inorder(root_node.rchild)

    def postorder(self, root_node):  # 后序遍历
        if root_node is None:
            return
        self.postorder(root_node.lchild)
        self.postorder(root_node.rchild)
        print(root_node.item, end='')


"""给出两种遍历的结果把树画出来，但是必须包含中序的遍历结果，才能把树画出来，只有根节点才能把左右子树分开确定
    依次逻辑推断出根，分出左右进行判断。
"""

if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print('广度遍历')
    tree.breadth_travel()
    print(' ')
    print('深度先序遍历')
    tree.preorder(tree.root)
    print(' ')
    print('深度中序遍历')
    tree.inorder(tree.root)
    print(' ')
    print('深度后序遍历')
    tree.postorder(tree.root)
