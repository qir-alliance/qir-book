# How do we use it?

![qirecosys-overview](qirecosys.png)

## Applications

- Ideally you don't directly interact with QIR :)
- Resource optimization passes with `qat`

## Infrastructure

### `pyqir`

- Emission, Execution, and analysis (py-based PL)= pyqir
- PyQIR matches the code to the defined profiles in QIR and generates .ll
- analysis: resource estimation?
- includes/skip the steps for QIR spec and qcor, for py-based languages
- where LLVM dialect meets/compiles the higher-level instruction to executables

### `qcor`

- Movements between abstraction levels (XACC and MLIR dialect) {cite}`mlirTN`
- MLIR --> quantum instructions = stand-alone DSL {cite}`mccaskey2021extending`

## Simulation

## Hardware

- profiles for different hardware platforms
