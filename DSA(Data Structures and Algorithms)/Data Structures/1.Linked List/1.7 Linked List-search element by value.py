#Searching an element by value in LL is O(n)

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

    
    def search_element_by_value(self,value):
        #we have to traverse through the LL to find the element ,hence the bigO is O(n)
        itr=self.head
        count=0
        while itr:
            if itr.data==value:
                return count#count will be the index at which element was found
            itr=itr.next
            count+=1
        return -1# if the element was not found

    def print_LL(self):
        itr=self.head
        while itr:
            print(f'{itr.data}-->',end='')
            itr=itr.next
    

ll=LinkedList()
for i in range(10):
    ll.insert_at_end(i)
print(f'{ll.print_LL()}','\n')

print(f'element 7 fount at position:{ll.search_element_by_value(7)}')

        
