#Sorting an unsorted array using merge sort
#We will keep on dividing the array untill we reach the single element and thenuse a method that merges two sorted arrays over it




def sort_an_array(array):

    #dividing the array into left and right parts until we reach the last element

    if len(array)<=1:
        return array
    
    #creating right and left arrays using slicing
    mid=len(array)//2
    left_array=array[:mid]
    right_array=array[mid:]

    #the following will recursively slice the array into smaller size until we reach the single element and store it in 
    #   left and right and then call the merge_sort()fn. to merge them
    left=sort_an_array(left_array)
    right=sort_an_array(right_array)
    
    return merge_sorted_array(left,right)#this will eventually merge the single elements


def merge_sorted_array(arr1,arr2):
    sorted_array=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):

        if arr1[i]==arr2[j]:
            sorted_array.append(arr1[i])
            i+=1
            j+=1

        elif arr1[i]<arr2[j]:
            sorted_array.append(arr1[i])
            i+=1
        
        elif arr1[i]>arr2[j]:
            sorted_array.append(arr2[j])
            j+=1

        
    while i<len(arr1):
        sorted_array.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        sorted_array.append(arr2[j])
        j+=1
    return sorted_array

array=[12,32,65,23,45,64,87,54,34]

print(sort_an_array(array))
