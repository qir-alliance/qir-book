# Data Types

Data type specifications are types of values and variables allowed in source compilers. Besides simple data types such as Int, Double, Bool, Pauli, and Range, other data types in QIR are represented as pointers to opaque LLVM structures. Declaring the data types as opaque pointers allows the compiler to create a placeholder for the type without needing to know its complete definition at that point. In this section we examine a few of these data types provided by QIR-specs, such as `%Qubit`, `%Result` and `%Array`. For more data types and details, please refer to the [QIR-specs documentation](https://github.com/qir-alliance/qir-spec/blob/main/specification/v0.1/1_Data_Types.md).

# Qubit (`%Qubit`)

Qubits can be managed either statically or dynamically. If a value is known at compile time, the corresponding memory allocation for that value is static. This means that the memory is allocated and determined before the program is executed. On the other hand, if a value is not known until runtime, the memory allocation for that value is dynamic. Static qubits have target-specific identifiers known at compile time. They can be managed using `inttoptr` instruction. On the other hand, dynamic qubits allocation and tracking are managed during quantum runtime. The quantum execution functions provide the necessary mechanisms to allocate and release qubits.

# Measurement (`%Result`)

In hybrid computation, the result value can determine the next quantum or classical operations. Hybrid computation control flow requires the value result to dictate the following operations or termination. Currently, they are many quantum computing measurement approaches that venders take advantage of. The forward declaration of measurement values allows for flexibility to serve a wide range of measurement approaches. Further, QIR's classical runtime utility functions provide tools to compare and presents null, zero, one and negative values of measurement results.


# Arrays (`%Array`)

 The representation of array data is decided by the runtime. Access to array elements is provided through byte pointers that the calling code needs to bitcast to the appropriate type. Any array manipulations needed to access an item are done through corresponding runtime functions.

Immutable arrays are supported, and modified copies can be created. If the existing array is not used after the generation of the modified copy, it is possible to avoid the copy and modify the existing array in place instead. Array slicing and projection can be used to construct new arrays that allow similar optimizations.
Several utility functions are provided by the classical runtime to support arrays, including functions for creating, copying, concatenating, slicing, and projecting arrays. For example, the runtime function `__quantum__rt__array_create_1d` creates a new one-dimensional array, and `__quantum__rt__array_slice_1d` creates and returns an array that is a slice of an existing one-dimensional array. If an %Array* pointer is null for any of these functions, it is an indication of runtime failure. For multidimensional array support, the functions `__quantum__rt__array_create`, `__quantum__rt__array_slice`, and `__quantum__rt__array_project` are provided.
