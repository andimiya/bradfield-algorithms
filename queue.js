// ## Stack from the /algos page
class Stack {

  constructor(self) {
    this.self = self;
  }

  __init__(self) {
    this._items = []
  }

  is_empty(self) {
    return !this._items
  }

  push(self, item) {
    this.append(item)
  }

  pop(self) {
    return this._items.pop()
  }

  peek(self) {
    return self._items[-1]
  }

  size(self) {
    return len(self._items)
  }
}

class Queue {

  __init__(self) {
    self.stack1 = new Stack()
    self.stack2 = new Stack()
  }

  is_empty(self) {
    return self.stack1.is_empty && self.stack2.is_empty
  }

  // # For an enqueue operation, push into stack 1
  enqueue(self, item) {
    return self.stack1.push(item)
  }
  // # For a dequeue operation
  // # Check if stack2 is empty
  // # If empty, transfer the contents of stack1 to stack2(pop from stack 1 and push into stack2)
  // ## (Since you can't pop from the bottom of a stack, reverse the order of contents in the stack to be able to pop off from the top of the stack)
  dequeue(self) {
    if (stack2.is_empty() == false) {
      return self.stack2.pop()
    }
    else if (self.stack2.is_empty() == true) {
      self.stack2.push(self.stack1.pop())
      return self.stack2.pop()
    }
  }
  size(self) {
    return len(self.stack1.size()) + len(self.stack2.size())
  }
}

// let queue = new Queue(['a', 'b', 'c', 'd']);
// queue.dequeue();

let stack = new Stack(['a', 'b', 'c', 'd']);
console.log(stack.push());