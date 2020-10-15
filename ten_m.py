import sys

sys.path.append("./utils")
from utils.IoTDBConstants import *
from Session import Session
from time import sleep
import time
from datetime import datetime
from datetime import timedelta
import random
import numpy as np

# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set and delete storage groups
session.set_storage_group("root.one_m")
session.create_time_series("root.one_m.s1", TSDataType.DOUBLE, TSEncoding.PLAIN, Compressor.SNAPPY)

measurements_ = ["s1"]
values_ = [10]
data_types_ = [TSDataType.DOUBLE]





# returns the elapsed milliseconds since the start of the program
def millis():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms


# Fixing random state for reproducibility
np.random.seed(19680801)

# dt:frequency one sec
dt = 0.00048828125
t = np.arange(0, 600, dt)
s1= np.around(np.random.randn(len(t))+20,4)
print(len(s1))
milliseconds=0

try:
    start_time = datetime.now()
    for time in range(len(s1)):
        values=[s1[time]]
        milliseconds = int(millis())
        print(milliseconds)
        session.insert_record("root.one_m", time, measurements_, data_types_, values)
finally:
    # close session connection.
    print(time)
    milliseconds = int(millis())
    print(milliseconds/1000)
    session.close()
    print("All executions done!!")


