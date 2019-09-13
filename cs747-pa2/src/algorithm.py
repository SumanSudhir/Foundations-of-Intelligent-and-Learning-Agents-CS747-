import argparse

import numpy as np
import pandas as pd
from pulp import *


class MDP:
    def __init__(self, mdp_file, algorithm):
        mdp_file = open(mdp_file, "r")
        self.algorithm = algorithm
        self.number_of_states = int(mdp_file.readline())
        self.number_of_actions = int(mdp_file.readline())
        # self.number_of_actions = int(lines[1])
        # self.task_type = lines[-1]
        # self.discount_factor = lines[-2]

        # self.reward_function = np.loadtxt(
        # mdp_file, skiprows=2, max_rows=self.number_of_states * self.number_of_actions)

        # self.transition_function = np.loadtxt(
        # mdp_file, skiprows=2 + (self.number_of_states * self.number_of_actions),  max_rows=self.number_of_states * self.number_of_actions)
        # print(self.reward_function)
        # print(self.transition_function)
        # print(self.number_of_states, self.number_of_actions, self.task_type)

        # def linear_programmming():
        self.reward = np.zeros(
            (self.number_of_states, self.number_of_actions, self.number_of_states))
        self.transition = np.zeros(
            (self.number_of_states, self.number_of_actions, self.number_of_states))

        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                read_line = mdp_file.readline().split()
                for sPrime in range(self.number_of_states):
                    self.reward[s][a][sPrime] = read_line[sPrime]

        # print(self.reward.shape)

        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                read_line = mdp_file.readline().split()
                for sPrime in range(self.number_of_states):
                    self.transition[s][a][sPrime] = read_line[sPrime]

        # print(self.transition[0][0][0])

        self.discount_factor = float(mdp_file.readline())
        self.task_type = mdp_file.readline()

        # print(self.discount_factor, self.task_type)

    def policy_iteration(self):
        V = np.zeros(self.number_of_states)
        # policy = np.random.choice(
        #     np.arange(self.number_of_actions), self.number_of_states)

        policy = np.zeros(self.number_of_states, dtype=int)
        # print(policy)
        iteration = 0
        while True:
            delta = 0.0
            iteration += 1
            for s in range(self.number_of_states):
                v = V[s]
                v_temp = 0
                for sPrime in range(self.number_of_states):
                    v_temp += self.transition[s][policy[s]][sPrime] * \
                        (self.reward[s][policy[s]][sPrime] +
                         self.discount_factor * V[sPrime])

                V[s] = v_temp
                delta = max(delta, np.abs(v - V[s]))
            # print(V)
            # print(delta)
            if delta < 0.00000000001:
                break

            policy_stable = True

            for s in range(self.number_of_states):
                old_action = policy[s]
                action = np.zeros(self.number_of_actions)
                for a in range(self.number_of_actions):
                    for sPrime in range(self.number_of_states):
                        action[a] += self.transition[s][a][sPrime] * \
                            (self.reward[s][a][sPrime] +
                             self.discount_factor * V[sPrime])

                policy[s] = np.argmax(action)

                # if old_action.all() == policy.all():
                #    policy_stable = True
                # else:
                #    policy_stable = False
            # if policy_stable == True:
            #    break
        print(iteration)
        return V, policy

    def linear_programmming(self):

        prob = LpProblem("lp", LpMinimize)
        var_state = LpVariable.dicts("v", range(self.number_of_states))
        # print(var_state)
        #prob += lpSum([var_state[i]] for i in range(self.number_of_states))
        print(prob)

        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                v = 0
                for sPrime in range(self.number_of_states):

                    v += self.transition[s][a][sPrime] * \
                        (self.reward[s][a][sPrime] +
                         self.discount_factor * var_state[sPrime])

                prob += var_state[s] >= v
                # print(prob)

        prob.solve()
        V = np.array([v.varValue for v in prob.variables()])
        #
        # for s in range(self.number_of_states):
        #     old_action = policy[s]
        #     action = np.zeros(self.number_of_actions)
        #     for a in range(self.number_of_actions):
        #         for sPrime in range(self.number_of_states):
        #             action[a] += self.transition[s][a][sPrime] * \
        #                 (self.reward[s][a][sPrime] +
        #                  self.discount_factor * V[sPrime])
        #
        #     policy[s] = np.argmax(action)

        print(V)
        return V


x = MDP("/home/sudhirsuman/Desktop/7thSemester/CS747/Assignment/cs747-pa2/data/continuing/MDP10.txt", 'lp')
# y, a = x.policy_iteration()
# print(y)
# print(a)

v = x.linear_programmming()
