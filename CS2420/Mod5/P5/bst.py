"""Contains treeNode and Binary search tree"""
class TreeNode():
    """class tree node creates a node with parent and left and right child"""
    def __init__(self, value = None, parent = None):
        """initializer"""
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def left_child(self):
        """returns left child"""
        return self.left

    def right_child(self):
        """returns right child"""
        return self.right

    def set_left(self, node):
        """sets left child and parent"""
        self.left = node
        if node is not None:
            node.parent = self
        return node

    def set_right(self, node):
        """sets right child and parent"""
        self.right = node
        if node is not None:
            node.parent = self
        return node

    def get_parent(self):
        """returns parent"""
        return self.parent

    def set_value(self, value):
        """sets node value"""
        self.value = value

    def get_value(self):
        """returns node value"""
        return self.value

    def level(self):
        """returns what level the node is on"""
        result = 0
        temp = self
        while temp.parent is not None:
            temp = temp.parent
            result += 1
        return result

    def add(self, item):
        """figures out wether item should be left or right of root and adds it"""
        if item < self.value:
            if self.left_child() is None:
                self.set_left(TreeNode(item))
            else:
                self.left_child().add(item)
        else:
            if self.right_child() is None:
                self.set_right(TreeNode(item))
            else:
                self.right_child().add(item)

    def find(self, item):
        """finds target node"""
        if self.value == item:
            return self.value
        elif item < self.value:
            if self.left is not None:
                return self.left.find(item)
            else:
                raise ValueError()
        else:
            if self.right is not None:
                return self.right.find(item)
            else:
                raise ValueError()

    def InOrder(self, results):
        """returns nodes inorder"""
        if self.left is not None:
            self.left.InOrder(results)
        results.append(self.value)
        if self.right is not None:
            self.right.InOrder(results)

    def PreOrder(self, results):
        """returns node in preorder"""
        results.append(self.value)
        if self.left is not None:
            self.left.PreOrder(results)
        if self.right is not None:
            self.right.PreOrder(results)

    def PostOrder(self, results):
        """returns nodes in postorder"""
        if self.left is not None:
            self.left.PostOrder(results)
        if self.right is not None:
            self.right.PostOrder(results)
        results.append(self.value)

    def __str__(self):
        """returns value as string"""
        return str(self.value)

class BST():
    """class bst creates a binary search tree"""
    def __init__(self):
        """initializer"""
        self.root = None

    def is_empty(self):
        """returns bool val if BST is empty or not"""
        return self.root == None

    def size(self):
        """returns the size of BST"""
        return self.__size(self.root)

    def __size(self, node):
        """recursively finds size of BST"""
        if node is None:
            return 0
        result = 1
        result += self.__size(node.left)
        result += self.__size(node.right)
        return result

    def height(self):
        """returns height of BST"""
        return self.__height(self.root, 1)

    def __height(self, node, current):
        """recursively fins height of BST"""
        left_val = current
        right_val = current
        if node.left_child() is not None:
            left_val = self.__height(node.left, current + 1)
        if node.right_child() is not None:
            right_val = self.__height(node.right, current + 1)
        return max(left_val, right_val)

    def add(self, item):
        """adds item to BST"""
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.root.add(item)
        return self.root

    def remove(self, item):
        """returns removed item from BST"""
        return self.__remove(self.root, item)

    def __remove(self, node, item):
        """recursively removes item from bst and remakes tree"""
        #! Go through remove function together
        if node is None:
            return node
        if item < node.get_value():
            node.set_left(self.__remove(node.left_child(), item))
        elif item > node.get_value():
            node.set_right(self.__remove(node.right_child(), item))
        else:
            if node.left_child() is None:
                temp = node.right_child()
                if temp is not None:
                    temp.parent = node.parent
                node = None
                return temp
            elif node.right_child() is None:
                temp = node.left_child()
                if temp is not None:
                    temp.parent = node.parent
                node = None
                return temp
            else:
                minNode = self.__minValueNode(node.right_child())
                node.set_value(minNode.get_value())
                node.set_right(self.__remove(node.right_child(), minNode.get_value()))
        return node

    def __minValueNode(self, node):
        """helper function for remove"""
        current = node
        while current.left_child() is not None:
            current = current.left_child()
        return current

    def find(self, item):
        """finds and returns item"""
        if self.root is not None:
            return self.root.find(item)
        raise ValueError()

    def inorder(self):
        """returns a list of treenodes in order"""
        result = []
        if self.root is not None:
            self.root.InOrder(result)
        return result

    def preorder(self):
        """returns a list of treenodes in preorder"""
        result = []
        if self.root is not None:
            self.root.PreOrder(result)
        return result

    def postorder(self):
        """returns a list of treenodes in postorder"""
        result = []
        if self.root is not None:
            self.root.PostOrder(result)
        return result

    def rebalance(self):
        """rebalances tree"""
        ordered_lyst = self.inorder()
        self.root = None
        self.__rebalance(ordered_lyst, 0, len(ordered_lyst)-1)

    def __rebalance(self, orderedList, low, high):
        """recursively rebalances treenode"""
        if low <= high:
            mid = (high - low) // 2 + low
            self.add(orderedList[mid])
            self.__rebalance(orderedList, low, mid - 1)
            self.__rebalance(orderedList, mid + 1, high)

    def __str__(self):
        self.__recurStr(self.root)
    
    def __recurStr(self, node):
        result = ""
        for i in range(node.level()):
            result += " "
        result += str(node.level()) + str(node.get_value())
        print(result)
        if node.left_child() is not None:
            self.__recurStr(node.left_child())
        if node.right_child() is not None:
            self.__recurStr(node.right_child())
        