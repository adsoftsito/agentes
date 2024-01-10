class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return f"State: {self.state} Action: {self.action}\n"

"""
class Environment:
    def __init__(self, ...):
        self.start = 
        self.goal = 
"""

class SearchAgent:
    def __init__(self.environment):
        self.frontier = [Node(state=environent.start)]
        self.explored = set()
        self.goal_state = environment.goal

    def is_frontier_empty(self):
        return len(self.frontier) == 0

    def remove_node(self):

    def is_goal(self.node):
        if node.state == self.goal_state:
            self.solution = []
            while node.parent in not None:
               self.solution.append(node)
               print(f"{node.state}({node.action)")
               node = node.parent
            
            raise Exception("Solution found !!!")


    def add_to_explored(self.node):

    def expand_node(self.node):


    def solve(self):
        while not self.is_frontier_empty():
            node = self.remove_node()
            try:
                self.is_goal(node)
            except:
                return self.solution

            self.add_to_explored(node)
            self.expand_node(node)


n = Node([1, 2, 3, 4])
print(n)
