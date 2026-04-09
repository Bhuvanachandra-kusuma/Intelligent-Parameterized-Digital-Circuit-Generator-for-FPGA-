def generate_adder(n_bits, arch):
    import os
    os.makedirs("generated", exist_ok=True)

    filename = f"generated/adder_{n_bits}_{arch}.v"

    with open(filename, "w") as f:
        f.write(f"""
module adder_{n_bits}_{arch}(
    input [{n_bits-1}:0] A,
    input [{n_bits-1}:0] B,
    output [{n_bits-1}:0] SUM
);

assign SUM = A + B;

endmodule
""")

    print(f"Generated: {filename}")



if __name__ == "__main__":
    for bits in [4, 8, 16]:
        for arch in ["rca", "cla"]:
            generate_adder(bits, arch)
