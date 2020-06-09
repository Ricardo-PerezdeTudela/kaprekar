# 23.10.2019
#
# Recreational mathematics: The Kaprekar constant 6174
#
# Any 4-digit number ends up in the Kaprekar constant 
# if the Kaprekar operation is recursively done to it: 
# Form the biggest and the smallest number one can form 
# with the four digits, and subtract them. 
#
# The number of steps (nsteps) required to reach the Kaprekar constant 
# follows a curious pattern. This script generates a plot 
# showing nsteps for any number N=XY, as a function of X and Y.

import numpy as np
import matplotlib.pyplot as plt

def Kaprekar_step(number):
    n = str(number).rjust(4, '0')
    digits = []
    for i in range(len(n)):
       digits.append(n[i])

    maxs = sorted(digits, reverse=True)
    mins = sorted(digits)

    max = int(''.join(map(str,maxs)))
    min = int(''.join(map(str,mins)))

    diff = max - min
    return diff


Kaprekar_number = 6174
Xmax = 100
max_cont = 100

niter = []
for i in range(0, Xmax**2):
    cont = 0
    n = i
    while (n != Kaprekar_number):
        if (cont >= max_cont):
            cont = 0
            break
        n = Kaprekar_step(n)
        cont = cont + 1
    niter.append(cont)

nn = np.asarray(niter)

nnn = np.reshape(nn,(Xmax,Xmax))

plt.title(r'Number of steps for $X \times Y$ reach the Kaprekar constant')
plt.xlabel("X")
plt.ylabel("Y")
mymap = plt.cm.get_cmap('hot', 8)    # 8 discrete colors, from 0 to 7.
heatmap = plt.pcolor(nnn, cmap=mymap)
plt.colorbar(heatmap)
plt.show()
