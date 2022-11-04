
# QIR generation with Q# #

In this section, QIR is generated from Q# code for teleportation to transfer the binary representation of “hello world!”, followed with ASCII decoding. Teleportation technique contains heterogeneous instructions at the compilation time. The interdependent conditionals following the measurement of the source and the auxiliary qubits in teleportation determine the next quantum gate operations on the target qubit.

Computations involving heterogeneous instructions at compile time can benefit from QIR enabled compilers. QIR is generated in LLVM, which is backed by decades of classical compilation research and development. Hybrid quantum algorithms were [defined](https://arxiv.org/pdf/2207.06850.pdf) to rely on both classical and quantum resources to fulfill the abstract computational model of the algorithm. In the next series of tutorials, a hybrid classical-quantum algorithm such as VQE or HHL (?) will be used to demonstrate further capabilities of QIR.
