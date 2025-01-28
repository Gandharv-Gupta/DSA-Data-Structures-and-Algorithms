# SIMPLE BINARY TREE
class tree_node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)

        if self.right:
            self.right.show()

root=tree_node(100)

root.left=tree_node(99)

root.right=tree_node(102)

root.show()



