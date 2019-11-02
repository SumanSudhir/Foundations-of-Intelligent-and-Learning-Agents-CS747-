import argparse

import numpy as np
import pandas as pd

ap = argparse.ArgumentParser()

ap.add_argument("-in", "--instance")
ap.add_argument("-al", "--algorithm")
ap.add_argument("-rs", "--randomSeed")
ap.add_argument("-ep", "--epsilon")
ap.add_argument("-hz", "--horizon")

args = vars(ap.parse_args())


class Algorithm:

    def __init__(self, instance, algorithm, randomSeed, epsilon, horizon):
        self.algorithm = algorithm
        self.instance = instance
        self.randomSeed = randomSeed
        self.epsilon = epsilon
        self.horizon = horizon

    def round_robin(self):
        n = 0
        action_value_t = 0
        df = pd.read_csv(self.instance, header=None)
        action_value = np.zeros(len(df))
        for i in range(self.horizon):
            current_arm = i % len(df)
            if i % len(df) == 0:
                n = n + 1
            reward = np.random.binomial(1, df[0][current_arm])
            action_value[current_arm] = action_value[current_arm] + reward
        # print(action_value)
        regret = max(df[0]) * self.horizon - sum(action_value)
        return regret

    def epsilon_greedy(self):
        df = pd.read_csv(self.instance, header=None)
        action_value = np.zeros(len(df))
        action_number = np.arange(len(df))
        arm_count = np.zeros(len(df))
        reward = 0
        for i in range(self.horizon):
            x = np.random.choice(["eps", "eps_conj"], 1,
                                 p=[self.epsilon, 1 - self.epsilon])

            if i < len(df):
                action_value[i] = np.random.binomial(1, df[0][i])
                arm_count[i] = arm_count[i] + 1
                # print(arm_count)

            if(x == "eps" and i >= len(df)):
                y = np.random.choice(action_number)
                arm_count[y] = arm_count[y] + 1
                action_value[y] = (action_value[y] * (arm_count[y] - 1) +
                                   np.random.binomial(1, df[0][y])) / arm_count[y]
                # print(action_value,y)
                # print(arm_count)
            elif x == "eps_conj" and i >= len(df):
                argmax = action_value.argmax(axis=0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = (action_value[argmax] * (arm_count[argmax] - 1) +
                                        np.random.binomial(1, df[0][argmax])) / arm_count[argmax]
                # print(action_value,argmax)
                # print(arm_count)
            # print(x)

        for i in range(len(df)):
            reward = reward + action_value[i] * arm_count[i]
        # print(sum(arm_count))
        regret = max(df[0]) * self.horizon - reward
        return regret

    def UCB(self):
        df = pd.read_csv(self.instance, header=None)
        action_value = np.zeros(len(df))
        arm_count = np.zeros(len(df))
        upper_bound = np.zeros(len(df))
        #t = len(df)
        reward = 0
        for i in range(self.horizon):
            if i < len(df):
                action_value[i] = np.random.binomial(1, df[0][i])
                arm_count[i] = arm_count[i] + 1
                #upper_bound[i] = 0 + action_value[i]

            else:
                for j in range(len(df)):
                    upper_bound[j] = action_value[j] + \
                        np.sqrt(2 * np.log(i + 1) / arm_count[j])

                argmax = upper_bound.argmax(axis=0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = ((action_value[argmax] * (arm_count[argmax] - 1)) +
                                        np.random.binomial(1, df[0][argmax])) / arm_count[argmax]

        for i in range(len(df)):
            # print(arm_count[i],action_value[i])
            reward = reward + action_value[i] * arm_count[i]
        # print(max(df[0])*self.horizon)
        regret = max(df[0]) * self.horizon - reward
        return regret

    def KL_UCB_bound(self, action_value, arm_count, total_count):
        delta = 0.001
        min = action_value
        max = 1
        mid_point = (min + max) / 2
        threhsold = 0.01

        if action_value == 1:
            return 1

        p = action_value
        q = (min + max) / 2
        constant_line = (np.log(total_count) + 3 *
                         np.log(np.log(total_count))) / arm_count
        KL = p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))

        while np.abs(max - min) > threhsold:

            q = (min + max) / 2
            KL = p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))

            if constant_line > KL:
                min = q
            else:
                max = q

        return q

    def KL_UCB(self):
        df = pd.read_csv(self.instance, header=None)
        action_value = np.zeros(len(df))
        arm_count = np.zeros(len(df))
        upper_bound = np.zeros(len(df))
        reward = 0

        for i in range(self.horizon):
            if i < len(df):
                action_value[i] = np.random.binomial(1, df[0][i])
                arm_count[i] = arm_count[i] + 1

                if action_value[i] == 0:
                    action_value[i] = action_value[i] + 0.0001

            else:
                for j in range(len(df)):
                    upper_bound[j] = self.KL_UCB_bound(
                        action_value[j], arm_count[j], i + 1)

                argmax = upper_bound.argmax(axis=0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = ((action_value[argmax] * (arm_count[argmax] - 1)) +
                                        np.random.binomial(1, df[0][argmax])) / arm_count[argmax]

        for i in range(len(df)):
            reward = reward + action_value[i] * arm_count[i]
            # print(max(df[0])*self.horizon)
        regret = max(df[0]) * self.horizon - reward
        return regret

    def thompson_sampling(self):
        df = pd.read_csv(self.instance, header=None)
        success_count = np.zeros(len(df))
        failure_count = np.zeros(len(df))
        reward = np.zeros(len(df))
        arm_count = np.zeros(len(df))
        beta_prob = np.zeros(len(df))

        for i in range(self.horizon):

            for j in range(len(df)):
                beta_prob[j] = np.random.beta(
                    success_count[j] + 1, failure_count[j] + 1)
            if i == 0:
                argmax = np.random.choice(np.arange(len(df)))
            else:
                argmax = beta_prob.argmax(axis=0)

            arm_count[argmax] = arm_count[argmax] + 1
            x = np.random.binomial(1, df[0][argmax])
            reward[argmax] = reward[argmax] + x

            if x == 1:
                success_count[argmax] = success_count[argmax] + 1

            else:
                failure_count[argmax] = failure_count[argmax] + 1

        regret = max(df[0]) * self.horizon - sum(reward)
        return regret


# Output Data get stored in outputData.txt

alg = Algorithm(str(args["instance"]), str(args["algorithm"]),
                int(args["randomSeed"]), float(args["epsilon"]), int(args["horizon"]))

np.random.seed(int(args["randomSeed"]))
if args["algorithm"] == "round-robin":
    regret = alg.round_robin()

elif args["algorithm"] == "epsilon-greedy":
    regret = alg.epsilon_greedy()

elif args["algorithm"] == "ucb":
    regret = alg.UCB()

elif args["algorithm"] == "kl-ucb":
    regret = alg.KL_UCB()

elif args["algorithm"] == "thompson-sampling":
    regret = alg.thompson_sampling()

#file = open("outputData.txt", "a")
output = (str(args["instance"]) + ", " + str(args["algorithm"]) + ", " + str(args["randomSeed"]
                                                                             ) + ", " + str(args["epsilon"]) + ", " + str(args["horizon"]) + ", " + str(regret) + '\n')
print(output)
