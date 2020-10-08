import sys
sys.path.append("./utils")
from utils.IoTDBConstants import *
from utils.Tablet import Tablet
from Session import Session
import os, re
import numpy as np

directory=os.listdir('DataforIoTDB/normal/flexible/1')
os.chdir('DataforIoTDB/normal/flexible/1')
value_list=[]
for file in directory:
    with open(file) as f:
        data=f.read().splitlines()
        floats = []
        for elem in data:
            try:
                floats.append(float(elem))
            except ValueError:
                pass
    value_list.append(floats)

df1=pd.DataFrame(value_list)
df2=df1.T.set_index(0)
# print(df2.iloc[:,0:0])

# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set and delete storage groups
session.set_storage_group("root.normalT")
#
# setting time series.
session.create_time_series("root.normalT.flexible", TSDataType.DOUBLE, TSEncoding.PLAIN, Compressor.SNAPPY)
session.create_time_series("root.normalT.rigid", TSDataType.DOUBLE, TSEncoding.PLAIN, Compressor.SNAPPY)


# setting multiple time series once.
ts_path_lst_ = ["root.normalT.flexible.x1.p1.s1", "root.normalT.flexible.x1.p1.s2", "root.normalT.flexible.x1.p1.s3","root.normalT.flexible.x1.p1.s4",
                "root.normalT.flexible.x1.p2.s1", "root.normalT.flexible.x1.p2.s2","root.normalT.flexible.x1.p2.s3","root.normalT.flexible.x1.p2.s4",
                "root.normalT.flexible.x1.p3.s1","root.normalT.flexible.x1.p3.s2","root.normalT.flexible.x1.p3.s3","root.normalT.flexible.x1.p3.s4",
                "root.normalT.flexible.x1.p4.s1","root.normalT.flexible.x1.p4.s2","root.normalT.flexible.x1.p4.s3","root.normalT.flexible.x1.p4.s4",
                "root.normalT.flexible.x1.p5.s1","root.normalT.flexible.x1.p5.s2","root.normalT.flexible.x1.p5.s3","root.normalT.flexible.x1.p5.s4"]
data_type_lst_=[]
for _ in range(20):
    data_type_lst_.append(TSDataType.DOUBLE)

encoding_lst_ = [TSEncoding.PLAIN for _ in range(len(data_type_lst_))]
compressor_lst_ = [Compressor.SNAPPY for _ in range(len(data_type_lst_))]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)

#
# with open('nor11.dat') as file:
#     data = file.read().splitlines()
#     floats=[]
#     for elem in data:
#         try:
#             floats.append(float(elem))
#         except ValueError:
#             pass
# Fixing random state for reproducibility
np.random.seed(19680801)

# dt:frequency one sec
dt = 0.001
t = np.arange(0, 10, dt)
s1= np.around(np.sin(np.random.randn(len(t))),4)
s2= np.around(np.sin(np.random.randn(len(t))),4)
s3= np.around(np.sin(np.random.randn(len(t))),4)
s4= np.around(np.sin(np.random.randn(len(t))),4)
s5= np.around(np.sin(np.random.randn(len(t))),4)
s6= np.around(np.sin(np.random.randn(len(t))),4)
s7= np.around(np.sin(np.random.randn(len(t))),4)
s8= np.around(np.sin(np.random.randn(len(t))),4)
s9= np.around(np.sin(np.random.randn(len(t))),4)
s10= np.around(np.sin(np.random.randn(len(t))),4)

data_types_=[]
for i in range(10):
    data_types_.append(TSDataType.DOUBLE)




measurements_ = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"]

for time in range(len(t)):
    values= [s1[time],s2[time],s3[time],s4[time],s5[time],s6[time],
               s7[time],s8[time],s9[time],s10[time]]
    session.insert_record("root.testdat", time, measurements_, data_types_, values)

for time in range(len(floats)):
    values = [floats[time]]
    session.insert_record("root.testdat", time, measurements_, data_types_, values)

# floats=df2.index.tolist()
# floats2=df2.iloc[:,0:1].values.tolist()
# print(floats2)



#
#
# # insert multiple records into database
# measurements_list_ = [["s1"],
#                       ["s2"]]
# values_list_ = [[float(data[0])],[floats[1]]]
# data_type_list_ = [data_types_, data_types_]
# device_ids_ = ["root.testdat", "root.testdat"]
# session.insert_records(device_ids_, [4, 5], measurements_list_, data_type_list_, values_list_)
