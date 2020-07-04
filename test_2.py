import numpy as np


def nonlin(x, deriv = False):
    if (deriv == True):
        return x * ( 1 - x )
    return 1 / ( 1 + np.exp( -x ) )

class Individ():
    def __init__(self):
        self.weig = np.random.random((3, 1))
        self.fit = 0

X = np.array([  [1, 0, 1],
                [0, 1, 1],
                [0, 0, 1],
                [0, 1, 1] ])

i_arr = []

for i in range(30):
    c = Individ()
    i_arr.append(c)

for iter in range(30):

    # прямое распространение
    l0 = X
    l1 = nonlin( np.dot(l0, i_arr[iter].weig ) )
    print(l1)
    print()
