#Bubble sort

def bubblesort(unsorted_list):
    
    # #way1:
    # for j in range(len(unsorted_list)-1):#len(unsorted-list)-1 because we dont have any number after the last number to compare it with
    #     for i in range(len(unsorted_list)-1):#len(unsorted-list)-1 because we dont have any number after the last number to compare it with
    #         if unsorted_list[i]>unsorted_list[i+1]:
    #             tmp=unsorted_list[i]
    #             unsorted_list[i]=unsorted_list[i+1]
    #             unsorted_list[i+1]=tmp

    # #way2:
    # for j in range(len(unsorted_list)-1):
    #     for i in range(len(unsorted_list)-1-j):#-j as once we run the loop once,the largest element gets sorted and we only need to run this loop for rest of the elements
    #         if unsorted_list[i]>unsorted_list[i+1]:
    #             tmp=unsorted_list[i]
    #             unsorted_list[i]=unsorted_list[i+1]
    #             unsorted_list[i+1]=tmp
        
        #way3:NOTE-The program keeps iterating the whole process even if the list is sorted ,hence rectifying that
    for j in range(len(unsorted_list)-1):
        swapped=False#initializing variable with false;it will become ture even if one swap occurs
        for i in range(len(unsorted_list)-1-j):#-j as once we run the loop once,the largest element gets sorted and we only need to run this loop for rest of the elements
            if unsorted_list[i]>unsorted_list[i+1]:
                tmp=unsorted_list[i]
                unsorted_list[i]=unsorted_list[i+1]
                unsorted_list[i+1]=tmp
                swapped=True#even if one swap occurs,means the list is still unsorted
        if swapped==False:#i.e the list is sorted,now break out of the outer loop
            break
    
            
    
    return unsorted_list
l=[4,3,2,5,6]
print(f'Input list is: {l}')
print('Sorted list is: ',bubblesort([4,3,2,5,6]))