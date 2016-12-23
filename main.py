import pickle
import math
from queue import Queue

from CardActions import possible_next_cards, add_card


class Node:
    def __init__(self, depth, parent=None, content=None):
        self.depth = depth
        self.parent = parent
        self.content = content
        self.children = []


def graph_creator(initial_situation, possible_actions_getter, action_applier, max_depth=math.inf):
    first_node = Node(0, None, initial_situation)
    q = Queue()
    q.put(first_node)

    counter = {0:1} #dictionary whete key is a depth level and value is nubber of nodes on this level

    while q.qsize() > 0:
        node = q.get()
        actions = possible_actions_getter(node.content)
        for action in actions:
            new_situation = action_applier(node.content.copy(), action)
            if node.depth + 1 <= max_depth:
                new_node = Node(node.depth + 1, node, new_situation)
                node.children.append(new_node)
                q.put(new_node)

                if node.depth + 1 not in counter:
                    print(node.depth + 1)
                counter[node.depth+1] = counter.get(node.depth+1, 0) + 1


    return first_node, counter


# a, counter = graph_creator([], possible_next_cards, add_card, 7)
