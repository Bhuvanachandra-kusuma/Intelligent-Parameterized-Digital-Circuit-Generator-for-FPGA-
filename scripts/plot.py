import matplotlib.pyplot as plt
import analyze


def plot_results():
    bits_list = [4, 8, 16]

    rca_luts = []
    cla_luts = []

    rca_delay = []
    cla_delay = []

    # Collect data
    for bits in bits_list:
        data = analyze.get_data(bits)

        rca_lut, rca_del = data["rca"]
        cla_lut, cla_del = data["cla"]

        rca_luts.append(rca_lut)
        cla_luts.append(cla_lut)

        rca_delay.append(rca_del)
        cla_delay.append(cla_del)

    #  Plot 1: LUT Comparison
    plt.figure()
    plt.plot(bits_list, rca_luts, marker='o', label='RCA')
    plt.plot(bits_list, cla_luts, marker='o', label='CLA')
    plt.title("LUT Usage vs Bit Width")
    plt.xlabel("Bit Width")
    plt.ylabel("Number of LUTs")
    plt.legend()
    plt.grid()
    plt.savefig("luts.png")

    #  Plot 2: Delay Comparison
    plt.figure()
    plt.plot(bits_list, rca_delay, marker='o', label='RCA')
    plt.plot(bits_list, cla_delay, marker='o', label='CLA')
    plt.title("Delay vs Bit Width")
    plt.xlabel("Bit Width")
    plt.ylabel("Delay (ns)")
    plt.legend()
    plt.grid()
    plt.savefig("delay.png")


if __name__ == "__main__":
    plot_results()
