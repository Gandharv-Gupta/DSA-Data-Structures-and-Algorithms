class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:

    def __init__(self):

        self.head=None
        
    def append_at_end(self,data):
      
        new_node=node(data)
      

        if self.head is None:
            self.head=new_node
            return
        
 
        itr=self.head
        while itr.next:
            itr=itr.next
      
        itr.next=new_node

    def print_LL(self):

        itr=self.head

        while itr:
            print(f'{itr.data}-->',end='')

            itr=itr.next

    def length_of_ll(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count


ll=linkedlist()

ll.append_at_end(1)
ll.append_at_end(2)
ll.append_at_end(3)

print(ll.print_LL(),'\n')

print(f'The length of linked list is:{ll.length_of_ll()}')
