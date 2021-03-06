import argparse

import pandas as pd
import numpy as np


ap = argparse.ArgumentParser()

ap.add_argument("--dataFileName")

args = ap.parse_args()

states = []
action = []
reward = []

def value_function(dataFileName):
    data_file = open(dataFileName, "r")
    with open(dataFileName) as f:
        for i, l in enumerate(f):
            pass
    episode = i - 3

    number_of_states = int(data_file.readline())
    number_of_actions = int(data_file.readline())
    discount_factor = float(data_file.readline())

    for i in range(episode):
        read_line = data_file.readline().split()
        states.append(int(read_line[0]))
        action.append(int(read_line[1]))
        reward.append(float(read_line[2]))

    n_plus_state = data_file.readline()
    states.append(int(n_plus_state))
    alpha = 100.0/episode
    prev_value = [0]*number_of_states
    value = [0]*number_of_states
    diff = np.inf
    m = 0

    while(diff > 10**(-7) and m < 150):
        state_count = [0]*number_of_states
        for i in range(episode):
            state_count[states[i]] += 1
            value[states[i]] += (1.0/state_count[states[i]])*(reward[i] + discount_factor*value[states[i+1]] - value[states[i]])

        diff = 0

        for j in range(number_of_states):
            diff += np.abs(prev_value[j] - value[j])
            prev_value[j] = value[j]

        m += 1
    for element in value:
        print(element)

value = value_function(args.dataFileName)
