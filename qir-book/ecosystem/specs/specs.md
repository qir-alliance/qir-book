# QIR Specifications

QIR-specs provides a wide range of specification for the intermediate representation of hybrid computation. It aims to establish a standardized format that can express programs from different quantum front ends and convert them into code for diverse quantum-classical architectures. The specifications define a wide range of LLVM-based representations for classical and quantum [data types](qir-book/ecosystem/specs/data-types.md) and [callable](qir-book/ecosystem/specs/callables.md), enabling the construction of compiled hybrid programs from QIR compatible source compiler. Led by the QIR Alliance, the specification is designed to represent quantum programs within the LLVM [MLIR](qir-book/concepts/MLIR.md) framework.
A subset of these specifications is used to define each [target profiles](qir-book/ecosystem/specs/profile-target.md), as QIR offers a vast selection of capabilities with respect to current diversity of target machine architectures. The QIR [runtime](qir-book/ecosystem/specs/runtime.md) does not require the source compiler to provide a memory model with garbage collection. Instead, it offers a reference and alias tracking scheme. Such flexibility and extensibility of the QIR specifications allow for the incorporation of new features and capabilities as they emerge.




