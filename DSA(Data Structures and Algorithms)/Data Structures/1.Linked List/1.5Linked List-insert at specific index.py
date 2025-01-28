#Code to insert element at a specific index in the linked list
#Insertion in a LL is O(n)

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
    
    def insert_at_specific_index(self,data,index):#insert'data' at 'index' location
        #either insert at the start,or insert at a given index

        new_node=node(data)

        #inserting at the start/head
        if index==0:
            new_node.next=self.head
            self.head=new_node#making this node,the head node
            
            return
        #inserting at a given index
        count=0
        itr=self.head
        while itr:
            if count==index-1:#accessing the element jsut before the index
                new_node.next=itr.next
                itr.next=new_node
            itr=itr.next

            count+=1
    
    def print_LL(self):
        itr=self.head
        while itr:
            print(f'{itr.data}-->',end='')
            itr=itr.next
        
        
ll=LinkedList()
for i in range(10):
    ll.insert_at_end(i)

print(f'{ll.print_LL()}','\n')

#inserting an element at starting
ll.insert_at_specific_index(100,0)
print(f'{ll.print_LL()}','\n')

#insert at a random index:

ll.insert_at_specific_index(101,5)#isnert 101 at 5th index
print(f'{ll.print_LL()}','\n')

                
        