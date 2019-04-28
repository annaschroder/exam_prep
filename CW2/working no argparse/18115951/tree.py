from math import sin, cos
from matplotlib import pyplot as plt
import yaml


def update_branch_end(branch, j):
    for sgn in range(-1, 3, 2):
        x = (branch["start"][j][0] +
             branch["length"]*sin(branch["start"][j][2] + sgn*branch["angle"]))
        y = (branch["start"][j][1] +
             branch["length"]*cos(branch["start"][j][2] + sgn*branch["angle"]))
        theta = branch["start"][j][2] + sgn*branch["angle"]
        branch["end"].append([x, y, theta])
    return branch["end"]


def update_plot(branch, j, i):
    for i in range(-2, 0):
        plt.plot([branch["start"][j][0], branch["end"][i][0]],
                 [branch["start"][j][1], branch["end"][i][1]])


tree = yaml.load(open("config.yml"))

plt.plot([0, 0], [0, 1])

for i in range(tree["iterations"]):
    tree["branch"]["end"] = []
    for j in range(len(tree["branch"]["start"])):
        tree["branch"]["end"] = update_branch_end(tree["branch"], j)
        update_plot(tree["branch"], j, i)
    tree["branch"]["start"] = tree["branch"]["end"]
    tree["branch"]["length"] *= tree["scale"]
plt.savefig('tree.png')
