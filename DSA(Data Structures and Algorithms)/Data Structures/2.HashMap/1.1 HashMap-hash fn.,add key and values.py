#creating a hash table/hash map
class hashmap:
    def __init__(self):
        self.max=10#everytime an object is created ,and array of size 10(initial memory allocated)will be created with all none elements
        self.arr=[None for i in range(self.max)]#creating a list with all none elements,of size 100
    
    def get_hash(self,key):#fn. takes key as i/p and returns a hash value/index at which we will insert the element
        h=0
        for i in key:#i will go through all the characters in the string
            h+=ord(i)
        return h%self.max#returns mod of h when divided by size of array
    
    def add(self,key,value):#fn. to get the  hash value of a key and insert its value at the given index      
        h=self.get_hash(key)#getting the index,where element will be inserted
        self.arr[h]=value#isnerting element at deduced index in the 'arr' array

    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(self.arr[i],',',end='')


hm=hashmap()
hm.add('Gandharv',99)
hm.add('sumita',88)
hm.add('shibanee',78)
hm.add('sahu',81)

hm.print_hashmap()