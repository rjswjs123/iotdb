import sys
import xlrd
sys.path.append("./utils")
from utils.IoTDBConstants import *
from utils.Tablet import Tablet
from Session import Session
import datetime
import time
import numpy as np


def get_float_time_stamp():
    datetime_now = datetime.datetime.now()
    return datetime_now.timestamp()

def get_time_stamp16():
    # 生成16时间戳   eg:1540281250399895    -ln
    datetime_now = datetime.datetime.now()
    print(datetime_now)

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 6位，微秒
    data_microsecond = str("%06d"%datetime_now.microsecond)

    date_stamp = date_stamp+data_microsecond
    return int(date_stamp)

def get_time_stamp13():
    # 生成13时间戳   eg:1540281250399895
    datetime_now = datetime.datetime.now()

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 3位，微秒
    data_microsecond = str("%06d"%datetime_now.microsecond)[0:3]

    date_stamp = date_stamp+data_microsecond
    return int(date_stamp)

def stampToTime(stamp):
    datatime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(stamp)[0:10])))
    datatime = datatime+'.'+str(stamp)[10:]
    return datatime

Sensor=1
Loop=20000000

# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set storage groups
session.set_storage_group("root.turbine2")


ts_path_lst_=[]
for i in range(Sensor):
    ts_path_lst_.append("root.turbine2.bently3500."+str(i+1))

number = len(ts_path_lst_)
data_type_lst_ = [TSDataType.DOUBLE for _ in range(number)]
encoding_lst_ = [TSEncoding.PLAIN for _ in range(number)]
compressor_lst_ = [Compressor.SNAPPY for _ in range(number)]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)

# insert multiple records into database
testdata = xlrd.open_workbook('testdata.xlsx')
Hdata = testdata.sheet_by_name('Sheet1')
length_Hdata = Hdata.nrows

device_ids_ = ["root.turbine2.bently3500" for _ in range(length_Hdata)]
measurements_list_=[]
for i in range(Sensor):
    measurements_list_.append(str(i+1))

measurements_lists_=[measurements_list_ for _ in range(length_Hdata)]
data_type_list_ = [TSDataType.DOUBLE for _ in range(number)]
data_type_lists_ = [data_type_list_ for _ in range(length_Hdata)]
print(len(data_type_lists_))
print(len(measurements_lists_))

values_list_ = []
for i in range(length_Hdata):
   values_list_.append([])
   for j in range(number):
      values_list_[i].append(Hdata.cell(i,0).value)

timestamp=0
try:
    st = get_float_time_stamp()
    for length in range(Loop):
        if timestamp%length_Hdata==0:
            timestamp=0
        session.insert_record("root.turbine2.bently3500", length, measurements_list_, data_type_list_, values_list_[timestamp])
        timestamp+=1
    en = get_float_time_stamp()
    Test_time = en - st
    print("Test_time: " + str(Test_time))
    Writing_frequency = (Sensor * Loop) / Test_time


finally:
    print("Writing frequency: "+ str(np.around(Writing_frequency,2)))
    # # close session connection.
    session.close()
    print("All executions done!!")
