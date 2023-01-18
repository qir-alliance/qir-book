from qutip import *
from qutip.qip.circuit import QubitCircuit, Measurement, Gate
from qutip import basis, tensor, identity
import numpy as np

teleportation = QubitCircuit(3, num_cbits = 2, input_states = ["\psi", "0", "0", "c0", "c1"])

teleportation.add_gate("SNOT", targets=[1])
teleportation.add_gate("CNOT", targets=[2], controls=[1])
teleportation.add_gate("CNOT", targets=[1], controls=[0])
teleportation.add_gate("SNOT", targets=[0])
teleportation.add_measurement("M0", targets=[0], classical_store=1)
teleportation.add_measurement("M1", targets=[1], classical_store=0)
teleportation.add_gate("X", targets=[2], classical_controls=[0])
teleportation.add_gate("Z", targets=[2], classical_controls=[1])

def ket_0():
    return ket("0")

def ket_1():
    return ket("1")
to_send = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1,
       0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0,
       0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0,
       0, 0, 1, 0, 0, 0, 0, 1]

# collecting teleported messages
teleported=[]
for x in to_send:
    msg= ket(str(x))
    state = tensor(msg, basis(2,0), basis(2,0))
    state_final = teleportation.run(state)
    final_measurement = Measurement("start", targets=[2])
    result = final_measurement.measurement_comp_basis(state_final)[-1]
    if np.array_equal(result, [1, 0]): teleported.append (0)
    if np.array_equal(result, [0, 1]): teleported.append (1)


# encoding binary to utf-8
teleported_str = ''.join(str(x) for x in teleported)
teleported_base2= int(teleported_str, 2)
teleported_base2
teleported_base2_chunks= (teleported_base2.bit_length() +7) // 8
teleported_bytes = teleported_base2.to_bytes(teleported_base2_chunks, "big")
received =teleported_bytes.decode(encoding='utf-8')
received