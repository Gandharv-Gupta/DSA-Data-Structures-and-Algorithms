#Finding minimum , maximum and sum of all values in a binary tree
# Min value in a tree-(Traverse to)The left most element of the tree
# Max value in a tree-(Traverse to) The right most  element of the tree


class binary_tree:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,val):
        if val==self.data:
            return
        
        if val<self.data:
            if  self.left:
                self.left.add_child(val)
            else:
                self.left=binary_tree(val)
        
        if val>self.data:
            if self.right:
                self.right.add_child(val)
            else :
                self.right=binary_tree(val)

    def find_min(self):#method to find the min value(traversing to the left most value) in the BT
        if self.left is None:#reaching the left most element ,which has its left element as none
            return self.data
        return self.left.find_min()#returning the data of the left most element;Also if self.left dosent exist,it will return the value of current node only
    
    def find_max(self):#method to find the ,ax value(traversing to the right most value) in the BT
        if self.right is None:
            return self.data
        return self.right.find_max()#returning the data of the right most element;Also if self.right dosent exist,it will return the value of current node only

      
    def find_sum(self):#method to find sum of all values in BT;We find sum using inorder traversal and them sum(list_in_order_traversal())
        values=[]
        if self.left:
            values+=self.left.find_sum()

        values.append(self.data)

        if self.right:
            values+=self.right.find_sum()
        
        return values
                  
        
    def print_tree_in_order(self):

        elements=[]

        if self.left:
            elements+=self.left.print_tree_in_order()
        
        elements.append(self.data)

        if self.right:
            elements+=self.right.print_tree_in_order()
        
        return elements
    
l=[23,32,33,11,43,34,45,54]
root=binary_tree(32)
for i in l:
    if i==32:
        continue
    else:
        root.add_child(i)

print(f'The input is:\n{l}\n')

print(f'In-Order Traversal is:\n{root.print_tree_in_order()}\n')

print(f'The Min value in BT is:\n{root.find_min()}\n')

print(f'The Max value in BT is:\n{root.find_max()}\n')

print(f'The Sum of all values in BT is:\n{sum(root.find_sum())}\n')



    
            
        