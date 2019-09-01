import pandas as pd
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("in", "--instance" )
ap.add_argument("al", "--algorithm" )
ap.add_argument("rs", "--randomSeed")
ap.add_argument("ep", "--epsilon")
ap.add_argument("hz", "--horizon")

args = vars(ap.parse_args())


class Algorithm:

    def __init__(self, instance, algorithm, randomSeed, epsilon, horizon):
        self.algorithm = algorithm
        self.instance = instance
        self.randomSeed = randomSeed
        self.epsilon = epsilon
        self.horizon = horizon
        np.random.seed(randomSeed)

    def round_robin():
        n = 0
        action_value_t = 0
        df = pd.read_csv(instance, header=None)
        action_value = np.zeros(len(df))
        for i in range(horizon):
            current_arm = i%len(df)
            if i%len(df) == 0:
                n = n+1
            reward = np.random.binomial(1,df[0][current_arm])
            action_value[current_arm] = action_value[current_arm] + reward
        #print(action_value)
        regret = max(df[0])*horizon - sum(action_value)
        return regret


    def epsilon_greedy():
        df = pd.read_csv(instance,header=None)
        action_value = np.zeros(len(df))
        action_number = np.arange(len(df))
        arm_count = np.zeros(len(df))
        reward = 0
        for i in range(horizon):
            x = np.random.choice(["eps","eps_conj"],1,p = [epsilon, 1-epsilon])

            if i<len(df):
                action_value[i] = np.random.binomial(1,df[0][i])
                arm_count[i] = arm_count[i] + 1
                #print(arm_count)

            if(x == "eps" and i>=len(df)):
                y = np.random.choice(action_number)
                arm_count[y] = arm_count[y] + 1
                action_value[y] = (action_value[y]*(arm_count[y]-1) + np.random.binomial(1,df[0][y]))/arm_count[y]
                #print(action_value,y)
                #print(arm_count)
            elif x == "eps_conj" and i>=len(df):
                argmax = action_value.argmax(axis=0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = (action_value[argmax]*(arm_count[argmax]-1) + np.random.binomial(1,df[0][argmax]))/arm_count[argmax]
                #print(action_value,argmax)
                #print(arm_count)
            #print(x)

        for i in range(len(df)):
            reward = reward + action_value[i]*arm_count[i]
        #print(sum(arm_count))
        regret = max(df[0])*horizon - reward
        return regret



    def UCB():
        df = pd.read_csv(instance,header=None)
        action_value = np.zeros(len(df))
        arm_count = np.zeros(len(df))
        upper_bound = np.zeros(len(df))
        #t = len(df)
        reward = 0
        for i in range(horizon):
            if i < len(df):
                action_value[i] =  np.random.binomial(1,df[0][i])
                arm_count[i] = arm_count[i] + 1
                #upper_bound[i] = 0 + action_value[i]

            else:
                for j in range(len(df)):
                    upper_bound[j] = action_value[j] + np.sqrt(2*np.log(i+1)/arm_count[j])

                argmax = upper_bound.argmax(axis = 0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = ((action_value[argmax]*(arm_count[argmax]-1)) + np.random.binomial(1,df[0][argmax]))/arm_count[argmax]


        for i in range(len(df)):
            #print(arm_count[i],action_value[i])
            reward = reward + action_value[i]*arm_count[i]
        #print(max(df[0])*horizon)
        regret = max(df[0])*horizon - reward
        return regret



    def KL_UCB_bound(action_value, arm_count, total_count):
        delta = 0.001
        min = 0 + action_value/arm_count
        max = 1 - delta
        mid_point = (min + max)/2
        threhsold = 0.0001

        if action_value == 0:
            action_value = action_value + delta
        p = action_value/arm_count
        q = (min + max)/2
        constant_line =  (np.log(total_count) + 3*np.log(np.log(total_count)))/arm_count
        KL = p*np.log(p/q) + (1-p)*np.log((1-p)/(1-q))

        while np.abs(constant_line - KL) > threhsold:

            q = (min + max)/2
            KL = p*np.log(p/q) + (1-p)*np.log((1-p)/(1-q))

            if constant_line > KL:
                min = q
            else:
                max = q

        return q




    def KL_UCB():
        df = pd.read_csv(instance,header=None)
        action_value = np.zeros(len(df))
        arm_count = np.zeros(len(df))
        upper_bound = np.zeros(len(df))
        reward = 0

        for i in range(horizon):
            if i < len(df):
                action_value[i] = np.random.binomial(1,df[0][i])
                arm_count[i] = arm_count[i] + 1

            else:
                for j in range(len(df)):
                    upper_bound[j] = KL_UCB_bound(action_value[j],arm_count[j],i+1)

                argmax = upper_bound.argmax(axis=0)
                arm_count[argmax] = arm_count[argmax] + 1
                action_value[argmax] = ((action_value[argmax]*(arm_count[argmax]-1)) + np.random.binomial(1,df[0][argmax]))/arm_count[argmax]

        for i in range(len(df)):
            reward = reward + action_value[i]*arm_count[i]
            #print(max(df[0])*horizon)
        regret = max(df[0])*horizon - reward
        return regret

    def thompson_sampling():
