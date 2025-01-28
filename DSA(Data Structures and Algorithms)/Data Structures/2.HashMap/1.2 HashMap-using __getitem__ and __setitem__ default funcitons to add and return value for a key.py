#__getitem___, __setitem__ and __delitem__ function in a hashmap
#both of them allows us to use obj['key']=value and obj['key'] rather than creating an object like obj=hashmap('key','value')

class hashmap:
    def __init__(self):
        self.max=10
        self.arr=[None for i in  range(self.max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)

        return h%self.max
    def __setitem__(self,key,value):#A default function to directly use obj[key]=value
        h=self.get_hash(key)
        self.arr[h]=value
        return
    def __getitem__(self,key):#a default fn. to directly use obj['key] to return its value
        h=self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h=self.get_hash(key)#a default fn. to delete a key value pair just like del obj['key]
        self.arr[h]=None
    
    def print_hashmap(self):
        for i in range(len(self.arr)):
            print(f'{self.arr[i]}',',',end='')


hm=hashmap()
#DONT USE FOLOWING:
# hm.add('Gandharv',99)
# hm.add('sumita',88)
# hm.add('shibanee',78)
# hm.add('sahu',81)

#Now we can directly use:(jsut like a dictionary)Due to __SETITEM__ method
hm['gandharv']=99
hm['sumita']=89
hm['shibanee']=90
hm['sahu']=100

print('Priniting Hah map:')
hm.print_hashmap()

#Now we can directly use:(jsut like a dictionary)Due to __GETITEM__ method
print(f'\nhm[\'sumita\'] is :{hm['sumita']}')

##Now we can directly use:(jsut like a dictionary)Due to __DELITEM__ method
print('\nDeleting a Key-value pair:')
del hm['sumita']
hm.print_hashmap()

#Merely by using __getitem__ , __setitem__and__delitem__ as names of our methods,we can directly use obj['key']or obj['key']=value

#NOTE-A collision is occuring here:
print('\n\nFollowing are collisions of keys gandharv and sahu:')
print(hm.get_hash('sahu'))
print(hm.get_hash('gandharv'))