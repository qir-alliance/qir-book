// Building on https://github.com/microsoft/Quantum/blob/main/samples/getting-started/teleportation/TeleportationSample.qs
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

namespace Teleportation {

    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Core;
    open Microsoft.Quantum.Arrays;

    // Pure quantum section of teleportation technique 
    operation Teleport (msg : Qubit, target : Qubit) : Unit {
        use register = Qubit();

        H(register);
        CNOT(register, target);

        CNOT(msg, register);
        H(msg);

        // Interdependent conditional section of teleportation technique 
        if (MResetZ(msg) == One) { Z(target); }
        if (IsResultOne(MResetZ(register))) { X(target); }
    }

    operation TeleportClassicalMessage (message : Bool) : Bool {

        use (msg, target) = (Qubit(), Qubit());
        if (message) {
            X(msg);
        }
        
        Teleport(msg, target);
        return MResetZ(target) == One;   
    }
}    