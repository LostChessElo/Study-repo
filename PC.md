# Central Processing Unit (CPU)

## Three main working parts:

###
![full CPU diagram](https://www.learncomputerscienceonline.com/wp-content/uploads/2019/05/Microprocessor.jpg)
###
### Control Unit
Fetches instructions and determines the meaning behind them.
### Arithmetic Logic Unit (ALU)
- **Addition**: Electrical circuits flip bits on and off using logic gates.
- **Comparisons**: Values are compared by subtracting them to check whether the result is negative.

### Registers
Tiny storage locations that hold numbers while they are being processed.

#### Example
**5 + 3** → each number is placed in a register → the ALU performs the addition through its circuits → **8** → the result is stored in another register.

A modern processor running at **3 GHz** can perform **3 billion operations per second**.

**Limitation**: The CPU needs instructions and data to be readily available in memory.

![CPU Diagram](https://algo.monster/courses/foundation/cpu-how-it-works.svg)

---

# Random Access Memory (RAM)

### The computer’s workspace

#### Program execution flow
Run program → OS loads data from disk/SSD → RAM → CPU fetches instructions and data from RAM billions of times per second.

RAM is fast but **temporary**. It loses all data when power is removed.

![RAM Diagram](https://algo.monster/courses/foundation/ram-how-it-works.svg)

---

# Storage (Disk / SSD / HDD)

### Permanent data storage

Two main types:
- **Hard Disk Drives (HDD)**
- **Solid State Drives (SSD)**

### HDD
Uses spinning magnetic platters. A magnetic arm moves across the disk to read and write data.  
Cheaper and offers larger capacity, but mechanical movement results in slower read and write speeds.

![HDD Diagram](https://algo.monster/courses/foundation/storage-hdd.svg)

---

### SSD
Uses NAND flash memory chips (similar to RAM but with different technology).  
Much faster read and write speeds due to the lack of mechanical movement.

![SSD Diagram](https://algo.monster/courses/foundation/storage-ssd.svg)

---

Both disk types are **slower than RAM**.

#### Program loading
When you double-click a program icon, the OS loads the program from storage → RAM → CPU can then execute it.

#### Saving data
When you save a file, data is removed from RAM and written back to permanent storage.

---

# How They Work Together

## Example: Running a Python program

OS finds Python scripts → loads the Python interpreter into RAM → the interpreter reads the scripts (also in RAM) and begins execution → CPU fetches instructions from RAM → executes them → stores results back into RAM → if you choose to save data, it moves from RAM to disk.

![Program Loading Diagram](https://algo.monster/courses/foundation/program-loading.svg)

---

- The **CPU** needs speed but cannot store much data.
- **RAM** provides fast access to reasonably large amounts of data but only temporarily.
- **Disk storage** holds massive amounts of data permanently but operates slowly.

This design is known as the **Von Neumann Architecture**, followed by most modern computers.  
It was proposed by mathematician **John von Neumann** in **1945**.

---

# Speed Hierarchy

![Memory Hierarchy](https://algo.monster/courses/foundation/memory-hierarchy.svg)

---

# In the Context of Programming

### Memory matters
When a program consumes too much RAM, the computer slows down.  
The OS begins using disk space as fake RAM (called **swap** or **virtual memory**), and because disk access is slower, overall performance decreases.

### Data structures live in RAM
When you create a list or an array, it occupies RAM. Understanding this helps visualize their performance characteristics.

### Loading takes time
The larger the file, the longer the read time. Efficient programs load data into RAM once and work with it there.
