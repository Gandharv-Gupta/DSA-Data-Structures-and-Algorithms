#poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
#You have to read this file in python and print every word and its count as show below.
#Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

path=r"C:\Users\HP\Downloads\poem.txt"

with open(path,'r') as file:
    content=file.read()#read the content as string

print(content)

list_of_content=content.split()#splitting the content based on spaces



#getting all the uniques:

set_of_content=set(list_of_content)


list_from_set=list(set_of_content)
size=len(list_from_set)

#finding occurances:
dict={}
for j in range(len(list_from_set)):
    count=0
    for i in range(len(list_of_content)):
        if list_from_set[j]==list_of_content[i]:
            count+=1
            dict[list_from_set[j]]=count

print(dict)
keys=[]
values=[]
class hashsmap:
    def __init__(self,size):
        self.max=size
        self.arr=[None for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.max
    def get_keys(self,dic):
        
        for i in dic.keys():
            keys.append(i)
    
    def get_values(self,dic):
        for i in dic.values():
            values.append(i)
        for p in keys:
            for j in values:
                self.set_item(p,j)

    def set_item(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value
    
    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(f'{self.arr[i]}',',',end='')

hm=hashsmap(size)
hm.get_keys(dict)
hm.get_values(dict)


hm.print_hashmap()

