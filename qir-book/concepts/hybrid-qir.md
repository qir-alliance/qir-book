# Hybrid in QIR #

- Hybrid quantum instructions are separated into blocks, separation of classical and quantum code

![alt text](/qir-book/tutorials/qir-emission/qiskit/teleport_qiskit.png)
- Post measurement conditional in teleportation as an example
## LLVM
* LLVM is a collection of modular and reusable compiler and toolchain technologies for developing and optimizing various programming languages
* It is open-source and maintained by a  community of contributors
* IR allows for easy analysis and manipulation of code, making it a popular choice for many programming languages, compilers, and other tools.
* libraries and tools for visualizing, debugging, and profiling of code
* Blocks:  linear sequences of instructions with a single-entry point and a single exit point.
    - to show the control flow: to analyze and optimize the code
    - CFG
* code profiling:
    - CPU profiling vs. memory profiling (is it relevant?)
* back ends include register allocation and scheduling
* In LLVM, registers are used as temporary storage locations for values
    - register allocator and register bank: assign values to physical registers of a target architecture during the code generation process
* Block Separation: QPU, CPU and between
    - __quantum__rt__ and __quantum__qis__

## Compilers:
* JIT compiles code at runtime, allowing for optimization
* AOT compiles code before runtime, can't detect bugs until the


* Advantages of modularity of QIR: shared passes: optimization and analysis. What else?



