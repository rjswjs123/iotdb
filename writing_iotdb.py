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

milliseconds=0
time=0
start_time = datetime.now()
try:
    while milliseconds<(60*1000):
        values = []
        temperature = 20.0
        temperature += random.uniform(-1, 1)
        values.append(np.around(temperature, 4))
        milliseconds = int(millis())
        session.insert_record("root.one_m", milliseconds, measurements_, data_types_, values)
        time +=1
        sleep(0.00048828125)
finally:
    # close session connection.
    print(time)
    session.close()
    print("All executions done!!")