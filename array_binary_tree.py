class array_binary_tree:
    def __init__(self):
        self.tree=[]
    def add_data(self,data):
        self.tree.append(data)
    def delete_data(self,data):
        i=0
        while i in range(len(self.tree)):
            if self.tree[i]==data:
                self.tree[i]=self.tree.pop()
                break
    def print_details(self):
        i=0
        while i in range(len(self.tree)-1):
            if i==0:
                print(f'{self.tree[i]} is the data')
                print('It is root node')
                print(f'{self.tree[(2*i)+1]} is left child')
                print(f'{self.tree[(2*i)+2]} is right child')
            else:
                print(f'{self.tree[i]} is the data')
                print(f'{self.tree[(i-1)//2]} is parent node')
                if (2*i)+1>len(self.tree)-1:
                    print('No left child')
                else:
                    print(f'{self.tree[(2*i)+1]} is left child')
                if (2*i)+2>len(self.tree)-1:
                    print('No right child')
                else:
                    print(f'{self.tree[(2*i)+2]} is right child')
            i+=1
    def print_tree(self):
        for i in self.tree:
            print(i)
arr=array_binary_tree()
arr.add_data(1)
arr.add_data(2)
arr.add_data(3)
arr.add_data(4)
arr.add_data(5)
#arr.print_details()
arr.delete_data(1)
#arr.print_tree()
arr.print_details()
