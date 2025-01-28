-------------ERROR-------------------

#Complete Quick sort algo with HOARE partitioning and RECURSION
def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp


def quick_sort(elements,start_index,end_index):
    pivot_index=start_index#note-initally the start_index and pivot_index are same;later the start index keeps increasing but the pivot remains same

    while start_index<end_index:
         
        while elements[start_index]<=elements[pivot_index] and start_index<len(elements):
            start_index+=1
            
        while elements[end_index]>elements[pivot_index] and end_index>0:
            end_index-=1

        if start_index<end_index:
            swap(start_index,end_index,elements)
    
    
    swap(pivot_index,end_index,elements)

    print(elements)

    
    return end_index#this will be the index where our pivot element has been placed

def call_for_sort(elements,start_index,end_index):
    
    
    if start_index<end_index:
        pi=quick_sort(elements,start_index,end_index)
        quick_sort(elements,start_index,pi-1)
        quick_sort(elements,pi+1,end_index)    

elements=[11,9,29,7,2,15,28]
call_for_sort(elements,0,len(elements)-1)

    