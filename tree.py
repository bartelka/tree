class Tree:
    def __init__(self, value):
        self.value = value
        self.right_side = None
        self.left_side = None

    def add_right(self, value):
        if self.right_side is None:
            temp = Tree(value)
            self.right_side = temp
        else:
            temp = Tree(value)
            temp.right_side = self.right_side
            self.right_side = temp

    def add_left(self, value):
        if self.left_side is None:
            temp = Tree(value)
            self.left_side = temp
        else:
            temp = Tree(value)
            temp.left_side = self.left_side
            self.left_side = temp

    def get_root_value(self):
        return self.value

    def get_right_tree(self):
        return self.right_side

    def get_left_tree(self):
        return self.left_side

    def preorder(self):
        print(self.value)
        if self.left_side:
            self.left_side.preorder()
        if self.right_side:
            self.right_side.preorder()

t = Tree(5)
t.add_left(8)
t.add_right(7)
t.get_right_tree().add_left(5)
t.get_right_tree().add_right(2)
t.get_left_tree().add_right(6)


t.preorder()

