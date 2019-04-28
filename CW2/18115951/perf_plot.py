import numpy as np
from matplotlib import pyplot as plt
from tree import update_branch_end
from tree_np import update_branch_np
from timeit import repeat
import yaml


def time_tree(count):

    def totime():
        tree = yaml.load(open("config.yml"))
        for i in range(count):
            tree["branch"]["end"] = []
            for j in range(len(tree["branch"]["start"])):
                tree["branch"]["end"] = update_branch_end(tree["branch"], j)
            tree["branch"]["start"] = tree["branch"]["end"]
            tree["branch"]["length"] *= tree["scale"]

    return repeat(totime, number=10)


def time_tree_np(count):

    def totime_np():
        tree = yaml.load(open("config.yml"))
        angles = np.array(0)
        x_end = np.array(0)
        y_end = np.array(1)
        plt.plot([0, 0], [x_end, y_end])
        for i in range(count):
            [x_start, y_start, x_end, y_end,
             angles] = update_branch_np(tree["branch"], angles, x_end, y_end)
            tree["branch"]["length"] *= tree["scale"]

    return repeat(totime_np, number=10)


def plot_time(function, counts, title=None):
    plt.plot(counts, list(map(function, counts)))
    plt.ylim(bottom=0)
    plt.xlim(left=0)
    plt.ylabel('seconds')
    plt.xlabel('number of iteration steps completed')
    plt.title('time to run tree.py and tree_np.py')


counts = np.arange(1, 21, 1)
plot_time(time_tree, counts)
plot_time(time_tree_np, counts)
plt.savefig('perf_plot.png')
