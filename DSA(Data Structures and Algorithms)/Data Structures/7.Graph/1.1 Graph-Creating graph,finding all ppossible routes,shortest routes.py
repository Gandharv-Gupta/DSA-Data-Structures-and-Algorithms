#Implementing graph

class graph:
    def __init__(self,edges):
        self.edges=edges#edges are a tuple of key values pair
        self.graph_dict={}#a dictionary to store all possible routes from all the nodes

        for start,end in self.edges:#unpacking the tuple:start-first value,end:second value
            if start in self.graph_dict:#if a key already exists
                self.graph_dict[start].append(end)#append the end to its value
            else:
                self.graph_dict[start]=[end]#store the end as a list in the dict if new key is there
        
        print(self.graph_dict)#no key-value pair for TORONTO as it has no destinaiton node

    def find_route(self,start,end,path=[]):#function to find all possible routes between start and end node
        '''
        We go to the start element and then see its values
        If the value contains our destination node,then stop
        Otherwise,recursively make the values of your key-start node to see 
            whether its values contain our destination node
        '''
        path+=[start]
        if start==end:#if start and destination are same
            return [start]
        
        if start not in self.graph_dict:#if start is  not there in the dictionary keys(e.g toronto)
            return []
        paths=[]
        paths.append(start)
        
        for node in self.graph_dict[start]:
            paths += self.find_route(node, end, path)
        return paths

l=[
    ('MUMBAI','PARIS'),
    ('MUMBAI','DUBAI'),
    ('PARIS','NEWYORK'),
    ('PARIS','DUBAI'),
    ('DUBAI','NEWYORK'),
    ('NEWYORK','TORONTO')
]
g=graph(l)

print(g.find_route('MUMBAI','NEWYORK'))

