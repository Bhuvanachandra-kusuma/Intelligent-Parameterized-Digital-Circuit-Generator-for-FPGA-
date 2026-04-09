# Intelligent-Parameterized-Digital-Circuit-Generator-for-FPGA-





# FPGA Adder Design Space Exploration Tool

## Overview
This project implements an automated FPGA design exploration framework using Python and Vivado.

It generates, synthesizes, and compares different adder architectures:
- Ripple Carry Adder (RCA)
- Carry Lookahead Adder (CLA)

## Features
- Parameterized Verilog generation
- Automated Vivado synthesis (TCL)
- Area (LUT) and timing extraction
- Architecture comparison
- Visualization of results
- Smart architecture selection

## Results
- RCA achieved ~43% lower LUT usage compared to CLA (16-bit)
- RCA achieved ~10% lower delay on FPGA
- Demonstrates FPGA carry-chain optimization advantage

## Tools Used
- Vivado (Kintex-7 xc7k70t)
- Python (Automation + Analysis)
- Matplotlib (Visualization)

## How to Run

```bash
python scripts/run_all.py
python scripts/analyze.py
python scripts/plot.py
python scripts/selector.py
