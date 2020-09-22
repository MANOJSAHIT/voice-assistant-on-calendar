class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class singly_linked_list:
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
    temp.next=new
  def insert_data(self,pos,data):
    temp=self.head
    new=node(data)
    if pos==0:
      new.next=self.head
      self.head=new
      return
    for i in range(pos-1):
      temp=temp.next
    new.next=temp.next
    temp.next=new
  def poping(self,pos):
    temp=self.head
    if pos==0:
      self.head=temp.next
      temp=None
      return
    for i in range(pos):
      prev=temp
      temp=temp.next
    prev.next=temp.next
    temp=None
  def remove_data(self,data):
    temp=self.head
    if temp.data==data:
      self.head=temp.next
      temp=None
      return
    while temp:
      if temp.data==data:
        prev.next=temp.next
        temp=None
      else:
        prev=temp
        temp=temp.next
  def position(self,data):
    temp=self.head
    c=0
    while temp:
      if temp.data==data:
        break
      else:
        c+=1
        temp=temp.next
    return c
  def reverse_list(self):
    temp=self.head
    prev=None
    while temp:
      tem=temp
      temp=temp.next
      tem.next=prev
      prev=tem
    self.head=prev
  def print_list(self):
    list_string=''
    temp=self.head
    while temp:
      list_string+=str(temp.data)
      temp=temp.next
    return list_string
