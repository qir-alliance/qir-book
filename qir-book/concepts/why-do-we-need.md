# Why do we need it?

The quantum computing field is faced with a surge in numbers of choices for hardware, software toolkits, and programming languages. The QIR ecosystem creates abstraction layers and tools required to facilitate interoperability. As shown in Figure 1, the QIR compilation model has 3 phases, each supported by an ecosystem tool. Starting with the language-specific phase of the compilation, the QIR ecosystem receives the instructions coded in a quantum programming language, such as Q#, Pyquil, Qiskit and Cirq. By the end of this phase, the generic QIR will be generated for enabled compilers, or by using Pyqir. The role of qir-spec is to provide representation for quantum programs in LLVM, to map the source code to QIR. In the last two phases, users can extract the generic and the transformed QIR code in `.ll` files. The qat tools can transform and analyze the instructions during the generic and target-specific phases.

 ![Figure 1](https://github.com/PariaNaghavi/qir-book/blob/main/qir-book/concepts/Figure1.png)

Every phase demonstrated in Figure 1 is accompanied by a tool maintained by the QIR Alliance. Collectively, they provide front-end, intermediate, and back-end support for other enabled compilers or languages compatible with Pyqir. If you were to take an abstraction elevator, you would find domain specific and quantum assembly languages at the higher level than the QIR ecosystem. The input instructions for QIR can be in Q# which is a high-level domain specific programming language or potentially OpenQASM 3.0, a multi-level IR assembly language. Although assembly languages are considered low level languages, they reside above the QIR compilation model. In Figure 1, the source code can be in a `.qasm`, `.py` or `.qs` file. Using the QIR tools, we can further lower the instructions to the target code, while applying optimization, analysis, and validation required by the machine.

Hardware vender-designed compilers mostly support code generation mapped to the requirements of their own hardware. However, the QIR aims to provide means for hardware-agnostic workflow. It uses compiler profiling to define requirements of target machines. The generic QIR can be further lowered according to target profiles. Users can target multiple machines with one set of instructions, since the adaptations needed for each is abstracted out.

The current limitations of noisy quantum devices have resulted in a strong shift towards hybrid approaches, utilizing classical (e.g., CPU, GPU) and quantum hardware resources together to complete the computational model [[1]](https://arxiv.org/pdf/2207.06850.pdf). The QIR is a hybrid compatible compiler. The LLVM backend of the ecosystem allows for compiler native classical control at the IR level, whereas most quantum compilers add classical support to a purely quantum compiler. The QIR ecosystem facilitates interoperability between languages, compiler libraries, transformations, analyzes, and optimizations. Withal, it supports interoperability for heterogeneous quantum-classical hardware architecture. This bridges the gap to place the QPU as an accelerator in HPC architectures.

## Hybrid quantum programs are the future of quantum computing

- QRAM model for circuit-based quantum computation
- [1](https://arxiv.org/pdf/2207.06850.pdf)
- [2](https://arxiv.org/pdf/2206.12950.pdf)

## Why an {term}`IR`?

- What is interoperability?
  - Interoperability with specific backends hardware profiles
- Optimization passes to classical and quantum code {cite}`mlirTN`
- Easy to simulate on HPC backends

## Motivations for QIR Community/ Alliance?

- {term}`Interoperability` opens doors to cross-fields problem-solving
