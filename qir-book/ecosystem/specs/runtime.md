# Runtime

This section is going to focus on specifications defined for the runtime of QIR. For heterogeneous computation, quantum and classical executions happen on different processing units.

Frist let’s consider quantum gates and qubits. The QIR specification does not include any definitions for gates, leaving it up to the development framework's compiler to define a set of quantum operations as LLVM functions. During the runtime, qubits are managed through a series of operations that handle their allocations and releases. To allocate a single qubit, the `__quantum__rt__qubit_allocate` function is used. This operation reserves the necessary resources and prepares the qubit for use in computations. When a qubit is no longer needed, it can be released, by which freeing its resources and making it available for reuse. It's important to handle the state of qubits properly during their lifetime. This includes ensuring that qubits are released properly and initialized according to the target specific compilation.

In QIR, the runtime memory management occurs on the classical side, and functions are available to monitor and control hybrid computations. These functions handle feedback messages and failures during execution. The memory management approach can vary across source platforms, and in QIR, it utilizes a reference and alias counting scheme instead of relying on garbage collection.

The compiler takes responsibility for tracking and modifying reference and alias counts. It generates code with appropriate calls to runtime functions, ensuring accurate count updates. Notably, these count modifications only apply to the specific instance and not inner items like tuple elements or arrays.

Reference counts keep track of the number of handles providing access to a value in LLVM. They determine when the value can be released. Initially, a value is assigned a reference count of 1 and is released when the count reaches 0. Alias counts track handles to a value in the source platform and guide data copying decisions. They are particularly useful for immutable data types represented as pointers in QIR.

QIR defines dedicated runtime functions for manipulating reference and alias counts, allowing precise count updates. Classical runtime implementations can offer alternative garbage collection mechanisms or treat count modifications as hints or no-ops based on specific needs.


