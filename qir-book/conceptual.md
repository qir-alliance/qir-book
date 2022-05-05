# What is QIR?
__What is QIR, why we need it, where it is used, and how it is used.__
- "Formal specifications embedded in LLVM..., it expresses quantum specific operations as declared function calls on opaque data types.." {\cite}`mlirTN`  
- Using a conceptual example, showing what each component of the ecosystem does and how they can be applied to users' needs
  ![qirecosys-overview](qirecosys.png)

__Motivations for QIR Community/ Alliance?__
- What is interoperability?
- Interoperability opens doors to cross-fields problem-solving such as error correction 
  
__Heterogeneous Data in IR__
- QRAM model for circuit-based quantum computation
- How is QIR different from other quantum IRs?

__Why IR?__
- interoperability with specific backends profiles (1:m) 
-  HPC backends 
-  Optimization passes to classical and quantum code 
 \{cite}`mlirTN` 

__Why LLVM?__
-  LLVM years of R&D
- MLIR quantum dialect 
- cqor compiler is in LLVM 
- qir spec is in LLVM dialect 
- "QIR is embedded in LLVM IR"
-  C++ and Clang for quantum function expression to be at the same level as classical information at IR\{cite}`mccaskey2021extending`

__pyqir__ 
- Emission, Execution, and analysis (py-based PL)= pyqir 
- Pyqir matches the code to the defined profiles in QIR and generates .ll
- analysis: resource estimation
- includes/skip the steps for QIR spec and qcor, for py-based languages 
- where LLVM dialect meets/compiles the higher-level instruction to executables 

__qir_spec__ 
- Formalization of Quantum Operation in LLVM
- Type Abstraction and Formalization 
- Function call = operations on opaque data types 
- Entry point functions 

__qcor__ 
- Movements between abstraction levels (XACC and MLIR dialect) 
-  MLIR --> quantum instructions = stand-alone DSL\{cite}`mccaskey2021extending`
