# Callables

Callables in QIR are subroutines represented by a pointer to an opaque LLVM type, %Callable. They are associated with wrapper functions for different specializations. Functors, such as "Adjoint" and "Controlled," can modify the behavior of callables. Memory management tables handle reference and alias counts, and implementation tables ensure the correct specialization is used when invoking callables.

External/intrinsic callables are declared in the quantum source and defined in external components linked with the compiled quantum code. For example, the targets' quantum instruction sets are represented as sets of external callables. The source compiler is responsible for lowering the hybrid code, generating appropriate LLVM declarations for the external callables referenced in the code.

QIR does not directly support generic or type-parameterized callables, but instead generates specific callables for concrete type parameters. The classical runtime provides functions for initializing, invoking, and manipulating callable values.
