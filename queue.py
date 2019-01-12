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

class Queue(object):

  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def is_empty(self):
    return self.stack1.is_empty and self.stack2.is_empty

  # For an enqueue operation, push into stack 1
  def enqueue(self, item):
    return self.stack1.push(item)

  # For a dequeue operation
  # Check if stack2 is empty
    # If empty, transfer the contents of stack1 to stack2 (pop from stack 1 and push into stack2)
    ## (Since you can't pop from the bottom of a stack, reverse the order of contents in the stack to be able to pop off from the top of the stack)
  def dequeue(self):
    if not stack2.is_empty():
      return self.stack2.pop()
    if stack2.is_empty():
      return self.stack2.push(stack1.pop())

  def size(self):
    return len(self.stack1.size() + len(self.stack2.size()

# def queue(list):
#   print(list)
  
# queue(['a','b','c','d'])