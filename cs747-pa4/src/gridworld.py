import argparse
import sys

import numpy as np



class windyGridWorld:

    def __init__(self,env_file):
        env_file = open(env_file,"r")

        read_line = env_file.readline().split()
        self.number_of_rows = read_line[0]
        self.number_of_colms = read_line[1]

        read_line = env_file.readline().split()
        self.start_row = read_line[0]
        self.start_colm = read_line[1]

        read_line = env_file.readline().split()
        self.target_row = read_line[0]
        self.target_colm = read_line[1]

        read_line = env_file.readline().split()
        self.wind_strength = read_line

        read_line = env_file.readline()
        self.wind_nature = read_line

        read_line = env_file.readline()
        self.number_of_actions = read_line

        read_line = env_file.readline()
        self.epsilon = read_line

        read_line = env_file.readline()
        self.alpha = read_line

        read_line = env_file.readline()
        self.decay_factor = read_line


    def epsilon_greddy(self):
        print(self.epsilon)



cls = windyGridWorld("grid_world_env.txt")
cls.epsilon_greddy()




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
