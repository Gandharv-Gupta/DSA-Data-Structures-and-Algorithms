#Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
# print out the median of the list so far on each new element.

#NOTE-A list having even number of elements-the median is mean of middle numbers(for odd no. of elements ,its the middle element after sorting)

def swap(a,b,arr):
    tmp=arr[a]
    arr[a]=arr[b]
    arr[b]=tmp

def find_median(elements):
    if len(elements)==1:
        median=elements[0]
        print(f'The median of only single element is {median}')
        return

    if len(elements)%2==0:
        #i.e even number of elements
        mid_index=len(elements)//2
        median=(elements[mid_index]+elements[mid_index-1])/2
        print(f'The median(Even no. of elements) now is {median}')

    else:
        mid_index=len(elements)//2
        median=elements[mid_index]
        print(f'The median(Odd no. of elements) now is {median}')


def insertion_sort(val):

    elements.append(val)

    for i in range(len(elements)):
        j=i-1

        while elements[i]<elements[j] and j>=0 and i>=0:
            swap(i,j,elements)
            i-=1
            j-=1
    print(f'The elements are:{elements}')
        
    find_median(elements)
        

    


def input_stream():
    print('Enter 5 numbers one by one:\n')

    for i in range(5):
        val=int(input('\nEnter the next Number:'))
        insertion_sort(val)

elements=[]
input_stream()





