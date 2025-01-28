#A simple Genreal Tree

class gtree:
    def __init__(self,data):
        self.data=data#to store any value in the node
        self.children=[]#a lsit to store childrens of currnet nodes(note-all the children will also be instances of class gtree)
        self.parent=None#initalizing parnet =none(for root node) and for the rest nodes,we will update it
    
    def add_child(self,child):#child added here,will also be instance of class gtree
        child.parent=self#make the current node ,by which the child node is added-as the parent of current node
        self.children.append(child)#append child as children of the current node on which its called
    
    def get_level(self):#A fn. to get the level of the current node
        #NOTE-Level of a node=Number of parents it has(we can access the parens using self.parent property)
        #we go to the parent of the current node and count it and then make parent-the current node,and then we go to the parent of current node(i.e. parent node) adn so on
        level=0
        p=self.parent#assigning p=parent of the current i/p node
        while p:#unless the self.parent becomes NONE-i.e. we reach the root node
         
            level+=1
            p=p.parent
        return level

    #printing a general tree
    #way 1:
    def print_tree_normal(self):
        print(self.data)#printing value of root node
        for i in self.children:
            print(i.data)#printing value of  its children
            #NOTE-This dosent work if even children have children and hence we need to call the print_tree() fn. recursively to reach the leaf node
    
    #way2:
    def print_tree_recursion_simple(self):
        print(self.data)#print the data of current node
        for child in self.children:#go through all the childrens of the current node(that are instances themselves) and print their data recursively
            child.print_tree_recursion()

    #way3-USE THIS:Printing the tree based on LEVELS
    def print_tree_recursion_main(self):
        #first get the level of the current node:
        level=self.get_level()
        additional_symbol='|'
        prefix='-'*level*3+additional_symbol
        print(prefix+self.data)
        if self.children:#i.e. only if a child exists;i.e. do not continue after leaf node
            for child in self.children:
                child.print_tree_recursion_main()
            



root=gtree('AUTOMOBILES')



wheeler_2=gtree('2-WHEELERS')
wheeler_2.add_child(gtree('Honda'))
wheeler_2.add_child(gtree('Royal-enfield'))
wheeler_2.add_child(gtree('Harley-Davidson'))

wheeler_3=gtree('3-WHEELERS')
wheeler_3.add_child(gtree('Ferrari'))
wheeler_3.add_child(gtree('Mercedes'))
wheeler_3.add_child(gtree('Audi'))


root.add_child(wheeler_2)
root.add_child(wheeler_3)

# root.print_tree_normal()

# root.print_tree_recursion_simple()
root.print_tree_recursion_main()


