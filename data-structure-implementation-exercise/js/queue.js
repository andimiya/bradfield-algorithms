class ArrayQueue {
  /*
   * A queue based on the built in Array type. 
   */
  constructor() {
    this.items = [];
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.shift();
  }

  size() {
    return this.items.length;
  }

  is_empty() {
    return this.size() === 0;
  }
}

class LinkedListNode {
  /*
   * A doubly linked list node, support for the LinkedListQueue. You should not need
   * to change this code, but you will want to use it in the LinkedListQueue
   */
  constructor(value, prevNode, nextNode) {
    this.value = value;
    this.prev = prevNode;
    this.next = nextNode;
  }
}

class LinkedListQueue extends LinkedListNode {
  /*
   * Finish the functions below to create a queue based on a linked list. Because
   * a queue must either:
   *
   * - enqueue to the head and dequeue from the tail; or
   * - enqueue to the tail and dequeue from the head.
   *
   * You should use a doubly linked list to ensure O(1) time enqueue and dequeue.
   */
  constructor(value, prevNode, nextNode) {
    super(value, prevNode, nextNode);

    this.length = 0;
    this.head = null;
    this.tail = null;
    this.currentNode;
  }

  // Add a node to the head
  enqueue(item) {

    const node = new LinkedListNode(item);
    // If there is no head, create a node and make that the head

    if (this.head == null) {
      // If there is no head, there must be no tail, so assign both the head and tail to the newly created node
      this.head = node;
      this.tail = node;
    }
    else {
      // Update head.prev to be the new node
      // Update the next node to the value of the old head
      // Make the new head the new node
      this.head.prevNode = node;
      node.nextNode = this.head;
      this.head = node;
    }
    this.length++;
  };

  // Remove a node from the tail
  dequeue(item) {
    // Hold the value of the current tail
    const prevTail = this.tail;
    // Re-assign the tail to the previous node
    this.tail = this.tail.prevNode;
    // Re-assign the previous node of the previous tail to be null
    prevTail.prevNode = null;

    if (this.tail == null) {
      this.head = null;
    } else {
      // Set the next node to the tail to null
      this.tail.nextNode = null;
    }
    this.length--;
    return prevTail.value;
  }
  size(items) {
    return this.length;
  };

  is_empty() {
    return this.size() === 0;
  }
}

// Quick tests to make sure the object is being built correctly
// let queue = new LinkedListQueue();
// queue.is_empty();
// queue.enqueue(1);
// queue.enqueue(4);
// queue.dequeue() === 1;
// queue.enqueue(3);
// console.log(queue.head.nextNode.value, 'queue')


class RingBufferQueue {
  /*
   * Finish the functions below such that this queue is backed by a Ring Buffer.
   * Recall that a ring buffer uses an array and two pointers to keep track of
   * where to read, and where to write.
   *
   * Be careful! If the read pointer were to overtake the write pointer, it
   * would return incorrect data! If the write pointer were to overtake the read
   * pointer, it would overwrite data that hasn't been read yet!
   *
   * In many contexts, you would avoid this issue by stalling when one pointer
   * would overwrite the other. Since doing so only makes sense in a multithreaded
   * environment, you may prefer to just resize the underlying ring buffer at
   * these times, instead.
   */
  constructor(value, prevNode, nextNode) {
    this.value = value;
    this.prev = prevNode;
    this.next = nextNode;
    this.count = 0;
    this.length = 10;  // Set a static length
    this.head = null;
    this.tail = null;
  }

  enqueue(item) {
    if (this.count == 1) {
      this.length = this.length * 2;
    }
    const node = new LinkedListNode(item);

    if (this.head == null) {
      // If head is null, add the value to the head. Also assign tail to that same value
      this.head = node;
      this.tail = node;
      this.count++;

    }
    else {
      // Traverse until the next empty space is found
      let currentNode = this.head;

      while (currentNode !== null) {
        if (!currentNode.nextNode) {
          const node = new LinkedListNode(item);
          currentNode.nextNode = node;
          this.count++;
          return;
        }
        else {
          // If there are no empty slots, then double the length of the object
          this.length = this.length * 2;
        }
      }
    }
  };

  dequeue(item) {
    if (this.count == 1) {
      this.length = this.length * 2;
    }
    // Hold the value of the current tail
    const prevTail = this.tail;
    // Re-assign the tail to the previous node
    this.tail = this.tail.prevNode;
    // Re-assign the previous node of the previous tail to be null
    prevTail.prevNode = null;

    if (this.tail == null) {
      this.head = null;
    } else {
      // Set the next node to the tail to null
      this.tail.nextNode = null;
    }
    this.count--;
    return prevTail.value;
  }

  size(items) {
    return this.length;
  };

  is_empty() {
    return this.count === 0;
  }
}

// let queue = new RingBufferQueue();
// queue.is_empty();
// queue.enqueue(1);
// queue.enqueue(2);

// queue.dequeue() === 1;

// console.log(queue, 'queue 2');
// console.log(queue.length, 'length');
// console.log(queue.count, 'count');
// // console.log(queue, 'queue 1');
// // queue.enqueue(3);

module.exports = {
  QUEUE_CLASSES: [RingBufferQueue],

  // Add additional entries to QUEUE_CLASSES as you fill in the implementations:
  // QUEUE_CLASSES: [ArrayQueue, LinkedListQueue, RingBufferQueue],
};
