// Building on https://github.com/microsoft/Quantum/blob/main/samples/getting-started/teleportation/TeleportationSample.qs
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

// In this section, QIR is generated from Q# code for teleportation to transfer the
// binary representation of “hello world!”, followed with ASCII decoding. 
// Teleportation technique contains heterogeneous instructions at the compilation time. The interdependent 
// conditionals following the measurement of the source and the auxiliary qubits in teleportation 
// determine the next quantum gate operations on the target qubit.
// Computations involving heterogeneous instructions at compile time can benefit from QIR enabled compilers. 
// QIR is generated in LLVM, which is backed by decades of classical compilation research and development. 
// Hybrid quantum algorithms were [defined](https://arxiv.org/pdf/2207.06850.pdf) to rely on both classical and
// quantum resources to fulfill the abstract computational model of the algorithm. In the next series of tutorials,
// a hybrid classical-quantum algorithm such as VQE or HHL (?) will be used to demonstrate further capabilities of QIR.

namespace Teleportion{

    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Core;
    open Microsoft.Quantum.Arrays;

    // Converts data type: int to bool 
    operation int2bool(bit: Int) : Bool {
            if (bit == 1){return true;}
            else {return false;}
        }
    // Converts data type: bool to int 
    operation bool2int(msg: Bool) : Int {
            if (msg == true){return 1;}
            else {return 0;}
        }
    // Pure quantum section of teleportation technique 
    operation Teleport (msg : Qubit, target : Qubit) : Unit {
        use register = Qubit();

        H(register);
        CNOT(register, target);

        CNOT(msg, register);
        H(msg);


        if (MResetZ(msg) == One) { Z(target); }

        if (IsResultOne(MResetZ(register))) { X(target); }
    }
    // Interdependent conditional section of teleportation technique 
    operation TeleportClassicalMessage (message : Bool) : Bool {
    
        use (msg, target) = (Qubit(), Qubit());

    
        if (message) {
            X(msg);
        }

    
        Teleport(msg, target);

        
        return MResetZ(target) == One;
    }

}