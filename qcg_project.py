!pip install qiskit
!pip install pylatexenc
!pip install qiskit-aqua[cplex]
!pip3 install -e
from qiskit import *
from qiskit.aqua.algorithms import Grover
from qiskit.aqua.components.oracles import LogicalExpressionOracle
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.tools.visualization import *
from qiskit.tools.monitor import job_monitor

%%javascript
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
}

import time
import matplotlib.pyplot as plt
from IPython import display
def hold(circuit, state, counts, fig1, fig2, fig3):
    circuit.draw(output='mpl', fold=100, ax=fig1.gca())
    plot_state_qsphere(state, ax=fig2.gca())
    plot_histogram(counts, ax=fig3.gca())
    display.display(fig1)
    display.display(fig2)
    display.display(fig3)
    display.clear_output(wait=True)
    time.sleep(2)

import numpy as np
from qiskit.circuit.library import Diagonal
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator, DensityMatrix, ScalarOp
from qiskit.visualization import plot_state_qsphere, plot_histogram
from qiskit.converters import circuit_to_dag, dag_to_circuit

# Problem size: width and number of iterations
n = 5
steps = int(np.sqrt(2**n))
oracle=QuantumCircuit(5,name='oracle')
# Diagonal operators for mark 
mark_state = Statevector.from_label('11010')
mark_state2 = Statevector.from_label('11011')
mark_state3 = Statevector.from_label('11001')
mark_state4 = Statevector.from_label('11110')
mark_state5 = Statevector.from_label('11000')

mark_circuit1 = Diagonal((-1)**mark_state.data)  # circuit that induces a -1 phase on the mark_state
mark_circuit2 = Diagonal((-1)**mark_state2.data)  # circuit that induces a -1 phase on the mark_state2
mark_circuit3 = Diagonal((-1)**mark_state3.data)  # circuit that induces a -1 phase on the mark_state3
mark_circuit4 = Diagonal((-1)**mark_state4.data)   # circuit that induces a -1 phase on the mark_state4
mark_circuit5 = Diagonal((-1)**mark_state5.data)    # circuit that induces a -1 phase on the mark_state5

oracle.append(mark_circuit1, [0,1,2,3,4])
oracle.append(mark_circuit2, [0,1,2,3,4] )
oracle.append(mark_circuit3, [0,1,2,3,4])
oracle.append(mark_circuit4, [0,1,2,3,4])
oracle.append(mark_circuit5, [0,1,2,3,4])
oracle.draw()

amp = QuantumCircuit(5,name='amp');
amp.h([0,1,2,3,4])
amp.x([0,1,2,3,4])
invert_state = Statevector.from_label('11111')
invert_state = Diagonal((-1)**invert_state.data)
amp.append(invert_state,[0,1,2,3,4])
amp.x([0,1,2,3,4])
amp.h([0,1,2,3,4])
amp.draw()


grover_circuit = QuantumCircuit(5,5)
grover_circuit.h([0,1,2,3,4])
grover_circuit.append(oracle,[0,1,2,3,4])
grover_circuit.append(amp,[0,1,2,3,4])
grover_circuit.append(oracle,[0,1,2,3,4])
grover_circuit.append(amp,[0,1,2,3,4])
# Import Aer
from qiskit import Aer,execute

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')
# Create a Quantum Program for execution
job = execute(grover_circuit,backend)
result = job.result()
outputstate = result.get_statevector()
print(outputstate)
grover_circuit.measure([0,1,2,3,4],[0,1,2,3,4])
grover_circuit.draw()

backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = backend_sim.run(transpile(grover_circuit, backend_sim), shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()
counts = result_sim.get_counts(grover_circuit)
print(counts)
from qiskit.visualization import plot_histogram
plot_histogram(counts,figsize=(25,10))