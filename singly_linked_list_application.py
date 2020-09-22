class node:
  def __init__(self,coef,exponent):
    self.coef=coef
    self.exponent=exponent
    self.next=None
class polynomial:
  def __init__(self):
    self.head=None
  def append_data(self,data,exponent):
    temp=self.head
    new=node(data,exponent)
    if temp==None:
      self.head=new
      return
    while temp.next!=None:
      temp=temp.next
    new.next=temp.next
    temp.next=new
  def print_polynomial(self):
    temp=self.head
    po=''
    while temp.next!=None:
      po+=f'{temp.coef}x^{temp.exponent}+'
      temp=temp.next
    po+=f'{temp.coef}x^{temp.exponent}'
    return po
class add_polynomial:
  def __init__(self):
    self.poly1=polynomial()
    self.poly2=polynomial()
    self.poly3=polynomial()
    self.poly1.append_data(0,5)
    self.poly1.append_data(5,4)
    self.poly1.append_data(2,3)
    self.poly1.append_data(3,2)
    self.poly1.append_data(7,1)
    self.poly2.append_data(9,6)
    self.poly2.append_data(6,4)
    self.poly2.append_data(3,2)
  def process(self):
    temp1=self.poly1.head
    temp2=self.poly2.head
    while temp1 and temp2:
      if temp1.exponent>temp2.exponent:
        self.poly3.append_data(temp1.coef,temp1.exponent)
        temp1=temp1.next
      elif temp1.exponent<temp2.exponent:
        self.poly3.append_data(temp2.coef,temp2.exponent)
        temp2=temp2.next
      else:
        self.poly3.append_data(temp1.coef+temp2.coef,temp1.exponent)
        temp1=temp1.next
        temp2=temp2.next
    print(self.poly3.print_polynomial())
ad=add_polynomial()
ad.process()
