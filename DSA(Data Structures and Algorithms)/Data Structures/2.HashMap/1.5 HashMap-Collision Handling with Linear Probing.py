#implementing collision handling with Linear probing

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

       
        #otherwise:
        itr=0
        while itr<=len(self.arr):#i.e. we will itreate thorugh all the elements in the array and check for a none value
            if itr==len(self.arr):
                itr=0#if we reach the end of array ,then start from the beginning
                            
            if self.arr[h]==None and h<len(self.arr):#using h<len(self.arr) so that index dosent go out of range
                self.arr[h]=value
                break
            h+=1
            itr+=1
    
        
    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(f'{self.arr[i]}',',',end='')


hm=hashmap()

hm.add('gandharv',99)#collision
hm.add('sumita',88)
hm.add('shibanee',78)
hm.add('sahu',81)#collision

hm.print_hashmap()







        