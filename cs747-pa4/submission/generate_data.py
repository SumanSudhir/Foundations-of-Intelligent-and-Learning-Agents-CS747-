import numpy as np
import argparse
import os
from gridworld import windyGridWorld

ap = argparse.ArgumentParser()
ap.add_argument("--num_action")
ap.add_argument("--stochasticity")
args = ap.parse_args()

# print(args.num_action)
# print(args.stochasticity)

#Part A
#Data generation for part a with four action
if int(args.num_action) == 4 and int(args.stochasticity) == 0:
    print("Data generation for part a with four action")
    os.remove("output_a.txt")
    file = open("output_a.txt", "a")
    t = 0
    mean_time = [0]*501
    for i in range(10):
        np.random.seed(i)
        cls = windyGridWorld("grid_world_env.txt")
        cls.number_of_actions = 4
        cls.episode = 500
        t = cls.Sarsa()
        mean_time = np.add(cls.time,mean_time)

    print(mean_time/10)
    for j in range(cls.episode+1):
        file.write(str("Episode")+ "," + str(j) + "," +  str("Time") + "," + str(mean_time[j]/10) + "\n")


#Part B
#Data generation for part b with king move
if int(args.num_action) == 8 and int(args.stochasticity) == 0:
    print("Data generation for part b with king move")
    os.remove("output_b.txt")
    file = open("output_b.txt", "a")
    t = 0
    mean_time = [0]*501
    for i in range(10):
        np.random.seed(i)
        cls = windyGridWorld("grid_world_env.txt")
        cls.number_of_actions = 8
        cls.episode = 500
        t = cls.Sarsa()
        mean_time = np.add(cls.time,mean_time)

    print(mean_time/10)
    for j in range(cls.episode+1):
        file.write(str("Episode")+ "," + str(j) + "," +  str("Time") + "," + str(mean_time[j]/10) + "\n")


# Part C
# Data generation for part c with king move and stochasticity
if int(args.num_action) == 8 and int(args.stochasticity) == 1:
    print("Data generation for part c with king move and stochasticity")
    os.remove("output_c.txt")
    file = open("output_c.txt", "a")
    t = 0
    mean_time = [0]*1001
    for i in range(10):
        np.random.seed(i)
        cls = windyGridWorld("grid_world_env.txt")
        cls.number_of_actions = 8
        cls.episode = 1000
        cls.wind_nature = 1
        t = cls.Sarsa()
        mean_time = np.add(cls.time,mean_time)

    print(mean_time/10)
    for j in range(cls.episode+1):
        file.write(str("Episode")+ "," + str(j) + "," +  str("Time") + "," + str(mean_time[j]/10) + "\n")



# #Data generation for part a with four action
# if int(args.num_action) == 4 and int(args.stochasticity) == 0:
#     file = open("output_a.txt", "a")
#     print("Creating data for 4 action case")
#
#     for j in range(200):
#         t = 0
#         for i in range(10):
#             np.random.seed(i)
#             cls = windyGridWorld("grid_world_env.txt")
#             cls.number_of_actions = 4
#             cls.episode = j
#             t = cls.Sarsa()
#             file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')
#
#
# #Data generation for part b with eight action
# if int(args.num_action) == 8 and int(args.stochasticity) == 0:
#     file = open("output_b.txt", "a")
#     print("Creating data for king move case")
#     for j in range(200):
#         t = 0
#         for i in range(10):
#             np.random.seed(i)
#             cls = windyGridWorld("grid_world_env.txt")
#             cls.number_of_actions = 8
#             cls.episode = j
#             t = cls.Sarsa()
#             file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')
#
#
# #Data generation for part c with action and stochasticity
# if int(args.num_action) == 8 and int(args.stochasticity) == 1:
#
#     print("Creating data for king move with Stochastic case")
#     file = open("output_c.txt", "a")
#     for j in range(200):
#         t = 0
#         for i in range(10):
#             np.random.seed(i)
#             cls = windyGridWorld("grid_world_env.txt")
#             cls.number_of_actions = 8
#             cls.wind_nature = 1
#             cls.episode = j
#             t = cls.Sarsa()
#             file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')
