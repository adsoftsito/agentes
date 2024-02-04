import random
import numpy as np

class Environment:
    def __init__(self, grid_size, render_on=False):
        self.grid_size = grid_size
        self.grid = []
        self.render_on = render_on
        self.agent_location = None
        self.goal_location = None

    def reset(self):
        # Initialize the empty grid as a 2d array of 0s
        self.grid = np.zeros((self.grid_size, self.grid_size))

        # Add the agent and the goal to the grid
        self.agent_location = self.add_agent()
        self.goal_location = self.add_goal()

        if self.render_on:
            self.render()

        # Return the initial state of the grid
        return self.get_state()

    def add_agent(self):
        # Choose a random location
        location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

        # Agent is represented by a 1
        self.grid[location[0]][location[1]] = 1

        return location

    def add_goal(self):
        # Choose a random location
        location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

        # Get a random location until it is not occupied
        while self.grid[location[0]][location[1]] == 1:
            location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
           
        # Goal is represented by a -1
        self.grid[location[0]][location[1]] = -1

        return location
      
    def render(self):
        # Convert to a list of ints to improve formatting
        grid = self.grid.astype(int).tolist()

        for row in grid:
            print(row)
        print('') # To add some space between renders for each step
      
    def get_state(self):
        # Flatten the grid from 2d to 1d
        state = self.grid.flatten()
        return state

env = Environment(5, render_on=True)
env.reset()

print(f'Agent Location: {env.agent_location}')
print(f'Goal Location: {env.goal_location}')
