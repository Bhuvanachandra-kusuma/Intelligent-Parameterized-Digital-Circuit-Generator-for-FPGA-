# Intelligent Parameterized Digital Circuit Generator for FPGA

> A Python-driven EDA automation framework for parameterized adder generation, synthesis, and design space exploration using Xilinx Vivado.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Verilog](https://img.shields.io/badge/Verilog-RTL-orange?style=flat-square)
![Vivado](https://img.shields.io/badge/Vivado-Kintex--7-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## Overview

This project implements a **circuit generator** — a software tool that automatically generates, synthesizes, and evaluates parameterized digital hardware designs. The framework targets Xilinx Kintex-7 FPGA (xc7k70t) and automates the full RTL-to-report pipeline:

```
Python (generator) → Verilog (RTL) → Vivado TCL (synthesis) → Reports → Analysis & Visualization
```

Two adder architectures are generated and compared across configurable bit-widths:

- **Ripple Carry Adder (RCA)** — leverages Xilinx dedicated carry-chain primitives
- **Carry Lookahead Adder (CLA)** — parallel prefix logic for theoretical speed advantage

---

## Key Results

| Bit-Width | Architecture | LUT Usage | Critical Path Delay |
|-----------|-------------|-----------|-------------------|
| 16-bit | RCA | **~43% lower** ✅ | **~10% lower** ✅ |
| 16-bit | CLA | Baseline | Baseline |
| 8-bit | RCA | Lower | Comparable |
| 4-bit | RCA | Lower | Comparable |

> **Finding:** On Xilinx FPGAs, RCA consistently outperforms CLA due to dedicated **carry-chain primitives** (CARRY4/CARRY8). CLA's parallel prefix logic cannot exploit these primitives, making RCA the architecture-aware optimal choice for FPGA targets.

---

## Project Structure

```
├── generator/
│   └── generator.py        # Core: parameterized Verilog RTL generation
│
├── scripts/
│   ├── run_all.py          # Master script: runs full pipeline end-to-end
│   ├── analyze.py          # Parses Vivado utilization & timing reports
│   ├── plot.py             # Generates comparison graphs (Matplotlib)
│   └── selector.py         # Smart architecture recommendation engine
│
├── vivado/
│   └── run.tcl             # TCL script: Vivado project, synthesis, report export
│
├── generated/              # Auto-generated Verilog files (RCA/CLA, 4/8/16-bit)
├── results/
│   ├── *.txt               # Raw Vivado utilization & timing reports
│   └── graphs/
│       ├── lut_vs_bits.png     # LUT usage comparison across bit-widths
│       └── delay_vs_bits.png   # Critical path delay comparison
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## How It Works

### 1. RTL Generation (`generator/generator.py`)
Generates synthesizable Verilog for RCA and CLA architectures at any specified bit-width. The generator is fully parameterized — adding new bit-widths or architectures requires no manual Verilog writing.

### 2. Synthesis via Vivado TCL (`vivado/run.tcl`)
The TCL script automates Vivado project creation, sets the Kintex-7 target device, runs synthesis, and exports structured utilization and timing reports. No GUI interaction required.

### 3. Metric Extraction (`scripts/analyze.py`)
Parses Vivado's post-synthesis reports to extract:
- **LUT utilization** (area metric)
- **Critical path delay** (timing metric)

### 4. Visualization (`scripts/plot.py`)
Generates area-delay trade-off plots comparing RCA vs CLA across all bit-widths using Matplotlib.

### 5. Architecture Selection (`scripts/selector.py`)
Rule-based engine that recommends the optimal architecture given a target bit-width and optimization objective (minimize area or minimize delay).

---

## Results

### LUT Usage vs Bit-Width
![LUT vs Bits](results/graphs/lut_vs_bits.png)

### Critical Path Delay vs Bit-Width
![Delay vs Bits](results/graphs/delay_vs_bits.png)

---

## Getting Started

### Prerequisites
- Python 3.8+
- Xilinx Vivado (2020.x or later) with Kintex-7 device support
- Vivado added to system PATH

### Installation

```bash
git clone https://github.com/Bhuvanachandra-kusuma/Intelligent-Parameterized-Digital-Circuit-Generator-for-FPGA-.git
cd Intelligent-Parameterized-Digital-Circuit-Generator-for-FPGA-
pip install -r requirements.txt
```

### Run the Full Pipeline

```bash
# Generate Verilog, run synthesis, extract metrics, plot results
python scripts/run_all.py
```

### Run Individual Steps

```bash
# Generate Verilog RTL only
python generator/generator.py

# Analyze Vivado reports
python scripts/analyze.py

# Generate comparison plots
python scripts/plot.py

# Get architecture recommendation
python scripts/selector.py
```

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Automation, analysis, visualization |
| Xilinx Vivado | Synthesis, static timing analysis |
| Verilog HDL | RTL hardware description |
| TCL scripting | Vivado automation |
| Matplotlib | Result visualization |
| Kintex-7 (xc7k70t) | Target FPGA device |

> **Note:** All synthesis results are post-synthesis hardware metrics targeting the Kintex-7 FPGA. No physical board deployment is required to reproduce the results.

---

## Motivation

This project is inspired by **circuit generator** methodologies used in modern EDA tools — where software automatically produces and evaluates hardware implementations rather than requiring manual RTL authoring for each configuration. The approach is analogous to tools like Fraunhofer IIS's [Intelligent IP](https://www.intelligent-ip.org) for analog circuit generation.

---

## Author

**Bhuvanachandra Kusuma**
M.Sc. Nanoelectronic Systems — Technische Universität Dresden

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/bhuvanachandrakusuma)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/Bhuvanachandra-kusuma)

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
