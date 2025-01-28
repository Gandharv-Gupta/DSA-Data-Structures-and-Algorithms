#Insert an element in the LL after a specific value

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        new_node=node(data)
        
        if self.head is None:
            self.head=new_node
            return
        itr=self.head
        while itr.next:
            itr=itr.next    
        itr.next=new_node 

            
    
    def insert_after(self,value,node_val):#value-element to be inserted;node_val=node after which we want to insert
        #first we have to find the node_name
        itr=self.head
        while itr:
            if itr.data==node_val:
                print('Value found.Now inserting\n')
                new_node=node(value)
                new_node.next=itr.next
                itr.next=new_node
                break
            itr=itr.next
        return -1
    def print_LL(self):
        itr=self.head
        while itr:
            print(f'{itr.data}-->',end='')
            itr=itr.next
        
ll=LinkedList()
for i in range(10):
    ll.insert_at_end(i)

print(f'{ll.print_LL()}','\n')

ll.insert_after(100,5)#insert 100 after element with value= 5   

print(f'{ll.print_LL()}','\n')


            



        
        