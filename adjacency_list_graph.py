#Implementing graph data structure using adjacency_list
class Graph:
    def __init__(self):
        self.graph_dictionary={}
    def graph_add_data(self,key,data):
        if key in self.graph_dictionary.keys():
            for i in self.graph_dictionary.keys():
                if i==key:
                    self.graph_dictionary[key].append(data)
                    break
        elif key in self.graph_dictionary.values():
            for i in self.graph_dictionary.values():
                if i==key:
                    self.graph_dictionary[key]=[data]
                    break
        else:
            self.graph_dictionary[key]=[data]
    def print_graph(self):
        for i in self.graph_dictionary.keys():
            for j in self.graph_dictionary[i]:
                print(f'{i}-->{j}')
graph=Graph()
graph.graph_add_data('A',1)
graph.graph_add_data('A',2)
graph.graph_add_data('A',3)
graph.graph_add_data('A',4)
graph.graph_add_data(1,2)
graph.print_graph()
