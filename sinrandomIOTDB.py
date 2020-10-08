import sys
sys.path.append("./utils")
from utils.IoTDBConstants import *
from utils.Tablet import Tablet
from Session import Session
import os, re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set and delete storage groups
session.set_storage_group("root.sin")
#
# setting multiple time series once.
ts_path_lst_ = ["root.sin.s1","root.sin.s2","root.sin.s3","root.sin.s4",
                "root.sin.s5","root.sin.s6","root.sin.s7","root.sin.s8",
                "root.sin.s9","root.sin.s10","root.sin.s11","root.sin.s12","root.sin.s13","root.sin.s14",
                "root.sin.s15","root.sin.s16","root.sin.s17","root.sin.s18",
                "root.sin.s19","root.sin.s20"]
data_type_lst_=[]
for _ in range(len(ts_path_lst_)):
    data_type_lst_.append(TSDataType.DOUBLE)

encoding_lst_ = [TSEncoding.PLAIN for _ in range(len(data_type_lst_))]
compressor_lst_ = [Compressor.SNAPPY for _ in range(len(data_type_lst_))]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)

# Fixing random state for reproducibility
np.random.seed(19680801)

# dt:frequency one sec
dt = 0.001
t = np.arange(0, 10, dt)
s1= np.around(np.sin(np.random.randn(10)),4)
s2= np.around(np.sin(np.random.randn(len(t))),4)
s3= np.around(np.sin(np.random.randn(len(t))),4)
s4= np.around(np.sin(np.random.randn(len(t))),4)
s5= np.around(np.sin(np.random.randn(len(t))),4)
s6= np.around(np.sin(np.random.randn(len(t))),4)
s7= np.around(np.sin(np.random.randn(len(t))),4)
s8= np.around(np.sin(np.random.randn(len(t))),4)
s9= np.around(np.sin(np.random.randn(len(t))),4)
s10= np.around(np.sin(np.random.randn(len(t))),4)
s11= np.around(np.sin(np.random.randn(len(t))),4)
s12= np.around(np.sin(np.random.randn(len(t))),4)
s13= np.around(np.sin(np.random.randn(len(t))),4)
s14= np.around(np.sin(np.random.randn(len(t))),4)
s15= np.around(np.sin(np.random.randn(len(t))),4)
s16= np.around(np.sin(np.random.randn(len(t))),4)
s17= np.around(np.sin(np.random.randn(len(t))),4)
s18= np.around(np.sin(np.random.randn(len(t))),4)
s19= np.around(np.sin(np.random.randn(len(t))),4)
s20= np.around(np.sin(np.random.randn(len(t))),4)
print(s1)
# data_types_=[]
# for i in range(20):
#     data_types_.append(TSDataType.DOUBLE)
#
# measurements_ = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10",
#                  "s11","s12","s13","s14","s15","s16","s17","s18","s19","s20"]
#
# for time in range(len(t)):
#     values= [s1[time],s2[time],s3[time],s4[time],s5[time],s6[time],
#                s7[time],s8[time],s9[time],s10[time],s11[time],s12[time],s13[time],s14[time],s15[time],s16[time],
#                s17[time],s18[time],s19[time],s20[time]]
#     session.insert_record("root.sin", time, measurements_, data_types_, values)
