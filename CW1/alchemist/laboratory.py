import random


class Laboratory(object):

    """ Generate the final contents of the shelves post experiment, and a
    string describing the contents, along with the number of reactions.

    Parameters
    ----------
    shelf1: list
        contents of the lower shelf
    shelf2: list
        contents of the upper shelf
    reations: bool
        If true, print only the number of reactions. If false print the number
        of reations followed by the final contents of the shelves

    Returns
    -------
    string
        number of reations with the option of the final state of the shelves
    """

    def __init__(self, shelf1, shelf2, reactions=False):
        self.shelf1 = shelf1
        self.shelf2 = shelf2
        self.reactions = reactions

    def can_react(self, substance1, substance2):
        condition1 = (substance1 == "anti" + substance2)
        condition2 = (substance2 == "anti" + substance1)
        return condition1 or condition2

    def update_shelves(self, shelf1, shelf2, substance1, substance2_index):
        index1 = self.shelf1.index(substance1)
        self.shelf1 = self.shelf1[:index1] + self.shelf1[index1 + 1:]
        self.shelf2 = (self.shelf2[:substance2_index] + self.shelf2
                       [substance2_index + 1:])
        return self.shelf1, self.shelf2

    def do_a_reaction(self, shelf1, shelf2):
        for substance1 in self.shelf1:
            possible_targets = [i for i, target in enumerate(self.shelf2) if
                                self.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(shelf1, shelf2, substance1,
                                           substance2_index)
        return self.shelf1, self.shelf2

    def run_full_experiment(self, shelf1, shelf2, reactions=False):
        count = 0
        ended = False
        self.shelf2 = sorted(shelf2)     # prevents randomisation failing tests
        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        if self.reactions:
            output = count
        else:
            output = ("lower: [%s]\nupper: [%s]"
                      % (', '.join(map(str, shelf1)),
                         ', '.join(map(str, shelf2))))
        print(output)
        return output
