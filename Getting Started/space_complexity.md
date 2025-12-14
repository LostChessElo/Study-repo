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