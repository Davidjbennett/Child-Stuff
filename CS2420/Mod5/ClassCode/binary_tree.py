class BinaryTree:
    def __init__(self, val):
        self.root = [val, None, None]

    def get_left_child(self):
        return self.root[1]
    
    def get_right_child(self):
        return self.root[2]

    def set_root_value(self, val):
        self.root[0] = val

    def get_root_value(self):
        return self.root[0]

    def insert_left(self, val):
        self.root[1] = BinaryTree(val)

    def insert_right(self, val):
        self.root[2] = BinaryTree(val)

    def __str__(self):
        return self.__recursive_str(0)

    def __recursive_str(self, level):
        result = "\n"
        for i in range(level):
            result += "   |"
        result += str(self.root[0])
        if self.root[1] is not None:
            result += self.root[1].__recursive_str(level + 1)
        if self.root[2] is not None:
            result += self.root[2].__recursive_str(level + 1)
        return result

my_tree = BinaryTree(10)
my_tree.insert_left(5)
my_tree.insert_right(15)
my_tree.get_left_child().insert_left(2)
my_tree.get_left_child().insert_right(7)
my_tree.get_right_child().insert_left(12)
my_tree.get_right_child().insert_right(17)
print(str(my_tree))
