# What is QIR?
- What is QIR, why we need it, where it is used, and how it is used.
- "Formal specifications embedded in llvm..., it expresses quantum specific operations as declared function calls on opaque data types.." \{cite}`mlirTN`  
- Using a conceptual example, showing what each component of the ecosystem does and how they can be applied to users needs.
  ![qirecosys-overview](qirecosys.png)
__What is QIR, why we need it, where it is used, and how it is used.__

__Motivations for QIR Community/ Alliance?__
- interoperability opens doors to cross-field problem-solving such as error correction 
- Resource estimation
__Hetrogenious Data at IR__
- QRAM model for circuit-based quantum computation

__Why IR?__
- interoperability with specific backends profiles  
-  HPC backends 
-  llvm years of R&D
-  Optimization passes to classical and quantum code 
 \{cite}`mlirTN` 

__Why LLVM?__
- qir spec is in LLVM dialect 
- "QIR is embedded in LLVM IR"
- cqor compiler is in LLVM 
-  MLIR quantum dialect 
-  C++ and Clang for quantum function expression at the same level as classical information\{cite}`mccaskey2021extending`

__pyqir__ 
- Emission, Execution and analysis (py-based PL)= pyqir 
(analysis: resource estimation)- Pyqir matches the profile to QIR and generates .ll
- includes/skip the steps for QIR spec and qcor use for py-based languages. 
- where llvm dialect meets/compiles the higher level instruction to executables 

__QIR Spec__ 
- Formalization of Quantum Operation in LLVM
- Type Abstraction and Formalization 
- Function call = operations on opaque data types 
- Entry point functions 

__qcor__ 
- Movements between abstraction levels (XACC and MLIR dialect) 
- "qcor translates quantum kernels ultimately to the
-  MLIR --> quantum instructions = stand-alone DSL\{cite}`mccaskey2021extending`