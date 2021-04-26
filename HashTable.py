from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    return [LinkedList()]*size    

  def hash_func(self, key):
    return hash(key) % self.size
    


  # 3️⃣ TODO: Complete the insert method.
  """
  Should insert a key value pair into the hash table, where the key is the word and the value 
  is a counter for the number of times the word appeared. When inserting a new word in the 
  hash table, be sure to check if there is a Node with the same key in the table already.
  """
  def insert(self, key, value):
    # get hash value of key, then modulate it to get index. then set i (index) to it
    i = self.hash_func(key)
    print("this key goes in index ", i)


    # look at the current linked list to see if it already has that key in ther
    data = [key, value]
    
    if self.arr[i].find(data) == -1: # not found, append key
      print("not found")
      self.arr[i].append(data)   
      print('key:', self.arr[i].head.data[0])
      print('value:', self.arr[i].head.data[1])  

    else:                       # found, increase the value by 1

      # store the value currently in this position
      # then delete node <--- need a helper function??
      # then create a node with (key, value) + new value stored
      # then append data
      print("found")
      self.arr[i].head.data[1] += 1  
      print('key:', self.arr[i].head.data[0])
      print('value:', self.arr[i].head.data[1]) 

    print(self.arr[i].head)
    # print(self.arr)
    return 
    




  # 4️⃣ TODO: Complete the print_key_values method.
  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    for LinkedList in self.arr:
      LinkedList.print_nodes()

if __name__ == "__main__":
    ht = HashTable(8)
    # print(ht.hash_func("key"))
    ht.insert("banana", 1)
    print("")
    ht.insert("apple", 1)
    print("")
    ht.insert("apple", 1)
    print("")
    ht.insert("banana", 1)
    print("")
    ht.insert("apple", 1)


    # words = ""
    # with open('example.txt') as f:
    #   words = f.read()
    # words = words.split()
    # for word in words:
    #   print(word)
    #   # ht.insert(word, 1)
