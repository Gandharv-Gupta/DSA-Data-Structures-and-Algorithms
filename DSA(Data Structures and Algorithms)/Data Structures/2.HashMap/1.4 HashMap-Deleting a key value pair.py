#deleting an element from hash map

class hashmap:
    def __init__(self):
        self.max=10
        self.arr=[None for i in  range(self.max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.max
    
    def add(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
        return
    
    def delete(self,key):#A fn. to simply delete a value(by assigning its key to none) in hashmap
        h=self.get_hash(key)
        self.arr[h]=None
    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(f'{self.arr[i]}',',',end='')

hm=hashmap()

hm.add('Gandharv',99)
hm.add('sumita',88)
hm.add('shibanee',78)
hm.add('sahu',81)

hm.print_hashmap()

hm.delete('sumita')

print('\nDeleting an element:')
hm.print_hashmap()


