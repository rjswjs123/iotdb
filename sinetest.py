import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec


# Fixing random state for reproducibility
np.random.seed(19680801)

#dt:frequency one sec
dt = 0.001
t = np.arange(0, 10, dt)
print(t)
# n1 = np.random.randn(len(t))
# n2=np.random.randn(len(t))
# n3=np.random.randn(len(t))
# n4=np.random.randn(len(t))
# n5=np.random.randn(len(t))
s1= np.around(np.sin(np.random.randn(len(t))),4)
print(s1)
# s2= np.around(np.sin(np.random.randn(len(t))),4)
# s3= np.around(np.sin(np.random.randn(len(t))),4)
# s4= np.around(np.sin(np.random.randn(len(t))),4)
# s5= np.around(np.sin(np.random.randn(len(t))),4)
# s6= np.around(np.sin(np.random.randn(len(t))),4)
# s7= np.around(np.sin(np.random.randn(len(t))),4)
# s8= np.around(np.sin(np.random.randn(len(t))),4)
# s9= np.around(np.sin(np.random.randn(len(t))),4)
# s10= np.around(np.sin(np.random.randn(len(t))),4)
#
#
#
# test=[]
# for i in range(5):
#     n = np.random.randn(len(t))
#     s = np.sin(n)
#     test.append(s)





# test=np.around(s,4)
# for i in range(100):
#     print(test[i])

# plt.subplot(211)
# plt.plot(t, s)