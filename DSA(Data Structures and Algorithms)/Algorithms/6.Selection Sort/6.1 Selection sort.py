#Selection sort
def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp

def selection_sort(elements):
    for i in range(len(elements)):
        
        for j in range(i,len(elements)):#starting from the index =i,we will keep on swapping to get the best candidate for position i
            if elements[j]<elements[i]:
                swap(i,j,elements)


    print(elements)
selection_sort([87,11,32,63,12,45,63])


            