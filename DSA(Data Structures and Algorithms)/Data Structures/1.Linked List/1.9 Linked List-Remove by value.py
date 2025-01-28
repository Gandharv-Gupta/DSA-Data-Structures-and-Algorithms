#code to remove_y_value in linked list

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

    def remove_by_value(self,value):#we first need to traverse through the LL to find the value and then repalce previouselement.next=nextelement
        #first find the index of the value:
        itr=self.head
        count=0
        while itr:
            if itr.data==value:
                break
            count+=1
            itr=itr.next
        #count is the index of our element
        #running another while loop to remove element:
        index=0
        itr2=self.head
        while itr2.next:
            if index==count-1:
                print('Element Found.Removed the Element:')
                itr2.next=itr2.next.next
                return
            
            index+=1
            itr2=itr2.next
    

    
    def print_LL(self):
        itr=self.head
        while itr:
            print(f'{itr.data}-->',end='')
        
            itr=itr.next


ll=LinkedList()
for i in range(10):
    ll.insert_at_end(i)

print(f'{ll.print_LL()}','\n')

ll.remove_by_value(5)#remove element with value=5
print(f'{ll.print_LL()}','\n')        