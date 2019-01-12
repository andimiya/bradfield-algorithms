## Note: If I put the reverseThisList function before the class on this page, it doesn't recognize the Stack class. Not sure why this would happen as the function should call the class no matter where the function is placed on this page.

# def reverseThisList(list):

#   s = Stack()
#   print(s)

#   for item in list:
#     s.push(item)
#   reversedList = []
#   while not s.is_empty():
#     print(reversedList)
#     reversedList.append(s.pop())
#   print(reversedList)
#   return reversedList

# reverseThisList(['one', 'two', 'three', 'four'])

## Stack from the /algos page
class Stack(object):

  def __init__(self):
      self._items = []

  def is_empty(self):
      return not bool(self._items)

  def push(self, item):
      self._items.append(item)

  def pop(self):
      return self._items.pop()

  def peek(self):
      return self._items[-1]

  def size(self):
      return len(self._items)

def reverseThisList(list):

  s = Stack()
  print(s)

  for item in list:
    s.push(item)
  reversedList = []
  while not s.is_empty():
    reversedList.append(s.pop())
  print(reversedList)
  return reversedList

reverseThisList(['one', 'two', 'three', 'four'])