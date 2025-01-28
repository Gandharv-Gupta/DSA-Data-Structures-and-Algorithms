#Simple Binary Tree

class binarytree:
    def __init__(self,data):#every node created will have inital values of left and right as none;
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,val):#we will call this method using a parent node,to create its child;that will either be its left child or right child
        #Root node
        if val==self.data:
            return#the current node=val 
        
        #LeftSubTree
        if val<self.data:#then we need to make the child node,a part of left subtree
            if self.left:#if our left subtree is NOT empty,then we will traverse through it and find the correct location of i/p node
                self.left.add_child(val)#recursively calling the method to find correct position
            else:#i.e our left subtree is empty;then make the i/p node-a left child of current node
                self.left=binarytree(val)
                return
        
        #RightSubTree
        if val>self.data:#then we need to make the child node,a part of right subtree
            if self.right:#if right subtree exists,traverse and find the correct locaiton
                self.right.add_child(val)
            else:#if no right child exist;then ake the i/p node, a right child of current node
                self.right=binarytree(val)
                return
    
    def print_tree_in_order(self):
        #A binary tree can only be printed using in-order,pre-order and post-order traversal way

        #IN ORDER TRAVERSAL:
        elements=[]

        #lst
        if self.left:
            elements+=self.left.print_tree_in_order()
        
        #root
        elements.append(self.data)

        #rst
        if self.right:
            elements+=self.right.print_tree_in_order()
        
        return elements

    def print_tree_pre_order(self):
        #A binary tree can only be printed using in-order,pre-order and post-order traversal way

        #IN ORDER TRAVERSAL:
        elements=[]

        
        #root
        elements.append(self.data) 
 
        #lst
        if self.left:
            elements+=self.left.print_tree_pre_order()

        #rst
        if self.right:
            elements+=self.right.print_tree_pre_order()
        
        return elements    

    def print_tree_post_order(self):
        #A binary tree can only be printed using in-order,pre-order and post-order traversal way

        #IN ORDER TRAVERSAL:
        elements=[]     
 
        #lst
        if self.left:
            elements+=self.left.print_tree_post_order()

        #rst
        if self.right:
            elements+=self.right.print_tree_post_order()
        
        #root
        elements.append(self.data)

        return elements    
    
    def search_tree(self,val):

        if val==self.data:#if val mateches current data
            return True
        
        if val<self.data:#lst
            if self.left:#is lst exists
                return self.left.search_tree(val)#recursively calling the fn to compare each element in the lst
            else:
                return False#for the condition that-val<data but the LST dosent exist/pr we reach the leaf node
            
        if val>self.data:#rst
            if self.right:#is lst exists
                return self.right.search_tree(val)#recursively calling the fn to compare each element in the rst
            else:
                return False#for the condition that-val<data but the RST dosent exist/pr we reach the leaf node

#creating a tree
l=[12,53,45,53,42,32,22,33,65,49]

print('The i/p is :\n',l,'\n')
root=binarytree(53)#choosing 53 as our root node

for i in l:
    if i==53:#skip this as its our root node already;although it will automatically skip it as in our code we have removed duplicates
        continue
    else:
        root.add_child(i)

print('In-Order Traversal:\n',root.print_tree_in_order(),'\n','\n')
print('Pre-Order Traversal:\n',root.print_tree_pre_order(),'\n','\n')
print('Post-Order Traversal:\n',root.print_tree_post_order(),'\n')
print('The program removed duplicates as well')