import numpy as np
import argparse
from gridworld import windyGridWorld

ap = argparse.ArgumentParser()
ap.add_argument("--num_action")
ap.add_argument("--stochasticity")
args = ap.parse_args()

# print(args.num_action)
# print(args.stochasticity)

#Data generation for part a with four action
if int(args.num_action) == 4 and int(args.stochasticity) == 0:
    file = open("output_a.txt", "a")

    for j in range(200):
        t = 0
        for i in range(10):
            np.random.seed(i)
            cls = windyGridWorld("grid_world_env.txt")
            cls.number_of_actions = 4
            cls.episode = j
            t = cls.Sarsa()
            file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')


#Data generation for part b with eight action
if int(args.num_action) == 8 and int(args.stochasticity) == 0:
    file = open("output_b.txt", "a")

    for j in range(200):
        t = 0
        for i in range(10):
            np.random.seed(i)
            cls = windyGridWorld("grid_world_env.txt")
            cls.number_of_actions = 8
            cls.episode = j
            t = cls.Sarsa()
            file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')


#Data generation for part c with action and stochasticity
if int(args.num_action) == 8 and int(args.stochasticity) == 1:

    file = open("output_c.txt", "a")

    for j in range(200):
        t = 0
        for i in range(10):
            np.random.seed(i)
            cls = windyGridWorld("grid_world_env.txt")
            cls.number_of_actions = 8
            cls.wind_nature = 1
            cls.episode = j
            t = cls.Sarsa()
            file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')
