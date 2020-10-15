import time
from time import sleep

max_time_end = time.time()+(10)  # 10 seconds
count=0
while True:
    if time.time() > max_time_end:
        break
    count += 1
    sleep(0)


print(count)