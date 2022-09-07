// Building on https://github.com/microsoft/Quantum/blob/main/samples/getting-started/teleportation/TeleportationSample.qs
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.
namespace Teleportion{

    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Core;
    open Microsoft.Quantum.Arrays;

    @EntryPoint()
    operation Greetings() : Unit { 
        mutable binary=[1, 0, 1, 0, 0];
        let msg = ForEach(int2bool, binary);
        let transferred= ForEach(TeleportClassicalMessage, msg);
        for index in 0 .. Length(transferred)-1{
            Message($"{transferred[index]}");
        }     
    }

}