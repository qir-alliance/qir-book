# Profiles and Code Generation

LLVM uses profiles to guide code generation. A QIR profile refers to a subset of specifications that defines a particular functionalities, registers, and features supported by a target machine. During code generation, the compiler maps high-level constructs and operations to the corresponding machine instructions supported by the target.

The QIR specifications for code generation outline several areas where it may deviate from a simple translation of intrinsics to target machine code. These specifications provide guidance for code generators to adapt the QIR to the target architecture, using [QAT](https://github.com/qir-alliance/qat)'s tools to ensure compatibility with the underlying runtime environment.

QIR runtime specifications assume no garbage collection. As a result, it manages both the stack and reference counting on heap. A runtime with memory management tools may require modifications to track memory allocation and reference counting.

For type representation, QIR uses opaque pointer types for certain data structures, such as `%Qubit`, `%Result` and `%Array`. The code generator must provide the same data types or alternative representations required by the target architecture. The quantum operations available on the target architecture may differ from the QIR's and has to be rewritten with sequences of QIR intrinsics.



