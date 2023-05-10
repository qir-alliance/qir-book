<!-- The answer meant to be unclear -->

# Why QIR Is in LLVM?

LLVM is an open-source compiler infrastructure project. It provides a collection of modular and reusable compiler and toolchain technologies for various target and front ends. Its design allows for flexiblity in performing various optimization and analysis techniques at the IR level. It serves as a common language to multiple targets, while providing general and target specific optimization, profiling, and analysis tools.

 LLVM is supported by decades of classical compilation research. For this reason, the interoperable and agnostic design of QIR was built based in LLVM. QIR benefits from the decades of research and development that have gone into LLVM. Moreover, the agnostic design of QIR allows it to target multiple backends, including simulators and actual quantum hardware, without compromising on tooling.
