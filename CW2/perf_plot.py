import numpy as np
from matplotlib import pyplot as plt
from tree import update_branch_end
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

    return repeat(totime, number=100)


def plot_time(function, counts, title=None):
    plt.plot(counts, list(map(function, counts)))
    plt.ylim(bottom=0)
    plt.xlim(left=0)
    plt.ylabel('seconds')
    plt.xlabel('number of iteration steps completed')
    plt.title('time to run refactored tree.py script')


counts = np.arange(1, 16, 1)
plot_time(time_tree, counts)

plt.savefig('perf_plot.png')
