class btnode:
    def __init__(self,data):#for creating first root node and then other nodes
        self.data=data
        self.left=None#initially we want both the right and left to be none
        self.right=None

    def add_child(self,val):

        if val==self.data:#BT is a set and cannot have duplicate values
            return
        
        if val<self.data:
            if self.left:#i.e. is self.left is not none
                self.left.add_child(val)
            else:
                self.left=btnode(val)#if we encouter none value
            
        if val>self.data:
            if self.right:#i.e. is self.right is not none
                self.right.add_child(val)
            else:
                self.right=btnode(val)

    def in_order_traversal(self):
        elements=[]

        #Adding LST:

        if self.left:
            elements+=self.left.in_order_traversal()

        #Adding root node
        elements.append(self.data)
        

        #aAdding RST
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

bt_nodes=[27,89,23,52,16,3,54,74,32]

def create_tree(nodes):

    root=btnode(nodes[0])#we chose the first element of the list as our root node

    #adding rest of the nodes:
    for i in range(1,len(nodes)):# adding bt_nodes[1] onwards as nodes in our tree
        root.add_child(nodes[i])
    
    print(root.in_order_traversal())


create_tree(bt_nodes)#calling our function to create tree







