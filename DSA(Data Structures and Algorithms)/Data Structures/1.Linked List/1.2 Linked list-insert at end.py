class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:

    def __init__(self):

        self.head=None# a variable to keep point to the head of our LL;Also it will help us traverse the LL
        #(initially the head is empty)
    def append_at_end(self,data):

        #create an object of class node with the provided data
        new_node=node(data)

        #if head is empty,then make the current element ,our head and then exit the fn.

        if self.head is None:
            self.head=new_node
            return
        
        #if self.head is not none,i.e. alread head exists,
        #then traverse to the last element and append the element to the last

        itr=self.head#starting from the first element we will traverse till last
        while itr.next:#i.e. untill the next element is not none
            itr=itr.next

        #now the itr has the value of last element
        itr.next=new_node

    def print_LL(self):

        itr=self.head

        while itr:#here we didnt use itr.next because ,for the last element,itr.next would be none and wont print the element;hence we only checked if the itr is none or not
            print(f'{itr.data}-->',end='')

            itr=itr.next

#the object of class node will autoatically be created once we create object of class LinkedList

ll=linkedlist()

ll.append_at_end(1)
ll.append_at_end(2)
ll.append_at_end(3)

ll.print_LL()


