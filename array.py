class arr:
  def __init__(self,n):
    self.n=n
    self.new_array=[]
  def append_data(self,data):
    self.new_array.append(data)
  def insert_data(self,pos,data):
    self.new_array.insert(pos,data)
  def poping(self,pos):
    self.new_array.pop(pos)
  def remove_data(self,data):
    self.new_array.remove(data)
  def position(self,data):
    return self.new_array.index(data)
  def reverse_list(self):
    self.new_array.reverse()
  def print_array(self):
    print(self.new_array)
