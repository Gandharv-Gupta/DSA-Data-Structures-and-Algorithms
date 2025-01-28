#to return a value for the given key in hashmap

class hashmap:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)    
        
        return h%self.max   
    
    def add(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value


    #fn. to return value for a given key
    def value_for_key(self,key):
        h=self.get_hash(key)#finding the index/hash no. for given key
        return self.arr[h]#returning value for the given key
    
    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(self.arr[i],',',end='')

hm=hashmap()
hm.add('gandharv',99)
hm.add('sumita',88)
hm.add('shibanee',78)
hm.add('sahu',81)
#NOTE-The above values are not inserted sequentially in self.arr array;just like dictionary ,its randomly arranged in that allocated memory space(although  contiguous)

hm.print_hashmap()
print(f'\nThe value for key \'sahu\' is: {hm.value_for_key('sahu')}')