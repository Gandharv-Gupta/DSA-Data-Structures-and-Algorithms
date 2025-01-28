#Merging 2 sorted arrays

def merge_sorted_arrays(array1,array2):#Array1 and array2 are sorted arrays
    sorted_arr=[]
    i=j=0
    while i< len(array1) and j< len(array2):

        if array1[i]==array2[j]:#if we encounter same element in both lists,then append any of them and increase both of their pointers
            sorted_arr.append(array1[i])
            i+=1
            j+=1        
        if array1[i]<array2[j]:
            sorted_arr.append(array1[i])
            i+=1
        
        elif array1[i]>array2[j]:
            sorted_arr.append(array2[j])
            j+=1

    
    #if any of the arrays is smaller,it elements might get sorted first or vuce versa,hence append the rest as it is 

    #the condition when one array is finished
    while i<len(array1):
        sorted_arr.append(array1[i])#appending the left over elements if any
        i+=1
    while j<len(array2):
        sorted_arr.append(array2[j])#appending the left over elements if any
        j+=1

    print(f'The sorted array is:{sorted_arr}')
    
array1=[1,3,5,7]
array2=[2,4,6,8,9,10]

merge_sorted_arrays(array1,array2)