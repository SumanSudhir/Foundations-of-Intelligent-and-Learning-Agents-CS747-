import numpy as np
from gridworld import windyGridWorld

# ap = argparse.ArgumentParser()
# ap.add_argument("--num_action")
# ap.add_argument("--stochasticity")
# args = ap.parse_args()



file = open("output2.txt", "a")

for j in range(200):
    t = 0
    for i in range(10):
        np.random.seed(i)
        cls = windyGridWorld("grid_world_env.txt")
        cls.number_of_actions = 8
        cls.episode = j
        t = cls.Sarsa()
        file.write(str("episode") +  "," +  str(j) + ", " + str("randomSeed") +  "," + str(i) + ", " + str("time") +  "," +  str(t) + '\n')



# import matplotlib.pyplot as plt
#
# plt.plot(time,episode)
# plt.savefig("img2.png")
