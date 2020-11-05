import sys
import xlrd
sys.path.append("./utils")
from utils.IoTDBConstants import *
from utils.Tablet import Tablet
from Session import Session
import datetime
import time
import numpy as np


# -------------variable---------------- #
# you can control this parameters
Sensor=24 # number of sensors
Loop=200 # number of LOOP

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



# creating session connection.
ip = "127.0.0.1"
port_ = "6667"
username_ = 'root'
password_ = 'root'
session = Session(ip, port_, username_, password_)
session.open(False)

# set storage groups
session.set_storage_group("root.turbine1")


ts_path_lst_=[]
for i in range(Sensor):
    ts_path_lst_.append("root.turbine1.bently3500."+str(i+1))

number = len(ts_path_lst_)
data_type_lst_ = [TSDataType.DOUBLE for _ in range(number)]
encoding_lst_ = [TSEncoding.PLAIN for _ in range(number)]
compressor_lst_ = [Compressor.SNAPPY for _ in range(number)]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)

# insert multiple records into database
testdata = xlrd.open_workbook('testdata.xlsx')
Hdata = testdata.sheet_by_name('Sheet1')
length_Hdata = Hdata.nrows

device_ids_ = ["root.turbine1.bently3500" for _ in range(length_Hdata)]
measurements_list_=[]
for i in range(Sensor):
    measurements_list_.append(str(i+1))

measurements_lists_=[measurements_list_ for _ in range(length_Hdata)]
data_type_list_ = [TSDataType.DOUBLE for _ in range(number)]
data_type_lists_ = [data_type_list_ for _ in range(length_Hdata)]

values_list_ = []
for i in range(length_Hdata):
   values_list_.append([])
   for j in range(number):
      values_list_[i].append(Hdata.cell(i,0).value)

# A function that adds the size of batch
def add_Batch(n):
    return n + length_Hdata

st=[] # The array of timestamps which start to inserting data
en=[] # The array of timestamps which end to inserting data
Test_time=[] # The array of test time

try:
    Timestamp = list(range(length_Hdata)) # First generate an array of batch size [0,1,..2047]
    for i in range(Loop):
        st.append(get_float_time_stamp())
        session.insert_records(device_ids_, Timestamp, measurements_lists_, data_type_lists_, values_list_)
        en.append(get_float_time_stamp())
        # Test_time.append(en[i]-st[i])
        # print("Test_time: " + str(Test_time[i]))

        # Using add_Batch fucntion adds the size of batch to each array index
        a = list(map(add_Batch, Timestamp))
        # ex) size of batch: 2048 => [0+2048,1+2048,...2047+2048]
        # ex) if number of LOOP : 2 => [0,1,2,3,.....,2047]
        #                              [2048,2049,2050,.....4095]

finally:
    All_Test_time=en[-1]-st[0]
    print("Test_time: "+str(All_Test_time))
    Writing_frequency=(length_Hdata*Sensor*Loop)/All_Test_time
    print("Writing frequency: "+ str(np.around(Writing_frequency,2)))
    # close session connection.
    session.close()
    print("All executions done!!")








