# Types of Linked Lists: A Complete Guide

## Table of Contents
1. [Singly Linked Lists](#singly-linked-lists)
2. [Doubly Linked Lists](#doubly-linked-lists)
3. [Circular Linked Lists](#circular-linked-lists)
4. [Comparison Summary](#comparison-summary)

---

# Singly Linked Lists

A **singly linked list** consists of nodes where each node contains data and a single pointer to the next node. The last node has a null pointer, marking the end of the list.

![Singly linked list example](https://media.geeksforgeeks.org/wp-content/uploads/20250901170546665785/link1.webp)

This structure allows us to form dynamically linked data in a chain-like sequence, where traversal is possible in only **one direction** (forward).

## Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data    # Data part of the node
        self.next = None    # Pointer to the next node
```

---

## Creating a Singly Linked List

```python
# Create the first node (head of the list)
head = Node(10)

# Link the second node
head.next = Node(20)

# Link the third node
head.next.next = Node(30)

# Printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next

# Output: 10 20 30
```

---

## Advantages and Disadvantages

| **Advantages** | **Disadvantages** |
|----------------|-------------------|
| Dynamic size - grows and shrinks as needed | No backward traversal possible |
| Efficient insertion/deletion at beginning $O(1)$ | Sequential access only - no random access |
| No memory waste from pre-allocation | Extra memory for storing pointers |
| Easy to implement | Traversal from head every time $O(n)$ for access |
| No need to shift elements during insertion/deletion | Cannot traverse backward to previous nodes |

### Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Access | $O(n)$ |
| Search | $O(n)$ |
| Insertion (at beginning) | $O(1)$ |
| Insertion (at end) | $O(n)$ |
| Deletion (at beginning) | $O(1)$ |
| Deletion (given node) | $O(n)$ |

---

# Doubly Linked Lists

A **doubly linked list** offers the ability to traverse the list in both directions (forward and backward). This is because each node contains a pointer to both the previous and next node.

![Example of doubly linked list](https://media.geeksforgeeks.org/wp-content/uploads/20250827100441798494/11.webp)

---

## Node Structure

Nodes in a doubly linked list have **3 fields**:
1. A pointer to the **previous node** (`prev`)
2. The **data** it stores
3. A pointer to the **next node** (`next`)

![Doubly node structure](image.png)

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None  # Pointer to previous node
        self.next = None  # Pointer to next node
```

---

## Creating a Doubly Linked List

```python
# Create the first node (head of the list)
head = Node(10)

# Create and link the second node
head.next = Node(20)
head.next.prev = head

# Create and link the third node
head.next.next = Node(30)
head.next.next.prev = head.next

# Traverse forward
temp = head
while temp is not None:
    print(temp.data, end="")
    if temp.next is not None:
        print(" <-> ", end="")
    temp = temp.next

# Output: 10 <-> 20 <-> 30
```

---

## Advantages and Disadvantages

| **Advantages** | **Disadvantages** |
|----------------|-------------------|
| Bidirectional traversal (forward and backward) | More memory required (extra prev pointer) |
| Efficient deletion when node reference is given $O(1)$ | More complex implementation |
| Can traverse from any node in both directions | Extra operations to maintain prev pointers |
| Easier to implement certain algorithms (like reversing) | More pointer manipulation increases bug risk |
| No need to maintain previous node during deletion | Slightly slower due to extra pointer updates |

### Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| Access | $O(n)$ |
| Search | $O(n)$ |
| Insertion (at beginning) | $O(1)$ |
| Insertion (at end) | $O(n)$ or $O(1)$ with tail pointer |
| Deletion (given node) | $O(1)$ |
| Deletion (by value) | $O(n)$ |

---

## Key Insight

> Each node in a doubly linked list contains the data it holds, a pointer to the next node in the list, and a pointer to the previous node in the list. By linking these nodes together through the next and prev pointers, we can traverse the list in both directions (forward and backward), which is a key feature of a doubly linked list.

---

# Circular Linked Lists

A **circular linked list** is a data structure where the last node points back to the first node, forming a closed loop. Circular linked lists can be created from both singly and doubly linked lists.

---

## Circular Singly Linked List

![Circular singly linked list example](https://media.geeksforgeeks.org/wp-content/uploads/20250829125719598746/25.webp)

In a circular singly linked list:
- The list moves in **one direction** only
- Each node contains data and a `next` pointer
- The last node's `next` pointer points back to the **first node** (head)
- This forms a circular structure with no null terminator

### Basic Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a circular singly linked list
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head  # Points back to head

# Traversing (must use a condition to avoid infinite loop)
current = head
count = 0
max_iterations = 10

while count < max_iterations:
    print(current.data, end=" -> ")
    current = current.next
    count += 1
    if current == head:
        print(f"(back to {head.data})")
        break
```

### Advantages and Disadvantages

| **Advantages** | **Disadvantages** |
|----------------|-------------------|
| Can traverse the entire list starting from any node | More complex implementation (no clear end point) |
| Useful for round-robin scheduling | Risk of infinite loops if not handled carefully |
| No null pointers to check | Cannot traverse backward |
| Efficient for applications requiring circular traversal | Slightly more complex pointer manipulation |
| Easy to reach any node from any other node | Finding the last node requires $O(n)$ traversal |

---

## Circular Doubly Linked List

![Circular doubly linked list example](https://media.geeksforgeeks.org/wp-content/uploads/20250829125747698901/26.webp)

In a circular doubly linked list:
- Each node contains a pointer to both the **previous** and **next** node, along with the data
- The last node's `next` pointer points back to the first node
- The first node's `prev` pointer points to the last node
- Allows for traversal in **two directions** (forward and backward) in a circular manner

### Basic Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Creating a circular doubly linked list
head = Node(10)
second = Node(20)
third = Node(30)

# Forward links
head.next = second
second.next = third
third.next = head

# Backward links
head.prev = third
second.prev = head
third.prev = second

# Traversing forward
current = head
for i in range(3):
    print(current.data, end=" <-> ")
    current = current.next
print(f"(back to {head.data})")

# Output: 10 <-> 20 <-> 30 <-> (back to 10)
```

### Advantages and Disadvantages

| **Advantages** | **Disadvantages** |
|----------------|-------------------|
| Bidirectional circular traversal | Most complex implementation of all linked list types |
| Can move forward or backward from any node | Highest memory overhead (two pointers + circular) |
| Efficient for complex navigation patterns | More pointer maintenance increases bug risk |
| Fast access to both previous and next nodes | Slower operations due to more pointer updates |
| Useful for browser history, music playlists, etc. | Risk of infinite loops in both directions |

---

## Use Cases for Circular Linked Lists

**Circular Singly Linked Lists:**
- Round-robin scheduling in operating systems
- Multiplayer games (turn rotation)
- Music player playlists (repeat mode)
- Managing buffers in circular queue implementations

**Circular Doubly Linked Lists:**
- Browser navigation (forward/back with wrap-around)
- Image viewer galleries (with looping)
- Undo/redo functionality with circular history
- Advanced navigation systems requiring bidirectional circular movement

---

# Comparison Summary

## Visual Comparison

| Feature | Singly | Doubly | Circular Singly | Circular Doubly |
|---------|--------|--------|-----------------|-----------------|
| **Traversal** | Forward only | Forward & Backward | Circular forward | Circular both ways |
| **Memory per node** | 1 pointer | 2 pointers | 1 pointer | 2 pointers |
| **Last node points to** | NULL | NULL | Head | Head |
| **First node prev** | N/A | NULL | N/A | Last node |
| **Implementation complexity** | Simple | Moderate | Moderate | Complex |
| **Best use case** | Simple forward traversal | Frequent bidirectional access | Circular processes | Complex circular navigation |

---

## When to Use Each Type

### Use Singly Linked List When:
- You only need forward traversal
- Memory is a concern
- Implementation simplicity is important
- You're building stacks or simple queues

### Use Doubly Linked List When:
- You need bidirectional traversal
- You frequently delete nodes (easier with prev pointer)
- You're implementing deques or LRU caches
- You need to navigate backward efficiently

### Use Circular Singly Linked List When:
- You need to repeatedly cycle through elements
- You're implementing round-robin algorithms
- You want to reach any node from any starting point
- NULL checks are unwanted overhead

### Use Circular Doubly Linked List When:
- You need circular navigation in both directions
- You're building advanced navigation systems
- You need the most flexible traversal options
- Memory overhead is acceptable for feature richness

---

## Space Complexity Comparison

For a list with **n** nodes:

| Type | Space Complexity | Extra Space per Node |
|------|------------------|----------------------|
| Singly Linked List | $O(n)$ | 1 pointer (4-8 bytes) |
| Doubly Linked List | $O(n)$ | 2 pointers (8-16 bytes) |
| Circular Singly | $O(n)$ | 1 pointer (4-8 bytes) |
| Circular Doubly | $O(n)$ | 2 pointers (8-16 bytes) |

---

## Final Thoughts

Each type of linked list has its own strengths and trade-offs. The choice depends on your specific requirements:

- **Memory efficiency** → Singly Linked List
- **Bidirectional flexibility** → Doubly Linked List  
- **Circular operations** → Circular Variants
- **Maximum flexibility** → Circular Doubly Linked List

Understanding these data structures deeply will help you make informed decisions when designing algorithms and systems.