from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    '''Populates self.arr with an array of LinkedLists, has given size'''
    arr = []
    for i in range(size):
      arr.append(LinkedList())
    return arr


  def hash_func(self, key):
    '''pass in key and return hash index'''
    return hash(key) % self.size
    

  def insert(self, key, value):
    '''Ckech if key-value pair exists. If yes, increase value by 1. If no, insert it '''
    i = self.hash_func(key)                   # i refers to the hash-index, or which index to look at in self.arr
    print("this key goes in index ", i)

    # look at the current linked list to see if it already has that key in ther

    if self.arr[i].find(key) == -1:           # not found, append key
      print("not found")
      self.arr[i].append(key, value)   

    else:                                     # found, increase the value by 1
      print("found")
      self.arr[i].edit(key)

    return 


  def print_key_values(self):
    '''prints all nodes in hashTable'''
    for ll in self.arr:
      ll.print_nodes()


if __name__ == "__main__":
    ht = HashTable(8)
    # ht.print_key_values()
    ht.insert("banana", 1)
    print("")
    ht.insert("apple", 1)
    # ht.print_key_values()
    print("")
    ht.insert("apple", 1)
    print("")
    ht.insert("banana", 1)
    print("")
    ht.insert("apple", 1)

    print("\nPrint Nodes:")
    ht.print_key_values()


