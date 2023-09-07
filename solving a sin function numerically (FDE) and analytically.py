#!/usr/bin/env python
# coding: utf-8

# ## Calculation of the Sin function
# 

# In[62]:


import numpy as np
from math import *
import matplotlib.pyplot as plt


# * f(x) = sin(kx)  #This is the space dependent sine function
# 
# * K = 2pi/ wavelenght

# In[70]:


xmax = 10                   #Physical Domain
nx = 200                    #Number of samples
dx = xmax/(nx-1)           #Grid Increment
x = np.linspace(0,xmax,nx) #Initialized Vector
l = 20*dx                  #Number of points per wavelength
k = 2*pi/l                 #Wave number
f = np.sin(k*x)       #Wave function


# # Plotting the sine function

# In[76]:


plt.plot(x,f)
plt.title('Sin Function')
plt.xlabel =('x (m)')
plt.ylabel =('Amplitude')
plt.xlim (0, xmax)
plt.grid()
plt.show()


# # Calculating the sine function numerically and comparing it to an Analytical solution

# In[72]:


nder = np.zeros(nx)  # Numerical derivative Initaiating a zero vector using the length of our physical domain
ader = np.zeros(nx)  # Analytical derivative 

#Create a loop to go from 1 to the lenght of our domain

for i in range (1, nx-1):   #This just tells us how long the loop would run for
    nder[i] = (f[i + 1] - f [i-1])/ (2*dx) # Here we initiate the finite difference approximation and ask the computer to update the zero vectors with new values

ader = k * np.cos(k*x)  #Analytical solution

ader[0] = 0
ader[nx-1] = 0 #Excluding the first and last term in order to calculate the root mean square error

#Error RMS is done to avoid problems with the wave edges

rms = np.sqrt(np.mean(nder-ader)**2)






# # Plotting the numerical derivative superimposing the analytical derivative and showing the difference

# In[73]:


plt.plot (x, nder, label = 'Numerical derivative, 2 points', marker = '*', color = 'black')
plt.plot (x, ader, label = 'Analytical derivative', lw = 1.5, ls = "-", color = 'red')
plt.plot (x, nder-ader, label = 'Differences', lw = 2, ls = '-')
plt.title (f'First Derivative, Err (rms) = {round(rms,8)}')
plt.xlabel =('x(m)')
plt.ylabel = ('Amplitude')
plt.legend(loc= 'lower left')
plt.grid()
plt.show()


# ## the numerical derivatives are well represented with the black markers while the red is the analytical derivative, the difference between the two is represented by the blue oscillating line. the RMS error from 0 to 10 is indicated. the key question about the difference(blue oscillation) is if it is accurate enough for a real simulation and how can we further investigate the behaviour of these finite differences
# 
# In order to do this we need to introduce the concept of number of points per wavelength
# 
# n = lamda/dx
# 
# # Now let's plot number of points per wavelength

# In[74]:


plt.plot (x, nder, label = 'Numerical derivative, 2 points', marker = '*', color = 'black')
plt.title (f'First derivative, RMS ERROR = {round(rms, 8)} num_of_points = {l/dx}')
plt.xlabel =('x')
plt.ylabel= ('Amplitude')
plt.legend(loc='lower left')
plt.xlim(xmax/2-1, xmax/2+1)
plt.grid()
plt.show()


# ###  Conclusion
# 
# * finite difference method can provide first derivative of a function
# * The accuracy depends on the number of points per wavelength
# * the more point we use the more accurate the approximation

# In[ ]:




