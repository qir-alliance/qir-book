# Check if various frameworks are installed.
try:
    import qiskit
except ImportError:
    qiskit = None

try:
    import qutip
    import qutip.qip.circuit
    import qutip.qip.operations
except ImportError:
    qutip = None

try:
    import cirq
except ImportError:
    cirq = None