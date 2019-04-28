# argparse library
from argparse import ArgumentParser
from .laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser(description="Print output of shelves")

    parser.add_argument('chemicalsData', type=str, help="yaml file")
    parser.add_argument('--reactions', '-r', action="store_true",
                        help="only show the number of reations")
    arguments = parser.parse_args()

    shelves = yaml.load(open(f"{arguments.chemicalsData}"))
    lab = Laboratory(shelves['lower'], shelves['upper'], arguments.reactions)

    lab.run_full_experiment(shelves['lower'], shelves['upper'],
                            arguments.reactions)


if __name__ == "__main__":
    process()
