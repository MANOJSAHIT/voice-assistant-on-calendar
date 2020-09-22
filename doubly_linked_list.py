class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class doubly_linked_list:
  def __init__(self):
    self.head=None
  def append_data(self,data):
    temp=self.head
    new=node(data)
    if temp==None:
      self.head=new
      return
    while temp.next!=None:
      temp=temp.next
    new.next=temp.next
    new.prev=temp
    temp.next=new
  def insert_data(self,pos,data):
    temp=self.head
    new=node(data)
    if pos==0:
      new.next=self.head
      new.prev=None
      self.head=new
      return
    for i in range(pos-1):
      temp=temp.next
    tem=temp.next
    new.next=temp.next
    new.prev=temp
    temp.next=new
    tem.prev=new
  def poping(self,pos):
    temp=self.head
    prev=None
    if pos==0:
      tem=temp.next
      tem.prev=None
      temp=None
      self.head=tem
      return
    for i in range(pos):
      prev=temp
      temp=temp.next
    if temp.next!=None:
      tem=temp.next
      tem.prev=temp.prev
      prev.next=temp.next
      temp=None
    else:
      prev.next=None
      temp=None
  def remove_data(self,data):
    temp=self.head
    if temp.data==data:
      tem=temp.next
      tem.prev=None
      temp=None
      self.head=tem
      return
    while temp:
      if temp.data==data:
        break
      else:
        prev=temp
        temp=temp.next
    if temp.next!=None:
      tem=temp.next
      tem.prev=temp.prev
      prev.next=temp.next
      temp=None
    else:
      prev.next=None
      temp=None
  def position(self):
    temp=self.head
    c=0
    while temp:
      c+=1
      temp=temp.next
    return c
  def reverse_list(self):
    temp=self.head
    while temp:
      pre=temp.prev
      temp.prev=temp.next
      temp.next=pre
      temp=temp.prev
    self.head=pre.prev
  def print_list(self):
    temp=self.head
    while temp:
      print(temp.data)
      temp=temp.next
