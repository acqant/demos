# This is the main script
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--arrays1", help="increase output verbosity", action="store_true")
parser.add_argument("--arrays2", help="increase output verbosity", action="store_true")
parser.add_argument("--dict1", help="increase output verbosity", action="store_true")
args = parser.parse_args()


def main():
    print("We are in the main def now...Hello...")
    import array_loops_n_more
    import arrays_example
    import dict_example

    if args.arrays1:
        arrays_example.simple_arrays()
    if args.arrays2:
        array_loops_n_more.demo_looping_arrays()
    if args.dict1:
        dict_example.simple_dict()


if __name__ == '__main__':
    print("We are being called from the script cause - __name__ == __main__")
    main()
