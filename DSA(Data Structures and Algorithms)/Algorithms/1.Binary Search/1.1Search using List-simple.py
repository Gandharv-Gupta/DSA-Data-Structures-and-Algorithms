#Normal search using LIST

def find_num(l,val):
    for index,num in enumerate(l):
        if val==num:
            print(f'{val} found at index {index}')
            return

l=[]
for i in range(10):
    l.append(i)
find_num(l,9)