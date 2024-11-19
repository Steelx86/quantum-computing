from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

print(qc)

qc.h(0)

print(qc)

qc.cx(0, 1)

print(qc)

qc.measure([0, 1], [0, 1])

print(qc)

simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()

counts = result.get_counts(qc)
print("Counts:", counts)
