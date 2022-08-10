

#Integrate Dirac Delta function (x-a)*f(x) from (a-x1) to (a+x2)=f(a)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
si=10.0

def f(x):
    return ((1.0/(si*np.sqrt(2*np.pi)))*np.exp(-(x-np.pi)**2/(2*si**2)))
a=np.pi-5*si #lower limit
b=np.pi+5*si #upper limit
x=np.arange(a,b,0.1)
R=[]
SI=[]
for k in range(10):
    R.append(quad(lambda x:f(x),a,b)[0])
    SI.append(si)
    plt.plot(x,f(x))
    si=si/2

print(R)
print(SI)
plt.xlabel("sigma")
plt.ylabel("integration result")
plt.grid(True)
plt.show()
