# The Stack and Heap

Programs need memory to store data. Modern computers do this using two main regions:

- **Stack**: A fast, organized region for temporary data following a strict **Last-In-First-Out (LIFO)** rule  
- **Heap**: A flexible region for data that needs to live longer or grow dynamically  

---

![Stack and heap](https://algo.monster/computer-basics/stack-heap-overview.svg)

---

# Stack

Like a stack of plates, you can add to or remove from the top.

When you perform a function call, a new **frame** is added to the top of the stack containing:
- **Function parameters**
- **Local variables**
- **Return address** (where to go back after the function completes)

When a function returns, its frame is removed from the stack.  
This process is extremely fast due to the LIFO rule.

---

### Python Example: Function Calls and the Stack

```python
def main():
    print("Starting")
    a()
    print("Done")

def a():
    x = 10
    b(x)

def b(value):
    y = value * 2
    c(y)

def c(result):
    print(f"Result: {result}")
```

---

![Stack function calls](https://algo.monster/computer-basics/stack-function-calls.svg)

---

### Stack Limitations

- **The stack has a small fixed size (usually a few megabytes)**  
  This is because the stack uses a simple and efficient allocation strategy.
- **Memory management is automatic** — when a function returns, its frame disappears immediately, freeing all memory it used.
- The stack stores **primitive data types** (such as integers and booleans) directly.
- **Objects and arrays are stored as references** on the stack, pointing to data in the heap.

---

## Stack Example – Local Variables

```python
def calculate_sum():
    # These variables live on the stack
    x = 10
    y = 20
    result = x + y
    return result  # Stack frame is cleaned up after return

answer = calculate_sum()
print(answer)  # 30
```

---

# The Heap

When you create objects, arrays, or any data that needs to grow dynamically, it is stored in the **heap**.

- **Slower than stack memory access**
- **More flexible**
- **Better for storing large data structures** that could cause a stack overflow

The heap requires memory management:
- **C/C++**: manual allocation and deallocation
- **Python and Java**: automatic garbage collection

The heap stores dynamically expanding data that needs to **outlive a function call**.

---

![Heap objects](https://algo.monster/computer-basics/heap-objects.svg)

---

# Stack References Point to Heap Objects

When you create an object or array:
- The **actual data** lives in the heap
- A **reference (pointer)** to that data lives on the stack

```python
def create_list():
    # 'numbers' is a reference on the stack
    # The actual list [1, 2, 3, 4, 5] lives on the heap
    numbers = [1, 2, 3, 4, 5]
    return numbers

my_list = create_list()
# The list survives even after create_list() returns
# because it's stored on the heap
print(my_list)  # [1, 2, 3, 4, 5]
```

---

![Stack to heap pointers](https://algo.monster/computer-basics/stack-heap-pointers.svg)

---

## Relevance

- **Understanding the lifecycle of data helps you write more efficient code**
- **The stack is fast** because allocation and deallocation only move a pointer
- **Heap operations are slower** because memory must be searched and managed
- **Memory issues differ between regions**
- **Memory leaks can only occur in the heap**, when objects are allocated but never freed or garbage-collected
- **Stack memory is automatically reclaimed** when a function returns — which is why **stack overflow errors** happen

---

# Stack Overflow Example

```python
def infinite_recursion(n):
    print(f"Call {n}")
    infinite_recursion(n + 1)  # Each call adds a stack frame

# This will eventually cause a RecursionError (stack overflow)
# infinite_recursion(0)
```
