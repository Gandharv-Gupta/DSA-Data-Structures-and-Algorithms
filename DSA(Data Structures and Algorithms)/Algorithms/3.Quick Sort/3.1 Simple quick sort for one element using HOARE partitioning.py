#Simple quick sort using HOARE partitioning
def swap(a,b,arr):#fn. to swap elements a and b in array arr
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp

def quick_sort(elements):
    pivot_element=elements[0]
    pivot_index=0
    start_index=1
    end_index=len(elements)-1

    while start_index<end_index:

        while elements[start_index]<pivot_element and start_index<len(elements):
            start_index+=1
        
        while elements[end_index]>pivot_element and end_index>0:
            end_index-=1
        
        #above both loops exist once we find the elements > pivot and < than pivot

        swap(start_index,end_index,elements)
    
    #once the start_index is > end_index:
    if start_index> end_index and start_index<=len(elements) and end_index>=0:
        swap(pivot_index,end_index,elements)

    print(f"Output: {elements}")
    print('Pivot element 11 in the correct position')
    


l=[11,9,29,7,2,15,28]
print(f'Input:{l}\n')
quick_sort(l)