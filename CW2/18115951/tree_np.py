from matplotlib import pyplot as plt
import numpy as np
import yaml
from argparse import ArgumentParser


def update_branch_np(branch, angles, x_end, y_end):
    l_angles = angles - branch["angle"]
    r_angles = angles + branch["angle"]
    angles = np.hstack((l_angles, r_angles))
    x_start = np.hstack((x_end, x_end))
    y_start = np.hstack((y_end, y_end))
    x_end = x_start + branch["length"]*np.sin(angles)
    y_end = y_start + branch["length"]*np.cos(angles)
    return [x_start, y_start, x_end, y_end, angles]


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

    angles = np.array(0)
    x_end = np.array(0)
    y_end = np.array(1)
    plt.plot([0, 0], [x_end, y_end])

    for i in range(tree["iterations"]):
        [x_start, y_start, x_end, y_end,
         angles] = update_branch_np(tree["branch"], angles, x_end, y_end)
        plt.plot([x_start, x_end], [y_start, y_end])
        tree["branch"]["length"] *= tree["scale"]

    plt.savefig('tree_np.png')


if __name__ == "__main__":
    process()
