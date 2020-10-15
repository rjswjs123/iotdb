import sys
sys.path.append("./utils")
from utils.IoTDBConstants import *
from Session import Session
from time import sleep
import time
from datetime import datetime
from datetime import timedelta
# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set and delete storage groups
session.set_storage_group("root.opcua")

# setting multiple time series once.
ts_path_lst_ = ["root.opcua.s1","root.opcua.s2","root.opcua.s3","root.opcua.s4","root.opcua.s5",
                "root.opcua.s6","root.opcua.s7","root.opcua.s8","root.opcua.s9","root.opcua.s10",
                "root.opcua.s11","root.opcua.s12","root.opcua.s13","root.opcua.s14","root.opcua.s15",
                "root.opcua.s16","root.opcua.s17","root.opcua.s18","root.opcua.s19","root.opcua.s20"]
data_type_lst_=[]
for _ in range(len(ts_path_lst_)):
    data_type_lst_.append(TSDataType.DOUBLE)

encoding_lst_ = [TSEncoding.PLAIN for _ in range(len(data_type_lst_))]
compressor_lst_ = [Compressor.SNAPPY for _ in range(len(data_type_lst_))]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)
#
sensor_number=20
data_types_ = []
for i in range(sensor_number):
    data_types_.append(TSDataType.DOUBLE)
#
measurements_ = ["s1", "s2", "s3", "s4", "s5","s6", "s7", "s8", "s9", "s10",
                 "s11", "s12", "s13", "s14", "s15","s16", "s17", "s18", "s19", "s20"]

start_time = datetime.now()

# returns the elapsed milliseconds since the start of the program
def millis():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

from opcua import Client
client=Client("opc.tcp://127.0.0.1:12345")
time=0
try:
    client.connect()
    print("start client")
    client.get_namespace_array()
    objects = client.get_objects_node()
    tempsens = objects.get_children()[1]
    while True:
        values = []
        for i in tempsens.get_children():
            values.append(i.get_value())
        # print(values)
        milliseconds=int(millis())
        session.insert_record("root.opcua", milliseconds, measurements_, data_types_, values)
        time+=1

finally:
    print(time)
    print(milliseconds)
    # close session connection.
    session.close()
    client.close_session()
    print("client close")


