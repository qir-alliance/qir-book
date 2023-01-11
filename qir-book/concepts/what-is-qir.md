# What is QIR?

The QIR ecosystem collectively creates a compiler system with the goal of interoperability for hybrid computation. Let’s consider a simple model of compilers consists of front-end, middle end and back-end abstraction layers. Together, they complete the goal of a compiler to transform source code into target-machine code. The front-end parses the sources code into abstract syntax tree and emits Intermediate Representation (IR) for the middle abstraction layer of the compiler. Transformations, analyses, and optimizations are performed on IRs before the back end generates the machine code.

Modern compilers take advantage of introducing new layers of abstraction in the middle end, dissolving traditional compiler phases. This new approach allows for Multiple Level Intermediate Representation (MLIR) compiler systems. Tools and components that lower the instruction with MLIR approach can be reused for different source languages and target machines. It was initially [introduced](https://arxiv.org/pdf/2101.11365.pdf) for in machine learning workflows to facilitate compilation for co-processing. MLIR spans the abstraction levels from after source code to machine code generation, creating a space for compiler extensibility and reusability with different high-level languages and low-level targets.

LLVM is consisted of libraries that support building compilers and compilation processes. It unifies different high-level languages into a common IR. Its modular design [allows](https://arxiv.org/pdf/2101.11365.pdf) for implementation of MLIR, using Static Single Assignment (SSA)-based IR data structures. The LLVM technologies have been used widely in classical compilation developments, because it creates a common IR at the end of the front-end phase, regardless of source language. Hence, functionalities developed in LLVM are shared easily for different source languages, target machines, analyses, and transformations. This cross language and hardware interoperability was needed in the current state of quantum computing field, so computational tools could be shared and reused.

Quantum Intermediate Representation (QIR) was designed and developed with the same interoperability objectives as LLVM. In fact, QIR is in LLVM.

## QIR Specification

- Formalization of Quantum Operation
  - QIR is embedded in LLVM IR
- Type Abstraction and Formalization
- Function call = operations on opaque data types
- Entry point functions

