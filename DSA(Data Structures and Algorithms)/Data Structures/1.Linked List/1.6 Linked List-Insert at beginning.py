#inserting at beginning:

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return

        #if self.head is not none:

        new_node.next=self.head#current head becomes the next element
        self.head=new_node#current inserted node becomes the head
    
    def print_LL(self):
        itr=self.head

        while itr:
            print(f'{itr.data}-->',end='')
            itr=itr.next

ll=LinkedList()
for i in range(10):
    ll.insert_at_beginning(i)

print(f'{ll.print_LL()}','\n')

        