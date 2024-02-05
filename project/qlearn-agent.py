from environment import Environment
from agent import Agent
from experience_replay import ExperienceReplay
import time

import warnings
import logging, os


if __name__ == '__main__':

    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    grid_size = 3

    environment = Environment(grid_size=grid_size, render_on=True)
    agent = Agent(grid_size=grid_size, epsilon=1, epsilon_decay=0.998, epsilon_end=0.01)
    #agent.load(f'models/model_{grid_size}.h5')

    experience_replay = ExperienceReplay(capacity=10000, batch_size=32)
    
    # Number of episodes to run before training stops
    episodes = 3 #5000
    # Max number of steps in each episode
    max_steps = 50

    print('=== init ===')
    print('agent location ', environment.agent_location)
    print('goal  location ', environment.goal_location)

    for episode in range(episodes):

        # Get the initial state of the environment and set done to False
        state = environment.reset()
        print('===================')
        print('agent location ', environment.agent_location)
        print('goal  location ', environment.goal_location)

        # Loop until the episode finishes
        for step in range(max_steps):
            #print('Episode:', episode)
            #print('Step:', step)
            #print('Epsilon:', agent.epsilon)

            # Get the action choice from the agents policy
            #print('state ', state)
            action = agent.get_action(state)
            print('action ', action)

            # Take a step in the environment and save the experience
            reward, next_state, done = environment.step(action)
            experience_replay.add_experience(state, action, reward, next_state, done)

            print('reward ', reward)  
            # If the experience replay has enough memory to provide a sample, train the agent
            if experience_replay.can_provide_sample():
                experiences = experience_replay.sample_batch()
                print('Episode:', episode)
                print('Step:', step)
                print('experiences ', experiences)
                agent.learn(experiences)

            # Set the state to the next_state
            state = next_state
            print('next state ', next_state)
            if done:
                print('=== done ========')
                print('Episode:', episode)
                print('Step:', step)

                print('agent location ', environment.agent_location)
                print('goal  location ', environment.goal_location)
               
                break
            
            # Optionally, pause for half a second to evaluate the model
            # time.sleep(0.5)

        agent.save(f'models/model_{grid_size}.h5')