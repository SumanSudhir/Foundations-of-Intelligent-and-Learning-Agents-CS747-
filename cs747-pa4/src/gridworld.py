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

        read_line = env_file.readline()
        self.episode = int(read_line)


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

        next_state_row += int(self.wind_strength[current_state_colm])

        if next_state_row > self.number_of_rows-1:
            next_state_row = self.number_of_rows-1

        return next_state_row, next_state_colm


    # def state_transition(self,current_state_row, current_state_colm, current_action):
    #     """ right = 0, up = 1, left = 2, down = 3, up-right = 4, up-left = 5
    #         down-left = 6, down-right = 7
    #     """
    #     next_state_row = current_state_row
    #     next_state_colm = current_state_colm
    #
    #     if current_action == 0:
    #         next_state_colm += 1
    #
    #     elif current_action == 1:
    #         next_state_row += 1
    #
    #     elif current_action == 2:
    #         next_state_colm -= 1
    #
    #     elif current_action == 3:
    #         next_state_row -= 1
    #
    #     elif current_action == 4:
    #         next_state_colm += 1
    #         next_state_row += 1
    #
    #     elif current_action == 5:
    #         next_state_colm -= 1
    #         next_state_row += 1
    #
    #     elif current_action == 6:
    #         next_state_colm -= 1
    #         next_state_row -= 1
    #
    #     elif current_action == 7:
    #         next_state_colm += 1
    #         next_state_row -= 1
    #
    #     next_state_row += int(self.wind_strength[current_state_colm])
    #
    #     if next_state_row < 0:
    #         next_state_row = 0
    #
    #     if next_state_colm < 0:
    #         next_state_colm = 0
    #
    #     if next_state_row > self.number_of_rows-1:
    #         next_state_row = self.number_of_rows-1
    #
    #     if next_state_colm > self.number_of_colms-1:
    #         next_state_colm = self.number_of_colms-1
    #
    #     return next_state_row, next_state_colm

    def epsilon_greddy(self,value,current_row,current_colm):

        action_number = np.arange(self.number_of_actions)
        action_value = np.zeros(self.number_of_actions)

        x = np.random.choice(["eps", "eps_conj"], 1, p=[self.epsilon, 1 - self.epsilon])

        """Explore"""
        if x == "eps" or value.all() == 0:
            action = np.random.choice(action_number)

        """Exploit"""

        if x == "eps_conj":
            for a in action_number:
                action_value[a] = value[current_row][current_colm][a]

            action = np.argmax(action_value)

        #print(action)
        return action


    def Sarsa(self):
        value = np.zeros((self.number_of_rows, self.number_of_colms, self.number_of_actions))

        iteration = 0
        for i in range(self.episode):
            current_row = self.start_row
            current_colm = self.start_colm

            action = self.epsilon_greddy(value, current_row, current_colm)

            while(current_row != self.target_row or current_colm != self.target_colm):
                reward = -1
                next_row, next_colm = self.state_transition(current_row, current_colm, action)
                next_action = self.epsilon_greddy(value, next_row, next_colm)
                #print(next_action)
                value[current_row][current_colm][action] += self.alpha*(reward + self.decay_factor*value[next_row][next_colm][next_action] - value[current_row][current_colm][action])

                current_row = next_row
                current_colm = next_colm
                action = next_action
                iteration += 1
                #print(value)
                print(current_row, current_colm, action)

        return iteration

cls = windyGridWorld("grid_world_env.txt")
# cls.epsilon_greddy()
# y,x = cls.state_transition(5,2,0)
t = cls.Sarsa()
print(t)
