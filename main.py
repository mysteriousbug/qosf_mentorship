from qiskit import QuantumCircuit, QuantumRegister, transpile
from math import pi

# Define the U gate decomposition
def U_gate(theta, phi, lambda_, qc, qubit):
    qc.rz(lambda_, qubit)
    qc.ry(theta, qubit)
    qc.rz(phi, qubit)

# Construct the CCX (Toffoli) gate
def construct_CCX(qc, control1, control2, target):
    U_gate(pi/2, 0, pi/2, qc, target)
    qc.cx(control2, target)
    U_gate(-pi/2, 0, pi/2, qc, target)
    qc.cx(control1, target)
    U_gate(pi/2, 0, -pi/2, qc, target)
    qc.cx(control2, target)
    U_gate(-pi/2, 0, pi/2, qc, target)

# Construct the CCCX (Fredkin) gate
def construct_CCCX(qc, control1, control2, control3, target):
    U_gate(pi/2, 0, pi/2, qc, target)
    qc.cx(control3, target)
    U_gate(-pi/2, 0, pi/2, qc, target)
    qc.cx(control2, target)
    U_gate(pi/2, 0, -pi/2, qc, target)
    qc.cx(control3, target)
    U_gate(-pi/2, 0, pi/2, qc, target)
    qc.cx(control1, target)
    U_gate(pi/2, 0, -pi/2, qc, target)
    qc.cx(control3, target)
    U_gate(-pi/2, 0, pi/2, qc, target)
    qc.cx(control2, target)
    U_gate(pi/2, 0, -pi/2, qc, target)
    qc.cx(control3, target)
    U_gate(-pi/2, 0, pi/2, qc, target)

# Construct the multi-controlled X gate
def construct_multi_controlled_X(qc, control_qubits, target):
    num_controls = len(control_qubits)
    for control in control_qubits:
        qc.cx(control, target)

# Create a quantum circuit with 4 qubits
qr = QuantumRegister(4)
qc = QuantumCircuit(qr)

# Construct CCX (Toffoli) gate
construct_CCX(qc, qr[0], qr[1], qr[2])

# Print the CCX gate circuit
print("CCX (Toffoli) gate circuit:")
print(qc)

# Create a new quantum circuit with 4 qubits
qr = QuantumRegister(4)
qc = QuantumCircuit(qr)

# Construct CCCX (Fredkin) gate
construct_CCCX(qc, qr[0], qr[1], qr[2], qr[3])

# Print the CCCX gate circuit
print("\nCCCX (Fredkin) gate circuit:")
print(qc)

# Prompt the user for the number of control qubits
num_controls = int(input("Enter the number of control qubits: "))

# Create a quantum circuit with (num_controls + 1) qubits
qr = QuantumRegister(num_controls + 1)
qc = QuantumCircuit(qr)

# Construct the multi-controlled X gate
construct_multi_controlled_X(qc, qr[:num_controls], qr[num_controls])

# Print the general multi-controlled X gate circuit
print("\nGeneral Multi-Controlled X gate circuit:")
print(qc)


