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

# Space Complexity

## What is Space Complexity?
- **Space complexity** is the total amount of memory an algorithm uses relative to its input size.
- It includes:
  - **Input space**: memory required to store the input.
  - **Auxiliary space**: extra (temporary) memory used during execution such as variables, recursion stack, and data structures.
- Like time complexity, space complexity is expressed **asymptotically** using **Big-O notation**.

## Visual Representation
![Space complexity graph](https://cdn.prod.website-files.com/5ef788f07804fb7d78a4127a/61d5fa7ff6021a66bf8d8f4a_space%20complexity-min.jpeg)

> **Note**  
> **Auxiliary space** refers only to temporary memory used by an algorithm, while **space complexity** refers to the **total memory** required for the algorithm to execute fully with input size `n`.

---

## Components of Space Complexity

To estimate memory requirements, we consider two parts:

### 1. Fixed Part
- Independent of input size.
- Includes:
  - Program instructions (code)
  - Constants
  - Scalar variables

### 2. Variable Part
- Dependent on input size.
- Includes:
  - Arrays and dynamic data structures
  - Recursion stack
  - Referenced variables

---

## Example 1: Addition of Two Scalar Variables

### Description
Adding two scalar variables requires memory only to store the result.

### Pseudocode
```cpp
// Algorithm: ADD_SCALAR(A, B)
// Input: Two scalar values A and B
// Output: C = A + B
C ← A + B
return C
```
#### Space Analysis
- Only one extra memory location is required to store the result.
- Space Complexity: $O(1)$ (constant space)
## Example 2: Frequency Counting in an Array
### Pseudocode
```cpp
int freq[n];
int a[n];

for (int i = 0; i < n; i++) {
    cin >> a[i];
    freq[a[i]]++;
}
```
### Full Implementation (C++)
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to count frequencies of array items
void countFreq(int arr[], int n)
{
    unordered_map<int, int> freq;

    for (int i = 0; i < n; i++)
        freq[arr[i]]++;

    for (auto x : freq)
        cout << x.first << " " << x.second << endl;
}

int main()
{
    int arr[] = {10, 20, 20, 10, 10, 20, 5, 20};
    int n = sizeof(arr) / sizeof(arr[0]);

    countFreq(arr, n);
    return 0;
}
```

> Python abstracts memory management, so C++ is used here to clearly demonstrate memory usage.
#### Space Complexity Analysis

- Two arrays of size n are used.
- Loop variable i requires constant space.
#### Final Result

Space Complexity: $O(n)$

### Key Takeaways

- Space complexity measures memory growth, not execution time.
- Auxiliary space is a subset of total space complexity.
- Constants do not affect Big-O notation.
- Recursive algorithms often increase space complexity due to stack usage.