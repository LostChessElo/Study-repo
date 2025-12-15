# Linked Lists: A Complete Guide

## The Problem with Arrays in Programming

Arrays store data in contiguous memory blocks, which means all elements are placed next to each other in memory. While this provides fast random access, it creates a significant problem: **inserting or deleting elements in the middle requires shifting all subsequent elements**.

For example, inserting an element at position 2 in an array of 1000 elements means moving 998 elements to make space. This operation has $O(n)$ time complexity.

**Linked lists solve this problem** by storing elements in a non-contiguous manner. Instead of requiring a continuous block of memory, linked lists scatter elements throughout memory and connect them using pointers.

---

## Linked List Structure

Linked lists store elements in **nodes**. Each node contains two components:
1. **Data**: The actual value or element
2. **Pointer/Reference**: A link to the next node in the sequence

![Node structure](https://algo.monster/courses/foundation/linked-list-node-structure.svg)

A linked list begins with a **head pointer** that points to the first node. The last node in the list points to `null` (or `None` in Python), which marks the end of the list.

![Linked list structure](https://algo.monster/courses/foundation/linked-list-chain.svg)

---

## Memory Layout: Scattered but Connected

Unlike arrays, linked lists don't require contiguous memory. Nodes can be scattered anywhere in memory, connected only by pointers.

![Memory layout comparison](https://algo.monster/courses/foundation/linked-list-memory-scattered.svg)

This scattered structure makes **insertions and deletions efficient**:

- **Insertion**: Create a new node, set its pointer to the next node, and update the previous node's pointer to point to the new node. No shifting required!
- **Deletion**: Simply update the previous node's pointer to skip over the deleted node. The deleted node becomes unreachable and can be garbage collected.

---

## The Null Terminator

When traversing a linked list, you follow pointers from node to node until you reach a `null` pointer. This null terminator is **critical**—without it, you wouldn't know where the list ends, potentially causing infinite loops or crashes.

> **Golden Rule**: Every linked list must end with a null pointer.

---

## Simple Example of a Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating three nodes
head = Node(1)
second = Node(2)
third = Node(3)

# Linking them together
head.next = second
second.next = third
# third.next is None (null) by default

# This creates: 1 -> 2 -> 3 -> None
```

---

## Arrays vs. Linked Lists: Key Tradeoffs

| Feature | Arrays | Linked Lists |
|---------|--------|--------------|
| **Access Time** | $O(1)$ - Direct indexing | $O(n)$- Must traverse |
| **Insertion/Deletion** | $O(n)$ - Requires shifting | $O(1)$ - Just update pointers* |
| **Memory** | Contiguous block required | Scattered, flexible |
| **Memory Overhead** | None | Extra space for pointers |
| **Best For** | Fast random access | Frequent insertions/deletions |

*$O(1)$ insertion/deletion assumes you already have a reference to the position. Finding the position still takes $O(n)$.

**Key Insight**: Arrays are optimized for **access speed**, while linked lists are optimized for **modification flexibility**.

---

# Nodes and Pointers: The Building Blocks

## Node Structure

Nodes have a simple structure with two fields:
1. **Data field**: Stores the actual value
2. **Next pointer**: Stores a reference to the next node

![Node class diagram](https://algo.monster/courses/foundation/linked-list-node-fields.svg)

In languages like Python, Java, and C#, we implement nodes using classes.

---

## Creating a Single Node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a node with data = 5
node = Node(5)
print(node.data)  # Output: 5
print(node.next)  # Output: None
```

---

## Linking Two Nodes

To link nodes together, you set the first node's `next` pointer to reference the second node:

```python
# Create two nodes
first = Node(10)
second = Node(20)

# Link first to second
first.next = second

# Now: first -> second -> None
print(first.data)       # Output: 10
print(first.next.data)  # Output: 20
print(second.next)      # Output: None
```

---

## Building a Node Chain

You can expand this pattern to create longer chains:

![Node chain](https://algo.monster/courses/foundation/linked-list-building-chain.svg)

```python
# Create nodes
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

# Link them together
head.next = second
second.next = third
third.next = fourth

# Chain: 1 -> 2 -> 3 -> 4 -> None
```

---

## Critical Pointer Management Tips

> **Warning**: Linked list operations revolve around manipulating pointers. Always keep references to nodes before breaking connections, or you'll lose access to parts of your list!

**Example of what NOT to do**:
```python
# BAD: Losing reference to the rest of the list
head = Node(1)
head.next = Node(2)
head = Node(99)  # Lost access to the node with value 2!
```

**Correct approach**:
```python
# GOOD: Keep references when modifying
new_node = Node(99)
new_node.next = head
head = new_node  # Now 99 points to the old head
```

---

## Practice: Building a List from an Array

A common task is converting an array into a linked list. The process involves creating nodes for each array element and linking them sequentially.

![Array to Linked list](https://algo.monster/courses/foundation/linked-list-from-array.svg)

### Implementation

```python
def array_to_linked_list(arr):
    """
    Convert an array to a linked list.
    Returns the head of the linked list.
    """
    if not arr:  # Handle empty array
        return None
    
    # Create the head node
    head = Node(arr[0])
    current = head
    
    # Create and link remaining nodes
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return head

# Example usage
arr = [10, 20, 30, 40]
head = array_to_linked_list(arr)

# Traverse and print the list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Output: 10 -> 20 -> 30 -> 40 -> None
```

### How It Works

1. **Handle edge case**: If the array is empty, return `None`
2. **Create head**: Initialize the first node with `arr[0]`
3. **Use a current pointer**: Keep track of the last node in our growing list
4. **Iterate and link**: For each remaining element, create a new node and link it
5. **Move current forward**: Update `current` to point to the newly added node

---

## Traversing a Linked List

To access or print all elements, you must traverse the list from head to tail:

```python
def print_linked_list(head):
    """Print all elements in a linked list."""
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Usage
head = Node(5)
head.next = Node(10)
head.next.next = Node(15)

print_linked_list(head)
# Output: 5 -> 10 -> 15 -> None
```

**Time Complexity**: $O(n)$ - must visit every node

---

## Summary

- **Linked lists** use nodes with data and pointers to create flexible, non-contiguous data structures
- **Nodes** are scattered in memory, connected by references
- The **null terminator** marks the end of the list and prevents infinite loops
- **Insertions and deletions** are efficient ($O(1)$ with a reference), but **access** requires traversal ($O(n)$)
- Always **preserve references** when manipulating pointers to avoid losing parts of your list
- Common operations include creating lists from arrays, traversing, inserting, and deleting nodes

---

## Next Steps

Now that you understand the basics of linked lists, you're ready to explore:
- Inserting nodes at specific positions
- Deleting nodes by value or position
- Reversing a linked list
- Detecting cycles in linked lists
- Doubly linked lists (nodes with both `next` and `prev` pointers)
