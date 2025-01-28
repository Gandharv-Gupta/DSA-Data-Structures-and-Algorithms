# Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,
# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# bubble_sort(elements, key='transaction_amount')

def bubble_sort(elements,sort_by):
    
    for i in  range(len(elements)-1):

        for j in range(len(elements)-1-i):

            if sort_by=='transaction_amount':
                if elements[j]['transaction_amount']>elements[j+1]['transaction_amount']:
                    tmp=elements[j]
                    elements[j]=elements[j+1]
                    elements[j+1]=tmp

            if sort_by=='name':
                if elements[j]['name']>elements[j+1]['name']:
                    tmp=elements[j]
                    elements[j]=elements[j+1]
                    elements[j+1]=tmp

            if sort_by=='device':
                if elements[j]['device']>elements[j+1]['device']:
                    tmp=elements[j]
                    elements[j]=elements[j+1]
                    elements[j+1]=tmp            
                    elements[j+1]=tmp            
    
    return elements

l = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(bubble_sort(l,'transaction_amount'),'\n')
print(bubble_sort(l,'name'),'\n')
print(bubble_sort(l,'device'),'\n')
                                     

