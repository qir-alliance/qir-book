# What is QIR?

Quantum Intermediate Representation (QIR) is a specification for expressing quantum programs.

## QIR Specification

- Formalization of Quantum Operation in {term}`LLVM`
  - QIR is embedded in LLVM IR {cite}`mlirTN`
- Type Abstraction and Formalization
- Function call = operations on opaque data types
- Entry point functions

## Why LLVM?

- LLVM years of R&D
- MLIR quantum dialect
- Other tools like qcor compiler use LLVM
- C++ and Clang for quantum function expression to be at the same level as classical information at IR {cite}`mccaskey2021extending`

## How is QIR different from other quantum IRs?

- There are not really any at the same level of abstraction/model
