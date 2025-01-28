# Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,
# elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key



def sort_array(array):
    
    
    if len(array)<=1:
        return array
    mid=len(array)//2
    left_array=array[:mid]
    right_array=array[mid:]

    left=sort_array(left_array)
    right=sort_array(right_array)

    return merge_sorted_arr(left[0]['name'],right[1]['name'])        



def merge_sorted_arr(a1,a2):
    i=j=0
    sorted_arr=[]
    while i<len(a1) and j<len(a2):
        if a1[i]==a2[j]:
            sorted_arr.append(a1[i])
            i+=1
            j+=1

        elif a1[i]<a2[j]:
            sorted_arr.append(a1[i])
            i+=1
        
        elif a1[i]>a2[j]:
            sorted_arr.append(a2[j])

    while i<len(a1):
        sorted_arr.append(a1[i])
        i+=1
    while j<len(a2):
        sorted_arr.append(a2[j])
        j+=1

    return sort_array


elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

print(sort_array(elements))