import numpy as np
import pandas as pd

from algorithm import Algorithm

instance = ["../instances/i-1.txt",
            "../instances/i-2.txt", "../instances/i-3.txt"]
algo = ["round-robin", "epsilon-greedy", "ucb", "kl-ucb", "thompson-sampling"]
epsilon = [0.002, 0.02, 0.2]
horizon = [50, 200, 800, 3200, 12800, 51200, 204800]
random_seed = []
for i in range(50):
    random_seed.append(i)


file = open("output.txt", "a")

# alg = Algorithm(instance[0], algo[0],
#                 random_seed[0], epsilon[0], horizon[0])
# np.random.seed(random_seed[0])
# regret = alg.epsilon_greedy()
# print(regret)

#regret = 0
for al in algo:
    for hz in horizon:
        for rs in random_seed:
            for ins in instance:
                # print(hz)
                if al == "epsilon-greedy":
                    i
                    for ep in epsilon:
                        alg = Algorithm(ins, al, rs, ep, hz)
                        np.random.seed(rs)
                        regret = alg.epsilon_greedy()
                        file.write(ins + ", " + al + ", " +
                                   str(rs) + ", " + str(ep) + ", " + str(hz) + ", " + str(regret) + '\n')

                else:
                    ep = 0.02

                    if al == "round-robin":
                        alg = Algorithm(ins, al, rs, ep, hz)
                        np.random.seed(rs)
                        regret = alg.round_robin()

                    elif al == "ucb":
                        alg = Algorithm(ins, al, rs, ep, hz)
                        np.random.seed(rs)
                        regret = alg.UCB()

                    elif al == "kl-ucb":
                        alg = Algorithm(ins, al, rs, ep, hz)
                        np.random.seed(rs)
                        regret = alg.KL_UCB()

                    elif al == "thompson-sampling":
                        alg = Algorithm(ins, al, rs, ep, hz)
                        np.random.seed(rs)
                        regret = alg.thompson_sampling()

                    # print(regret)
                    file.write(ins + ", " + al + ", " +
                               str(rs) + ", " + str(ep) + ", " + str(hz) + ", " + str(regret) + '\n')
