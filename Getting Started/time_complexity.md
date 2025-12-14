# Time Complexity

- **Time complexity** is the computational time an algorithm takes to run.  
- It is commonly estimated by **counting the number of basic operations** performed, assuming each takes constant time.  
- Because execution time can vary based on input, we typically consider the **worst-case time complexity**.  
- Expressed using **Big O notation**, a branch of asymptotic analysis.

---

### Visual Representation
![Time Complexity Graph](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

> **Note:** We are interested in the **rate of growth** with respect to input size.

---

## Common Time Complexities

| Name                  | Complexity        |
|-----------------------|-----------------|
| Constant time         | $O(1)$           |
| Inverse Ackermann time| $O(\alpha(n))$   |
| Iterated log time     | $O(\log^* n)$    |
| Log-logarithmic       | $O(\log \log n)$ |
| Logarithmic           | $O(\log n)$      |
| Linear time           | $O(n)$           |
| Linearithmic time     | $O(n \log n)$    |
| Quadratic time        | $O(n^2)$         |
| Cubic time            | $O(n^3)$         |
| Factorial time        | $O(n!)$          |
| Exponential time      | $O(2^n)$         |

> There are more complexities, but these are the most common.

---

## Understanding Time Complexity: Simple Examples

**Scenario:** Imagine a classroom of 100 students, and you have to find a pen without knowing who has it.

- **$O(n^2)$**: Ask the first student and then ask them about all other 99 students, repeat for each student.  
- **$O(n)$**: Ask each student individually until you find the pen.  
- **$O(\log n)$**: Divide the class into two groups and ask which side has the pen, then repeat the process until only one student remains.

---

### Is execution time the same as time complexity?

- **No.** Time complexity counts **how many times statements are executed**, not actual wall-clock time.  
- On Linux, you can verify actual runtime using the `time` command.

---

## Code Examples

### Constant Time: $O(1)$

```python
print("Hello World")
```

- Prints once → **constant time**.

---

### Linear Time: $O(n)$

```python
n = 8
for i in range(1, n + 1):
    print("Hello World !!!")
```

- Prints **n times** → **linear time**.

---

### Logarithmic Time: $O(\log n)$

```python
n = 8
i = 1
while i <= n:
    print("Hello World !!!")
    i *= 2
```

- `i` doubles each iteration → **logarithmic time**.

---

## How Time Complexity is Computed

### Assumptions:

- Single processor, 32-bit
- Sequential execution
- 1 unit time for arithmetic/logic operations
- 1 unit time for assignment/return

---

### Example 1: Sum of 2 numbers

```python
a = 5
b = 6

def sum(a,b):
  return a+b

print(sum(a,b))
```

- Arithmetic → 1 unit, Return → 1 unit  
- Total: 2 units → $O(1)$ (constant)

---

### Example 2: Sum of elements in a list

```python
def list_sum(A):
    total = 0
    for i in range(len(A)):
        total += A[i]
    return total

A = [5, 6, 1, 2]
print(list_sum(A))
```

- Loop runs **n times** → linear  
- Time complexity: $O(n)$

---

### Time Complexity Calculation (for reference)

```text
T_sum = 1 + 2*(n+1) + 2*n + 1 = 4n + 4 = C1*n + C2 = O(n)
```

---

## Comparing Algorithms

- **Execution times:** Vary by machine → not reliable.  
- **Number of statements:** Vary by language → not ideal.  
- **Ideal:** Use **Big O notation**, comparing growth functions $f(n)$ independent of machine or language.

---

## Summary

- Time complexity measures **how the number of operations grows with input size**, not actual runtime.  
- **Big-O notation** helps us compare algorithms **independently of hardware**.  
- Common complexities range from **$O(1)$** to **$O(2^n)$**.  
- Understanding time complexity helps in **choosing efficient algorithms** for large inputs.

# Other asymptotic notations
## Big Omega $\Omega$ notation
- Describes best-case scenario time complexity
### Visual representation
####
![big omega notation](https://cdn.kastatic.org/ka-perseus-images/c02e6916d15bacae7a936381af8c6e5a0068f4fd.png)
####
## Big Theta $\Theta$ notation
- Describes the average-case scenario time complexity 
### Visual representation
![Big theta notation](https://cdn.kastatic.org/ka-perseus-images/c14a48f24cae3fd563cb3627ee2a74f56c0bcef6.png)
