import os
import re

RESULTS_DIR = "results"


def extract_luts(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()

        # Match LUT count
        match = re.search(r'\|\s*LUT.*?\|\s*(\d+)', text)
        if match:
            return int(match.group(1))

        return None
    except:
        return None


def extract_delay(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()

        # Match: Data Path Delay:        5.141ns
        match = re.search(r'Data Path Delay:\s+([\d\.]+)ns', text)
        if match:
            return float(match.group(1))

        return None
    except:
        return None


def analyze():
    print("\n FULL DESIGN COMPARISON\n")

    for bits in [4, 8, 16]:
        print(f"🔎 {bits}-bit:")

        # File names
        util_rca = f"{RESULTS_DIR}/util_adder_{bits}_rca.txt"
        util_cla = f"{RESULTS_DIR}/util_adder_{bits}_cla.txt"

        timing_rca = f"{RESULTS_DIR}/timing_adder_{bits}_rca.txt"
        timing_cla = f"{RESULTS_DIR}/timing_adder_{bits}_cla.txt"

        # Extract values
        rca_luts = extract_luts(util_rca)
        cla_luts = extract_luts(util_cla)

        rca_delay = extract_delay(timing_rca)
        cla_delay = extract_delay(timing_cla)

        # Print results
        print(f"RCA → LUTs: {rca_luts}, Delay: {rca_delay}")
        print(f"CLA → LUTs: {cla_luts}, Delay: {cla_delay}")
        print()

def get_data(bits):
    RESULTS_DIR = "results"

    util_rca = f"{RESULTS_DIR}/util_adder_{bits}_rca.txt"
    util_cla = f"{RESULTS_DIR}/util_adder_{bits}_cla.txt"

    timing_rca = f"{RESULTS_DIR}/timing_adder_{bits}_rca.txt"
    timing_cla = f"{RESULTS_DIR}/timing_adder_{bits}_cla.txt"

    rca_luts = extract_luts(util_rca)
    cla_luts = extract_luts(util_cla)

    rca_delay = extract_delay(timing_rca)
    cla_delay = extract_delay(timing_cla)

    return {
        "rca": (rca_luts, rca_delay),
        "cla": (cla_luts, cla_delay)
    }


if __name__ == "__main__":
    analyze()
