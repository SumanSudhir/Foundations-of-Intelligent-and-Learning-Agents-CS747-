import argparse
import sys

import numpy as np



class windyGridWorld:

    def __init__(self,env_file):
        env_file = open(env_file,"r")

        read_line = env_file.readline().split()
        self.number_of_rows = int(read_line[0])
        self.number_of_colms = int(read_line[1])

        read_line = env_file.readline().split()
        self.start_row = int(read_line[0])
        self.start_colm = int(read_line[1])

        read_line = env_file.readline().split()
        self.target_row = int(read_line[0])
        self.target_colm = int(read_line[1])

        read_line = env_file.readline().split()
        self.wind_strength = read_line

        read_line = env_file.readline()
        self.wind_nature = int(read_line)

        read_line = env_file.readline()
        self.number_of_actions = int(read_line)

        read_line = env_file.readline()
        self.epsilon = float(read_line)

        read_line = env_file.readline()
        self.alpha = float(read_line)

        read_line = env_file.readline()
        self.decay_factor = float(read_line)


    def epsilon_greddy(self):
        print(self.epsilon)



    def state_transition(self,current_state_row, current_state_colm, current_action):
        """ right = 0, up = 1, left = 2, down = 3, up-right = 4, up-left = 5
            down-left = 6, down-right = 7
        """
        next_state_row = current_state_row
        next_state_colm = current_state_colm


        if current_action == 0 and current_state_colm < self.number_of_colms-1:
            next_state_colm += 1

        elif current_action == 1 and current_state_row < self.number_of_rows-1:
            next_state_row += 1

        elif current_action == 2 and current_state_colm > 0:
            next_state_colm -= 1

        elif current_action == 3 and current_state_row > 0:
            next_state_row -= 1

        elif current_action == 4 and current_state_colm < self.number_of_colms-1 and current_state_row < self.number_of_rows-1:
            next_state_colm += 1
            next_state_row += 1

        elif current_action == 5 and current_state_colm > 0 and current_state_row < self.number_of_rows-1:
            next_state_colm -= 1
            next_state_row += 1

        elif current_action == 6 and current_state_colm > 0 and current_state_row > 0:
            next_state_colm -= 1
            next_state_row -= 1

        elif current_action == 7 and current_state_colm < self.number_of_colms-1 and current_state_row > 0:
            next_state_colm += 1
            next_state_row -= 1

        next_state_row += int(self.wind_strength[current_state_row])

        return next_state_row, next_state_colm



cls = windyGridWorld("grid_world_env.txt")
# cls.epsilon_greddy()
y,x = cls.state_transition(5,2,0)
print(y,x)






# def reward_function(num_state,num_action):
#
#     reward = np.zeros((num_state, num_action, num_state))
#     transition = np.zeros((num_state, num_action, num_state))
#
#     for s in range(num_state):
#         for a in range(num_action):
#             for sPrime in range(num_state):
#
#
#
#
#     for s in range(num_state):
#         for a in range(num_action):
#             for sPrime in range(num_state):
