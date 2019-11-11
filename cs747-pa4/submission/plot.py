import pandas as pd
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df_a = pd.read_csv("output_a.txt", header=None)
plt.figure(figsize=(13,8))
plt.plot(df_a[3],df_a[1], "r", label = 'windyGridWorldpart_a')
plt.xlabel('time')
plt.ylabel('episode')
plt.legend()
plt.legend(loc='best')
plt.savefig('part_a')
plt.clf()


df_b = pd.read_csv("output_b.txt", header=None)
plt.figure(figsize=(13,8))
plt.plot(df_b[3],df_b[1], "b", label = 'windyGridWorldpart_b')
plt.xlabel('time')
plt.ylabel('episode')
plt.legend()
plt.legend(loc='best')
plt.savefig('part_b')
plt.clf()


df_c = pd.read_csv("output_c.txt", header=None)
plt.figure(figsize=(13,8))
plt.plot(df_c[3],df_c[1], "g", label = 'windyGridWorldpart_c')
plt.xlabel('time')
plt.ylabel('episode')
plt.legend()
plt.legend(loc='best')
plt.savefig('part_c')
plt.clf()
