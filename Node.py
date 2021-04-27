class Node:

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
  
  def increase_val(self):
    self.value += 1
