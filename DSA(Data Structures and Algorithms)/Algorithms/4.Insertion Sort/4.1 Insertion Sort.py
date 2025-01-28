def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp


def insertion_sort(elements):
    
    for i in range(len(elements)):
        j=i-1
        while  elements[i]<elements[j]and j>=0 and i>=0:
            
            swap(i,j,elements)
            #Both i and j keep reducing untill we reach the first element/we reach the element such that elements[i]>elements[j] and then exit the loop
            i-=1
            j-=1
    print(elements)    

l=[11,9,29,7,2,15,28]
insertion_sort(l)



