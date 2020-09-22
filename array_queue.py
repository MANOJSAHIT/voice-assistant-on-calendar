class arrqueue:
  def __init__(self):
    self.queue=[]
    self.end=-1
  def enqueue(self,dat):
    self.end+=1
    self.queue.append(dat)
  def dequeue(self):
    if self.is_emp():
      return
    self.end-=1
    return self.queue.pop(0)
  def front(self):
    return self.queue[0]
  def rear(self):
    return self.queue[self.end]
  def is_emp(self):
    return self.end==-1
  def get_queue(self):
    return self.queue
