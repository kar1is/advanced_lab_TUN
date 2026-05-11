import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x-0.76929)**3 - 3*(x-0.76929)**2 + (x-0.76929)+3

x = np.linspace(0,3.6,1000)

plt.figure(figsize=(4,4))
plt.plot(x,f(x), c='k')
plt.xticks([])
plt.yticks([])

ax = plt.gca()

plt.scatter(0.95279, 3.08866,c='r')
plt.annotate(
    rf'$(V_p,I_p)$',
    (0.95279, 3.08866),
    textcoords="offset points",
    xytext=(0,8)
)

plt.scatter(2.58579,0.91134,c='r')
plt.annotate(
    rf'$(V_v,I_v)$',
    (2.58579,0.91134),
    textcoords="offset points",
    xytext=(-16,8)
)

plt.scatter(3.40228,3.08866,c='r')
plt.annotate(
    rf'$(V_{{pf}},I_p)$',
    (3.40228,3.08866),
    textcoords="offset points",
    xytext=(-36,8)
)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
plt.xlabel('V')
plt.ylabel('I')
plt.tight_layout()
plt.savefig('IV.eps', format='eps')
plt.show()
