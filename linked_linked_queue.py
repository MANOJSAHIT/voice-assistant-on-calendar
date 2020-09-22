class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkqueue:
  def __init__(self):
    self.head=None
    self.end=-1
  def enqueue(self,data):
    new=node(data)
    temp=self.head
    self.end+=1
    if temp==None:
      self.head=new
      return
    while temp.next!=None:
      temp=temp.next
    new.next=temp.next
    temp.next=new
  def dequeue(self):
    temp=self.head
    self.end-=1
    if temp==None:
      return
    d=self.head.data
    self.head=temp.next
    temp=None
    return d
  def front(self):
    return self.head.data
  def rear(self):
    while temp.next!=None:
      temp=temp.next
    return temp.data
  def is_emp(self):
    return self.end==-1
  def get_queue(self):
    temp=self.head
    z1=''
    while temp:
      z1+=str(temp.data)
      temp=temp.next
    return z1
#Stack Implementation Using Queue
class qstack:
  def __init__(self):
    self.q1=linkqueue()
    self.q2=linkqueue()
  def push(self,dat):
    self.q2.enqueue(dat)
    while not self.q1.is_emp():
      self.q2.enqueue(self.q1.dequeue())
    self.q=self.q1
    self.q1=self.q2
    self.q2=self.q
  def poping(self):
    return self.q1.dequeue()
  def print_stack(self):
    print(self.q1.get_queue())
sta=qstack()
sta.push(1)
sta.push(2)
sta.push(3)
sta.push(4)
print(sta.poping())
sta.print_stack()
