
# Why QIR Is in LLVM?

LLVM is an open-source compiler infrastructure project. It provides a collection of modular and reusable compiler and toolchain technologies for various target and front ends. Its design allows for flexibility in performing various optimization and analysis techniques at the IR level. LLVM representation is in Static Single Assignment (SSA) form by which variables are assigned exactly once throughout the program. It serves as a common representation for different development frameworks and target architectures, offering both general and target specific optimization, profiling, and analysis tools.
The LLVM project is supported by decades of classical and heterogeneous compilation research. For this reason, the interoperable and modular design of QIR was based in LLVM and [MLIR](qir-book/concepts/MLIR.md).
