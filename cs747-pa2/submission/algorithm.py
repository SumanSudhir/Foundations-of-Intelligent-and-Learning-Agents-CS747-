import argparse
import sys

import numpy as np
import pandas as pd
from pulp import *

ap = argparse.ArgumentParser()

ap.add_argument("--mdp")
ap.add_argument("--algorithm")

args = ap.parse_args()


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
        # self.discount_factor = 1

        # print(self.discount_factor, self.task_type)

    def policy_iteration_by_converging(self):
        V = np.zeros(self.number_of_states)
        # policy = np.random.choice(
        #     np.arange(self.number_of_actions), self.number_of_states)
        policy = np.zeros(self.number_of_states, dtype=int)
        new_policy = np.zeros(self.number_of_states, dtype=int)
        # print(policy)
        iteration = 0
        while True:
            i = 0
            iteration = iteration + 1
            while True:
                delta = 0.0
                # iteration += 1
                for s in range(self.number_of_states):
                    v = V[s]
                    v_temp = 0
                    for sPrime in range(self.number_of_states):
                        v_temp += self.transition[s][policy[s]][sPrime] * \
                            (self.reward[s][policy[s]][sPrime] +
                             self.discount_factor * V[sPrime])

                    V[s] = v_temp
                    delta = max(delta, np.abs(v - V[s]))

                if delta < 0.00000001:
                    break
            # print(V)
            # print(delta)

            for s in range(self.number_of_states):
                old_action = policy[s]
                action = np.zeros(self.number_of_actions)
                for a in range(self.number_of_actions):
                    for sPrime in range(self.number_of_states):
                        action[a] += self.transition[s][a][sPrime] * \
                            (self.reward[s][a][sPrime] +
                             self.discount_factor * V[sPrime])

                new_policy[s] = np.argmax(action)

                if policy[s] != new_policy[s]:
                    policy[s] = new_policy[s]
                    i = i + 1

            if i == 0:
                break
            # if old_action.all() == policy.all():
            #    policy_stable = True
            # else:
            #    policy_stable = False
            # if policy_stable == True:
            #    break
        # print(iteration)
        return V, policy

    def policy_iteration_by_linear_equation(self):
        policy = np.zeros(self.number_of_states, dtype=int)
        new_policy = np.zeros(self.number_of_states, dtype=int)
        V = np.zeros(self.number_of_states)
        # prob = LpProblem("lp", LpMinimize)
        # var_state = LpVariable.dicts("V", range(self.number_of_states))

        while True:
            prob = LpProblem("lp", LpMinimize)
            var_state = LpVariable.dicts("V", range(self.number_of_states))
            prob += lpSum([var_state[i] for i in range(self.number_of_states)])
            i = 0
            # policy = new_policy.copy()
            # print(policy)
            for s in range(self.number_of_states):
                v_temp = 0
                for sPrime in range(self.number_of_states):
                    v_temp += self.transition[s][policy[s]][sPrime] * (
                        self.reward[s][policy[s]][sPrime] + self.discount_factor * var_state[sPrime])

                prob += var_state[s] == v_temp

            prob.solve()
            V = np.array([v.varValue for v in prob.variables()])

            for s in range(self.number_of_states):
                V_temp = np.zeros(self.number_of_actions)
                for a in range(self.number_of_actions):
                    v_temp = 0
                    for sPrime in range(self.number_of_states):
                        v_temp += self.transition[s][a][sPrime] * (
                            self.reward[s][a][sPrime] + self.discount_factor * V[sPrime])

                    V_temp[a] = v_temp

                new_policy[s] = np.argmax(V_temp)
                if policy[s] != new_policy[s]:
                    policy[s] = new_policy[s]
                    i = i + 1

            # if policy.all() == new_policy.all():
            #    break
            # print(policy)
            # # print(policy)
            # print(policy)
            # print(new_policy)
            if i == 0:
                break

        # print(len(V))
        return V, policy

    def linear_programmming(self):

        policy = np.zeros(self.number_of_states, dtype=int)
        prob = LpProblem("lp", LpMinimize)
        var_state = LpVariable.dicts("v", range(self.number_of_states))

        prob += lpSum([var_state[i] for i in range(self.number_of_states)])
        # print(var_state)
        #prob += lpSum([var_state[i]] for i in range(self.number_of_states))
        # print(prob)
        for s in range(self.number_of_states):
            for a in range(self.number_of_actions):
                v_temp = 0
                for sPrime in range(self.number_of_states):
                    v_temp += self.transition[s][a][sPrime] * \
                        (self.reward[s][a][sPrime] +
                         self.discount_factor * var_state[sPrime])

                prob += var_state[s] >= v_temp
                # print(prob)

        prob.solve()
        V = np.array([v.varValue for v in prob.variables()])

        for s in range(self.number_of_states):
            V_temp = np.zeros(self.number_of_actions)
            for a in range(self.number_of_actions):
                v_temp = 0
                for sPrime in range(self.number_of_states):
                    v_temp += self.transition[s][a][sPrime] * (
                        self.reward[s][a][sPrime] + self.discount_factor * V[sPrime])

                V_temp[a] = v_temp

            policy[s] = np.argmax(V_temp)

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

        # print(V)
        return V, policy


# x = MDP("/home/sudhirsuman/Desktop/7thSemester/CS747/Assignment/cs747-pa2/data/episodic/MDP10.txt", 'lp')
# y, p = x.policy_iteration_by_linear_equation()
# print(y)
# print(p)
#
# v, p = x.linear_programmming()
# print(v)
# print(p)

alg = MDP(args.mdp, args.algorithm)

if args.algorithm == "hpi":
    #value, action = alg.policy_iteration_by_linear_equation()
    value, action = alg.policy_iteration_by_converging()

elif args.algorithm == "lp":
    value, action = alg.linear_programmming()

for i in range(len(value)):
    sys.stdout.write(str(value[i]) + "\t" + str(action[i]) + "\n")
    # sys.stdout.write("%.10f\n" % value[i])
