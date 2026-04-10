import analyze

def choose_best(luts_rca, delay_rca, luts_cla, delay_cla):
    score_rca = luts_rca + delay_rca
    score_cla = luts_cla + delay_cla

    if score_rca < score_cla:
        return "RCA"
    else:
        return "CLA"


def main():
    print("\n SMART ARCHITECTURE SELECTION\n")

    for bits in [4, 8, 16]:
        print(f"{bits}-bit:")

        # Hardcoded for now (later we automate)
        data = analyze.get_data(bits)

        rca_luts, rca_delay = data["rca"]
        cla_luts, cla_delay = data["cla"]

        best = choose_best(rca_luts, rca_delay, cla_luts, cla_delay)

        print(f"Best Architecture: {best}\n")


if __name__ == "__main__":
    main()
