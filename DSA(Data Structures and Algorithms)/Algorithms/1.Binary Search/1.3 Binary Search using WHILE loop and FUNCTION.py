
#Implementing BInary search using a FUNCTION and WHILE LOOP(The same binary search can be implemented without class and recursion)

def binary_search(l,num):#l=list,num-number to be found
    start_index=0
    end_index=len(l)-1
    mid_index=(start_index+end_index)//2

    while start_index<=end_index:#NOTE- start_index less than and 'equal to' end_index

        if num==l[mid_index]:
            return mid_index
        
        
        elif num<l[mid_index]:
            #start index remains same
            end_index=mid_index-1
            mid_index=(start_index+end_index)//2


        
        elif num>l[mid_index]:
            #end index remains same
            start_index=mid_index+1
            mid_index=(start_index+end_index)//2

    return -1#NOTE-This will be executed only if the above while loop fails
     
l=[]
for i in range(10):
    l.append(i)

print(f'Number 6 found at index :{binary_search(l,6)}')#we are passing a sorted list here

print(binary_search(l,11))

        



