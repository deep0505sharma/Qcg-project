# Solving Boolean SAT Problem using Grover’s Algorithm

### This project is made as a part of the IITR QCG- Open Summer Project, 2022. It involves solving a boolean satisfiability problem (dinner problem) using Grover's algorithm.

<img src="https://user-images.githubusercontent.com/103529456/174482753-c6491988-ccb6-40c5-8fc8-56782ca4814d.gif" alt="qiskit" width="500"/>

## 📌 Table of Contents
* [Description / Internal Working](#description)
* [Features](#features)
* [Tech Stack / Dependencies](#tech-stack)
* [Getting Started / Setup](#getting-started)
* [User Guide](#📖-user-guide)
* [Challenges Faced and Learnings](#💡-challenges-faced-and-learnings)
* [Resources](#resources)


<a id="description"></a>
## 📓  Description / Internal Working
This project aims at solving a dinner problem (boolean satisfiability problem ) using Grover's algorithm. 

SAT(Boolean Satisfiability Problem) is the problem of determining if there exists an interpretation that satisfies a given boolean formula. It asks whether the variables of a given boolean formula can be consistently replaced by the values TRUE or FALSE in such a way that the formula evaluates to TRUE. If this is the case, the formula is called satisfiable. On the other hand, if no such assignment exists, the function expressed by the formula is FALSE for all possible variable assignments and the formula is unsatisfiable.

A Boolean SAT problem can be solved by determining all the input combinations that fit into a boolean function such that the output is true. Since searching through the combinations is needed, Grover's algorithm is used.

Grover’s algorithm, also known as the quantum search algorithm, is a quantum algorithm designed by Los Grover in 1996 to search for an element in an unsorted array quadratically faster ( O(sqrt(N) ) : Time Complexity) than the classical linear search for large datasets. This project aims at solving a particular boolean satisfiability problem (dinner problem) using Grover's algorithm.

### Problem Statement
Frank wants to throw a dinner party to celebrate Alice and Bob’s engagement. He is also considering inviting their mutual friends Charles, Dave and Eve. However, he is aware that Charles will come to the party only if Dave comes without Eve. Frank wants to know what possible combinations of invitations he can write for his friends Alice, Bob, Charles, Dave and Eve.

Help Frank calculate all the possible combinations using Grover’s algorithm.

### Working
1. Create 5 quantum channel labelled as qi, i ∈ {0, 1, 2, 3, 4}. where qo represents presence of Alice, q1 represents presence of Bob, q2 represents presence of Charles, q3 represents presence of Dave, q4 represents presence of Eve. Apply Hadamard gate to each channel - it creates superposition of every possible states.
2. Create an oracle that flips a state if it satisfies the problem statement.
3. Reflect all the states about the mean and amplify the amplitudes of the possible states that satisfy the problem statement.
4. Run the final circuit on Statevector Simulator Backend - to calculate amplitudes, and Qasm Simulator - to print histogram of the frequency of the states.

<a id="features"></a>
## 🚀 Features
- The amplitudes of the states are calculated by running the circuit on a Statevector Simulator Backend.
- Final Grover circuit drawn in a image type file (.png)
- The possible counts of all the states is measured by running the circuit on a Qasm Simulator and stored in counts.txt file.
- The histogram of the frequency of all the states is also plotted.

<a id="tech-stack"></a>
## 💻 Tech Stack / Dependencies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-%236929C4.svg?style=for-the-badge&logo=Qiskit&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

***Python*** : The complete project is written in python programming language.

***Qiskit*** : Provides tools for creating and manipulating quantum programs and running them on prototype quantum devices on IBM Quantum Experience or on simulators on a local computer.

***Numpy*** : To work with matrices.

***matplotlib*** : Plotting library for python, used to plot figures.  

***Visual Studio Code*** : Editor used in the project.

<a id="getting-started"></a>
## 📦 Getting Started / Setup

1. Clone this repository.

```javascript
  git clone https://github.com/deep0505sharma/Qcg-project.git
```  

2. Install the given requirements, one-by-one-

```javascript
  pip3 install jupyter

  pip3 install qiskit

  pip3 install matplotlib
```

<a id="user Guide"></a>
## 📖 User Guide

### 1. Amplitude
 The amplitudes of the states are calculated by running the circuit on a Statevector Simulator Backend.

Statevector([-0.08562621-1.64517430e-16j, -0.08562621-5.70308882e-16j,
             -0.08562621-4.59238028e-16j, -0.08562621-5.47310893e-16j,
             -0.08562621-1.81524369e-16j, -0.08562621-4.97960940e-16j,
             -0.08562621-4.86993603e-16j, -0.08562621-5.25327667e-16j,
             -0.08562621-3.42227314e-16j, -0.08562621-5.62145286e-16j,
             -0.08562621-5.23634951e-16j, -0.08562621-6.33539263e-16j,
             -0.08562621-3.31877132e-16j, -0.08562621-5.00810593e-16j,
             -0.08562621-5.62029814e-16j, -0.08562621-5.03945867e-16j,
             -0.08562621-9.25056760e-17j, -0.08562621-4.08091507e-16j,
             -0.08562621-3.14367887e-16j, -0.08562621-3.64276836e-16j,
             -0.08562621-2.58698834e-16j, -0.08562621-3.01049095e-16j,
             -0.08562621-3.10898440e-16j, -0.08562621-2.34740755e-16j,
              0.4005097 +2.19258526e-15j,  0.4005097 +2.54512603e-15j,
              0.4005097 +2.01811652e-15j,  0.4005097 +2.18576796e-15j,
             -0.08562621-4.50684960e-16j, -0.08562621-4.60023861e-16j,
              0.4005097 +2.33360524e-15j, -0.08562621-4.77036923e-16j],
            dims=(2, 2, 2, 2, 2))

### 2. Final Circuit
The final Grover circuit in (.png) type file

<img src="https://user-images.githubusercontent.com/103529456/174485156-2fc7da23-d729-4964-a6e6-fb443cc7cdde.png" alt="grover_circuit" width="705"/>

### 3. Counts of the State
The counts of all the possible states, used to print histogram, is present in ***counts.txt*** file in the project directory.
[Link_to_Counts.txt_file](counts.txt)

### 4. Histogram
The histogram of the frequency of all the states is also included. It is calculated using the counts, which are measured by running the circuit on a Qasm Simulator.

<img src="https://user-images.githubusercontent.com/103529456/174485457-5943064c-3181-4318-999e-13c20749ea01.png" alt="histogram" width="705"/>

<a id="challenges"></a>
## 💡 Challenges faced and learnings

- Learnt about qubits, quantum gates and quantum circuits.
- Got familiar with Qiskit and Grover's Algorithm.
- Faced major challenges in implementing diffuser for amplitude amplification.
- Learnt about how matplot library can be used to plot figures.

<a id="resources"></a>
## 📚 Resources

* [ Help from IIT Roorkee Quantum Computing Group](https://www.facebook.com/qcgiitr/)
* [Qiskit Textbook ](https://qiskit.org/textbook/ch-states/introduction.html)
* [Grover's Algorithm](https://youtu.be/0RPFWZj7Jm0)
* [Grover's Algorithm Qiskit Textbook](https://qiskit.org/textbook/ch-algorithms/grover.html)
* [SAT Problem using Grover's Algorithm](https://qiskit.org/textbook/ch-applications/satisfiability-grover.html)

---------
  ```javascript
  if you_Liked:
      ⭐ star_Repository()
  #Thank You!! 🙏
  ```
-----------
