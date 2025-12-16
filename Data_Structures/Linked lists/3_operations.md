# Linked List Operations

## Table of Contents
1. [Length of a Linked List](#length-of-a-linked-list)
2. [Print a Linked List](#print-a-linked-list)
3. [Search an Element](#search-an-element-in-a-linked-list)
4. [Insertion Operations](#insertion)
5. [Get Nth Node](#get-nth-node-in-a-linked-list)

---

# Length of a Linked List

Given a singly linked list, the task is to find its length (number of nodes).

**Examples:**

```
Input: LinkedList = 1->3->1->2->1
Output: 5

Input: LinkedList = 2->4->1->9->5->3->6
Output: 7

Input: LinkedList = 10->20->30->40->50->60
Output: 6
```

---

## Iterative Approach

**Algorithm:**
1. Initialize `count` as 0
2. Initialize a node pointer, `curr = head`
3. While `curr` is not NULL:
   - Move `curr` to `curr.next`
   - Increment `count` by 1
4. Return `count`

```python
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def count_nodes(head):
    count = 0
    curr = head
    
    while curr is not None:
        count += 1
        curr = curr.next
    
    return count

# Example usage
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Count of nodes is", count_nodes(head))
# Output: Count of nodes is 5
```

**Complexity:**
- **Time**: $O(n)$ where $n$ is the number of nodes
- **Space**: $O(1)$

---

## Recursive Approach

The idea is to use recursion where `countNodes(node)` calls itself with the next node until reaching the end. Each recursive call returns `1 + count of remaining nodes`.

```python
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def count_nodes(head):
    # Base case
    if head is None:
        return 0
    
    # Count this node plus the rest
    return 1 + count_nodes(head.next)

# Example usage
head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Count of nodes is", count_nodes(head))
# Output: Count of nodes is 5
```

**Complexity:**
- **Time**: $O(n)$ where $n$ is the length of the linked list
- **Space**: $O(n)$ due to recursion call stack

---

# Print a Linked List

Given the head of a singly linked list, print all elements in the list.

## Iterative Approach

```python
class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()

# Example usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)
# Output: 10->20->30->40
```

**Complexity:**
- **Time**: $O(n)$
- **Space**: $O(1)$

---

## Recursive Approach

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
    if node is None:
        print()
        return
    
    print(f"{node.data}", end="")
    if node.next is not None:
        print("->", end="")
    
    printList(node.next)

# Example usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)
# Output: 10->20->30->40
```

**Complexity:**
- **Time**: $O(n)$
- **Space**: $O(n)$ due to recursion call stack

---

# Search an Element in a Linked List

Given the head and a key in a linked list, determine if the key exists within the linked list.

## Iterative Approach

```python
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def search_key(head, key):
    curr = head
    
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    
    return False

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

key = 5
if search_key(head, key):
    print("true")
else:
    print("false")
# Output: true
```

**Complexity:**
- **Time**: $O(n)$
- **Space**: $O(1)$

---

## Recursive Approach

```python
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def searchKey(head, key):
    # Base case
    if head is None:
        return False
    
    # If key found in current node
    if head.data == key:
        return True
    
    # Recur for remaining list
    return searchKey(head.next, key)

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

key = 5
if searchKey(head, key):
    print("true")
else:
    print("false")
# Output: true
```

**Complexity:**
- **Time**: $O(n)$
- **Space**: $O(n)$ due to recursion call stack

---

# Insertion

Insertion involves adding a node to a specific position within the list. There are different types:
- At the front of a linked list (prepend)
- After a given node
- Before a given node
- At a specific position
- At the end of a linked list (append)

---

## Prepend a Linked List

Insert a new node at the beginning of the list.

![Insertion at beginning](https://media.geeksforgeeks.org/wp-content/uploads/20240726182404/Insertion-at-the-Beginning-of-Singly-Linked-List.webp)

**Algorithm:**
1. Create a new node
2. Point the new node's `next` to the current head
3. Update head to point to the new node

**Complexity:**
- **Time**: $O(1)$
- **Space**: $O(1)$

---

## Insertion After a Given Node

Insert a new node after a specified node.

![Insertion after given node](https://media.geeksforgeeks.org/wp-content/uploads/20240726183039/Insert-a-node-after-a-given-node-in-Linked-List.webp)

**Algorithm:**
1. Initialize a pointer `curr` to traverse the list starting from head
2. Loop through the list to find the node with data equal to `key`
3. If not found, return from function
4. Create a new node with the given data
5. Set the new node's `next` pointer to the given node's `next`
6. Update the given node's `next` pointer to point to the new node

**Complexity:**
- **Time**: $O(n)$ for traversal to find the node
- **Space**: $O(1)$

> The process is similar for insertion before a given node, just keep track of the previous node.

---

## Insertion at a Specific Position

Insert a new node at a given position in the list.

![Insertion at specific position](https://media.geeksforgeeks.org/wp-content/uploads/20240726183200/Insertion-at-a-Specific-Position-of-the-Singly-Linked-List-copy.webp)

**Algorithm:**
1. Traverse the linked list up to `position-1` nodes
2. Once at `position-1`, create a new node with the given data
3. Point the new node's `next` to the current node's `next`
4. Point the current node's `next` to the new node

**Complexity:**
- **Time**: $O(n)$ where $n$ is the position
- **Space**: $O(1)$

---

## Append to a Linked List

Insert a new node at the end of the list.

![Append to linked list](https://media.geeksforgeeks.org/wp-content/uploads/20240726183551/Insertion-at-the-End-of-Singly-Linked-List.webp)

**Algorithm:**
1. Create a new node
2. If the list is empty, make the new node the head
3. Otherwise, traverse to the last node
4. Set the last node's `next` pointer to the new node

**Complexity:**
- **Time**: $O(n)$ to traverse to the end
- **Space**: $O(1)$

---

# Get Nth Node in a Linked List

Given a linked list, write a function to get the data at the $k^{th}$ position. If no such node exists, return -1.

![Example](https://media.geeksforgeeks.org/wp-content/uploads/20240822110836/Maximum-of-all-subarrays-of-size-K.webp)

---

## Recursive Approach

```python
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def get_nth_node(head, index):
    if head is None:
        return -1
    
    if index == 1:
        return head.data
    
    return get_nth_node(head.next, index - 1)

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = get_nth_node(head, 3)
print(f"Element at index 3 is {result}")
# Output: Element at index 3 is 3
```

**Complexity:**
- **Time**: $O(n)$ where $n$ is the index
- **Space**: $O(n)$ for recursive call stack

---

## Iterative Approach

```python
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def get_nth_node_iterative(head, n):
    current = head
    count = 1
    
    # Traverse until end or nth node
    while current is not None:
        if count == n:
            return current.data
        count += 1
        current = current.next
    
    # Index out of bounds
    return -1

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

index = 3
result = get_nth_node_iterative(head, index)
if result != -1:
    print(f"Element at index {index} is {result}")
else:
    print(f"Index {index} is out of bounds")
# Output: Element at index 3 is 3
```

**Complexity:**
- **Time**: $O(n)$ where $n$ is the index
- **Space**: $O(1)$

---

## Summary

| Operation | Iterative Time | Iterative Space | Recursive Time | Recursive Space |
|-----------|----------------|-----------------|----------------|-----------------|
| Length | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
| Print | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
| Search | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |
| Insert at beginning | $O(1)$ | $O(1)$ | - | - |
| Insert after node | $O(n)$ | $O(1)$ | - | - |
| Insert at position | $O(n)$ | $O(1)$ | - | - |
| Insert at end | $O(n)$ | $O(1)$ | - | - |
| Get Nth node | $O(n)$ | $O(1)$ | $O(n)$ | $O(n)$ |

---

## Key Takeaways

- **Iterative approaches** generally use $O(1)$ space but require explicit loop control
- **Recursive approaches** are often more elegant but use $O(n)$ space due to the call stack
- **Insertion at the beginning** is the most efficient operation at $O(1)$
- **Most operations** require traversal, resulting in $O(n)$ time complexity
- Always check for edge cases like empty lists or invalid positions.