from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    # return [LinkedList()]*size 
    arr = []
    for i in range(size):
      arr.append(LinkedList())
    return arr

  def hash_func(self, key):
    return hash(key) % self.size
    


  # 3️⃣ TODO: Complete the insert method.
  """
  Should insert a key value pair into the hash table, where the key is the word and the value 
  is a counter for the number of times the word appeared. When inserting a new word in the 
  hash table, be sure to check if there is a Node with the same key in the table already.
  """
  def insert(self, key, value):
    # i refers to the hash-index, or which index to look at in self.arr
    i = self.hash_func(key)
    print("this key goes in index ", i)

    # look at the current linked list to see if it already has that key in ther

    if self.arr[i].find(key) == -1:            # not found, append key
      print("not found")
      self.arr[i].append(key, value)   

    else:                                      # found, increase the value by 1
      print("found")
      self.arr[i].edit(key)




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
    counter = 0
    for ll in self.arr:
      # print(counter)
      counter += 1
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


    # words = ""
    # with open('example.txt') as f:
    #   words = f.read()
    # words = words.split()
    # ht = HashTable(8)
    # for word in words:
    #   print(word)
      # ht.insert(word, 1)
