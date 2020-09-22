class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class circular_linked_list:
  def __init__(self):
    self.head=None
  def append_data(self,data):
    temp=self.head
    new=node(data)
    if temp==None:
      self.head=new
      new.next=self.head
      return
    while temp.next!=self.head:
      temp=temp.next
    temp.next=new
    new.next=self.head
  def insert_data(self,pos,data):
    temp=self.head
    new=node(data)
    if pos==0:
      new.next=temp
      while temp.next!=self.head:
        temp=temp.next
      self.head=new
      temp.next=new
      return
    for i in range(pos-1):
      temp=temp.next
    if temp.next!=self.head:
      new.next=temp.next
      temp.next=new
    else:
      temp.next=new
      new.next=self.head
  def poping(self,pos):
    temp=self.head
    tem=self.head
    if pos==0:
      while temp.next!=self.head:
        temp=temp.next
      self.head=tem.next
      temp.next=self.head
      tem=None
      return
    for i in range(pos):
      prev=temp
      temp=temp.next
    if temp.next!=self.head:
      prev.next=temp.next
      temp=None
    else:
      prev.next=self.head
      temp=None
  def remove_data(self,data):
    temp=self.head
    tem=self.head
    if temp.data==data:
      while temp.next!=self.head:
        temp=temp.next
      self.head=tem.next
      temp.next=self.head
      tem=None
      return
    while temp:
      if temp.data==data:
        break
      else:
        prev=temp
        temp=temp.next
    if temp.next!=self.head:
      prev.next=temp.next
      temp=None
    else:
      prev.next=self.head
      temp=None
  def position(self,data):
    temp=self.head
    pos=0
    while temp.next!=self.head:
      if temp.data==data:
        break
      else:
        pos+=1
        temp=temp.next
    return pos
  def print_list(self):
    temp=self.head
    while temp.next!=self.head:
      print(temp.data)
      temp=temp.next
    print(temp.data)
