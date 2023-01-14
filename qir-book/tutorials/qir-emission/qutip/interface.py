# -*- coding: utf-8 -*-
"""
====
# qwop

This module provides a high-level interface for working with QIR programs and
other Python based quantum computing tools.
This file contains some misc utilities and a abstract class to help structure
specific exporters.
====
"""

from abc import ABCMeta, abstractmethod

from typing import (
    Any, Literal, Optional, Union, Generic, TypeVar, overload, TYPE_CHECKING
)

import pyqir as pqp

from _optional_deps import qiskit as qk, cirq, qutip as qt

TOutput = TypeVar('TOutput')

__all__ = [
    'CircuitLikeExporter',
    'export_block'
]


# General utility functions
def _resolve_id(value: Any, default: str = "unsupported") -> Union[int, str]:
    if hasattr(value, "id"):
        return value.id
    return default

def _resolve(value, in_):
    id = _resolve_id(value)
    if id not in in_:
        in_[id] = len(in_)
    return in_[id]

def is_circuit_like(block : pqp.BasicBlock) -> bool:
    return all(
        isinstance(instruction, (pqp.QirQisCallInstr, pqp.QirQirCallInstr))
        for instruction in block.instructions
    )

class CircuitLikeExporter(Generic[TOutput], metaclass=ABCMeta):
    @abstractmethod
    def on_simple_gate(self, name, *qubits) -> None:
        pass

    @abstractmethod
    def on_measure(self, qubit, result) -> None:
        pass

    @abstractmethod
    def on_comment(self, text) -> None:
        pass

    @abstractmethod
    def export(self) -> TOutput:
        pass

    @abstractmethod
    def qubit_as_expr(self, qubit) -> str:
        pass

    @abstractmethod
    def result_as_expr(self, result) -> str:
        pass

@overload
def export_block(block: pqp.BasicBlock, to: CircuitLikeExporter[TOutput]) -> Optional[TOutput]: ...
@overload
def export_block(block: pqp.BasicBlock, to: Literal["openqasm2"]) -> Optional[str]: ...
if TYPE_CHECKING or qk is not None:
    @overload
    def export_block(block: pqp.BasicBlock, to: Literal["qiskit"]) -> Optional[qk.QuantumCircuit]: ...
if cirq is not None:
    @overload
    def export_block(block: pqp.BasicBlock, to: Literal["cirq"]) -> Optional[cirq.Circuit]: ...
if qt is not None:
    @overload
    def export_block(block: pqp.BasicBlock, to: Literal["qutip"]) -> Optional[qt.qip.circuit.QubitCircuit]: ...

def export_block(block, to):
    import qwop.exporters.cirq as _cirq_ex
    import qwop.exporters.openqasm2 as _openqasm2_ex
    import qwop.exporters.qiskit as _qiskit_ex
    import qwop.exporters.qutip as _qutip_ex

    if to == "openqasm2":
        exporter = _openqasm2_ex.OpenQasm20Exporter
    if qk is not None and to == "qiskit":
        exporter = _qiskit_ex.QiskitExporter
    if cirq is not None and to == "cirq":
        exporter = _cirq_ex.CirqExporter
    if qt is not None and to == "qutip":
        exporter = _qutip_ex.QuTiPExporter
    else:
        # Assume to is an exporter
        exporter = to
    return exporter(block).export()