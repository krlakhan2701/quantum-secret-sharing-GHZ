# Quantum Secret Sharing (GHZ)

This repository contains implementations and experiments for quantum secret sharing using GHZ states.

## Reproducing the Python environment

To reproduce the environment used for the notebooks (recommended to keep environments isolated):

1. Create and activate a new virtual environment:

```bash
python3 -m venv .venv-qiskit
source .venv-qiskit/bin/activate
```

2. Upgrade packaging tools and install the minimal runtime used here:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install qiskit-terra==0.22.3 ipykernel matplotlib pylatexenc
```

Notes:
- The full `qiskit` meta-package can require `qiskit-aer` which may need native build tools (conan, C/C++ toolchain) to build. If you need simulators from `qiskit-aer`, prefer installing via `conda` or ensure build tools are available.
- After installing packages, register a kernel for the notebook UI:

```bash
python -m ipykernel install --user --name qss-qiskit --display-name "Python (qss-qiskit)"
jupyter kernelspec list
```

3. Open the notebooks in VS Code and select the `Python (qss-qiskit)` kernel from the kernel picker.

If you prefer conda or need `qiskit-aer` binary wheels, use:

```bash
conda create -n qss-qiskit python=3.11
conda activate qss-qiskit
conda install -c conda-forge qiskit matplotlib ipykernel pylatexenc
python -m ipykernel install --user --name qss-qiskit --display-name "Python (qss-qiskit)"
```

If anything fails, open an issue or ask for help and include the error messages.
