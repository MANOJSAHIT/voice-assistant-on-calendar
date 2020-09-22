class stack:
  def __init__(self,n):
    self.n=n
    self.array=[]*n
    self.size=0
  def push(self,data):
    if self.size==self.n:
      return 'overflow'
    self.array.append(data)
    self.size+=1
  def poping(self):
    if self.size==0:
      return
    self.size-=1
    return self.array.pop()
  def top(self):
    if self.size==0:
      return
    return self.array[self.size-1]
  def length(self):
    return self.size
  def empty(self):
    return self.size==0
  def print_stack(self):
    return self.array
#String reverse using stack
reverse=stack(10)
s1=input()
stri=''
for i in s1:
  reverse.push(i)
for j in range(len(s1)):
  stri+=reverse.poping()
print(stri)
