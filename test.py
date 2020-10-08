import random
import time
a=time.perf_counter()
count=0
while ((time.perf_counter()-a)<1):
    count+=1
    time.sleep(0.001)
print(count)