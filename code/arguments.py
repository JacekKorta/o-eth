import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Handle JD translation sheets")
    parser.add_argument("-m", "--mode", choices=["translate", "colour"])
    parser.add_argument("-t", "--translate", type=bool, default=True, help="Run translate mode")
    args = parser.parse_args()
    return args
