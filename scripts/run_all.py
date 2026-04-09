from run_vivado import run_vivado

for bits in [4, 8, 16]:
    for arch in ["rca", "cla"]:
        file = f"generated/adder_{bits}_{arch}.v"
        top = f"adder_{bits}_{arch}"
        print(f"Running Vivado for {file}")
        run_vivado(file, top)
