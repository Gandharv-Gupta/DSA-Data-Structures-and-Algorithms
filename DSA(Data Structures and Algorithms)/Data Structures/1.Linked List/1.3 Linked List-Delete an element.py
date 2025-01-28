class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    
    def __init__(self):#note that the self.head will be initialized none only once,when the object is created and the object will be created only once too(rest all operations we perform using that object)
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

    #Fn to get length of linekd list
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        
        return count

    
    #Fn. to delete element from a specific index
    def delete_from_index(self,index):# we need to provide the index at which we need to delete the element from

        #raise an exception if the index is invalid
        if index<0 or index>self.get_length():
            raise Exception('Invalid value for index')#raises exception if the index is negative or if the index is> length of our LL


        #if trying to delete the head:then,the next element becomes the head element
        if index==0:
            self.head=self.head.next
            return#exit the function

        count=0#in LL ,we have to count the index explicitly,hence using a counter
        itr=self.head#using an iterator to traverse through the linkedlist
        while itr:

            #to delete,stop one element before the actual index,and change its .next element,skipping the middle element
            if count==index-1:#stopping one element before the index
                itr.next=itr.next.next
                break
                
            count+=1#keep increasing counter            

            itr=itr.next
        
        


    def printLL(self):

        itr=self.head

        while itr:
            print(f'{itr.data}-->',end='')
            itr=itr.next

ll=LinkedList()
for i in range(10):
    ll.insert_at_end(i)

print(ll.printLL(),'\n')

ll.delete_from_index(1)#can also input this from user
#NOTE-Deletion is O(n) in linked list
        
ll.printLL()
        
        