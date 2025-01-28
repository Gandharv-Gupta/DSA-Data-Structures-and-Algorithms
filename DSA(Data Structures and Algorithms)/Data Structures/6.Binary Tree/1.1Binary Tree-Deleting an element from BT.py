#deleting an element from binary tree
class binrarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,val):
        if val==self.data:
            return
        
        elif val<self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left=binrarytree(val)
        
        elif val>self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=binrarytree(val)

    def find_min(self):#This fn. will iterate to the left most element of the tree/subtree over whihch this fn will be called
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):#This fn. will iterate to the right most element of the tree/subtree over whihch this fn will be called
        if self.right is None:
            return self.data
        return self.right.find_max()    
    
    def delete_node(self,val):#val is the value to be deleted from the tree

        #we will keep finding the node using:
        if val<self.data:
            if self.left:
                self.left=self.left.delete_node(val)#stores the value returned from this fn. in self.left
        if val>self.data:
            if self.right:
                self.right=self.right.delete_node(val)#stores the value returned from this fn. in self.right
        #we keep on recursively calling the delete function until we get to a position where  val==self.data

        if val==self.data:#i.e. we found the value in the binary tree

            if self.left is None and self.right is None:#if both the children of the val(that we want to delete) are non i.e. a leaf node;
                return None#then simply replace the node to bedeleted with NONE
            
            elif self.left:#i.e the node to be deleted has a left child but not a right child
                return self.right#then replace the current node with self.right

            elif self.right:#i.e the node to be deleted has a right child but not a left child
                return self.left#then replace the current node with self.left
            
            #i.e the node to be deleted has both children(right sub tree and left sub tree)
            min_val=self.right.find_min()#find the minimum value from the right sub tree/or we can also find the ,ax value from lrft sub tree
            self.data=min_val#replace the value of current node  with min_val
            #now restructure the tree
            self.right=self.right.delete_node(min_val)#recursively perform this method to delete the duplicate value from the tree
        
        return self

    def print_tree_in_order(self):
        elements=[]

        if self.left:
            elements+=self.left.print_tree_in_order()
        
        elements.append(self.data)
        
        if self.right:
            elements+=self.right.print_tree_in_order()
        
        return elements
    

l=[10,20,30,40,50,60,70,80]
root=binrarytree(40)
for i in l:
    if i==40:
        continue
    else:
        root.add_child(i)

print(root.print_tree_in_order(),'\n')

print('Deleting 60 from the tree:')
root.delete_node(60)
print(root.print_tree_in_order())