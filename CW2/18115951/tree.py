from math import sin, cos
from matplotlib import pyplot as plt
import yaml
from argparse import ArgumentParser


def update_branch_end(branch, j):
    for sgn in range(-1, 3, 2):
        theta = branch["start"][j][2] + sgn*branch["angle"]
        x = (branch["start"][j][0] + branch["length"]*sin(theta))
        y = (branch["start"][j][1] + branch["length"]*cos(theta))
        branch["end"].append([x, y, theta])
    return branch["end"]


def update_plot(branch, j, i):
    for i in range(-2, 0):
        plt.plot([branch["start"][j][0], branch["end"][i][0]],
                 [branch["start"][j][1], branch["end"][i][1]])


def process():
    parser = ArgumentParser(description="find the tree of life structure.")
    parser.add_argument('--length', default=1, type=float,
                        help="length of inital branch")
    parser.add_argument('--angle', default=0.05, type=float,
                        help="angle of separation between branches")
    parser.add_argument('--scale', default=0.5, type=float,
                        help="scale down of branch length per iteration")
    parser.add_argument('--iterations', default=4, type=int,
                        help="number of iterations")
    args = parser.parse_args()

    tree = yaml.load(open("config.yml"))
    tree["branch"]["length"] = args.length
    tree["branch"]["angle"] = args.angle
    tree["scale"] = args.scale
    tree["iterations"] = args.iterations

    plt.plot([0, 0], [0, 1])

    for i in range(tree["iterations"]):
        tree["branch"]["end"] = []
        for j in range(len(tree["branch"]["start"])):
            tree["branch"]["end"] = update_branch_end(tree["branch"], j)
            update_plot(tree["branch"], j, i)
        tree["branch"]["start"] = tree["branch"]["end"]
        tree["branch"]["length"] *= tree["scale"]

    plt.savefig('tree.png')


if __name__ == "__main__":
    process()
