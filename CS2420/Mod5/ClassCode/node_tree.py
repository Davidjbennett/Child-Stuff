class TreeNode:
    def __init__(self, val=None, parent=None):
        self.value = val
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

    def insert_left(self, node):
        self.left_child = node
        node.parent = self
        return node

    def insert_right(self, node):
        self.right_child = node
        node.parent = self
        return node
    
    def level(self):
        current = self
        result = 0
        while self.parent is not None:
            current = current.parent
            result += 1
        return self.parent
    
    def get_parent(self):
        return self.parent


    def __str__(self):
        return self.__recursive_str(0)

class BinaryTree2:
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root

    def height(self):
        return recursive_height(self.root, 0)

    def recursive_height(self, node, value):
        left_height = value
        right_height = value
        left_node = node.get_left_child()
        right_node = node.get_right_child()
        if left_node is not None:
            left_height = self.recursive_height(left_node, value+1)
        if right_node is not None:
            right_height = self.recursive_height(right_node, value+1)
        if left_node is None and right_node is None:
            return value
        return max(left_height, right_height)


my_tree = BinaryTree2()
my_tree.set_root(TreeNode(10))
my_tree.get_root().insert_left(TreeNode(5))
my_tree.get_root().insert_right(TreeNode(15))
my_tree.get_root().get_left_child().insert_left(TreeNode(2))
my_tree.get_root().get_left_child().insert_right(TreeNode(7))
my_tree.get_root().get_right_child().insert_left(TreeNode(12))
my_tree.get_root().get_right_child().insert_right(TreeNode(17))
print(my_tree.height())

