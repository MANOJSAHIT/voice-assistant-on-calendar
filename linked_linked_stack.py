class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkstack:
  def __init__(self):
    self.head=None
    self.size=0
  def push(self,data):
    new=node(data)
    if self.size==0:
      self.head=new
      self.size+=1
      return
    new.next=self.head
    self.head=new
    self.size+=1
  def poping(self):
    if self.size==0:
      return
    temp=self.head
    d=temp.data
    self.head=temp.next
    temp=None
    self.size-=1
    return d
  def top(self):
    if self.size==0:
      return
    return self.head.data
  def length(self):
    return self.size
  def empty(self):
    return self.size==0
  def print_stack(self):
    link_string=''
    temp=self.head
    while temp!=None:
      link_string+=str(temp.data)
      temp=temp.next
    return link_string
#Paranthesis Balnce using Stack
paran=linkstack()
s=input('enter the string\n')
cbal=True
for i in s:
  if i in "([{":
    paran.push(i)
  else:
    if paran.empty():
      cbal=False
    else:
      p=paran.poping()
      if p=='(' and i==')':
        cbal=True
      elif p=='[' and i==']':
        cbal=True
      elif p=='{' and i=='}':
        cbal=True
      else:
        cbal=False
        break
if cbal and paran.empty():
  print("balanced")
else:
  print("not balanced")
#Decimaml To Binary Using Stack
inte=int(input('enter the number :'))
conv=linkstack()
c=0
binary=''
while inte!=0:
  conv.push(inte%2)
  inte=int(inte/2)
while not conv.empty():
  binary+=str(conv.poping())
print(binary)
