#Implementing BInary search using a CLASS and RECURSION
#NOTE-Binary search can only be applied on a SORTED list

class binary_search:
    def __init__(self,sorted_list):
        self.sorted_list=sorted_list
        self.start_index=0
        self.end_index=len(sorted_list)-1
        self.mid_index=(self.start_index+self.end_index)//2

        print(f'Input List:\n{self.sorted_list}')

    def find_num(self,num):

        
        if self.start_index>self.end_index :#as the start index keep increasing and end index keeps decreasing ,we break out once we reach the end of list
            print(f'\n{num} not found\n')#number not found
            return

        if num==self.sorted_list[self.mid_index]:
            print(f'\nElement {num} found at index {self.mid_index} ')
        
        elif num<self.sorted_list[self.mid_index]:
            #start index remains same
            self.end_index=self.mid_index-1
            self.mid_index=(self.start_index+self.end_index)//2
            self.find_num(num)#calling the fn recursively

        elif num>self.sorted_list[self.mid_index]:
            #end index remains same
            self.start_index=self.mid_index+1
            self.mid_index=(self.start_index+self.end_index)//2
            self.find_num(num)#calling the fn recursively


l=[]
for i in range(10):
    l.append(i)

bs=binary_search(l)#we are passing a sorted list here

bs.find_num(5)

bs.find_num(11)
    