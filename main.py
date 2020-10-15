import sys
import xlrd
sys.path.append("./utils")
from utils.IoTDBConstants import *
from utils.Tablet import Tablet
from Session import Session
import datetime
import time

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

# setting multiple time series once.
ts_path_lst_ = ["root.turbine1.bently3500.sensor1", "root.turbine1.bently3500.sensor2", "root.turbine1.bently3500.sensor3",
                "root.turbine1.bently3500.sensor4", "root.turbine1.bently3500.sensor5", "root.turbine1.bently3500.sensor6",
                "root.turbine1.bently3500.sensor7","root.turbine1.bently3500.sensor8","root.turbine1.bently3500.sensor9",
                "root.turbine1.bently3500.sensor10", "root.turbine1.bently3500.sensor11", "root.turbine1.bently3500.sensor12",
                "root.turbine1.bently3500.sensor13", "root.turbine1.bently3500.sensor14", "root.turbine1.bently3500.sensor15",
                "root.turbine1.bently3500.sensor16", "root.turbine1.bently3500.sensor17", "root.turbine1.bently3500.sensor18",
                "root.turbine1.bently3500.sensor19", "root.turbine1.bently3500.sensor20", "root.turbine1.bently3500.sensor21",
                "root.turbine1.bently3500.sensor22", "root.turbine1.bently3500.sensor23", "root.turbine1.bently3500.sensor24",]

number = len(ts_path_lst_)
data_type_lst_ = [TSDataType.DOUBLE for _ in range(number)]
encoding_lst_ = [TSEncoding.PLAIN for _ in range(number)]
compressor_lst_ = [Compressor.SNAPPY for _ in range(number)]
session.create_multi_time_series(ts_path_lst_, data_type_lst_, encoding_lst_, compressor_lst_)

# insert one record into the database.
# measurements_ = ["s_01", "s_02", "s_03", "s_04", "s_05", "s_06"]
# values_ = [False, 10, 11, 1.1, 10011.1, "test_record"]
# data_types_ = [TSDataType.BOOLEAN, TSDataType.INT32, TSDataType.INT64,
#             TSDataType.FLOAT, TSDataType.DOUBLE, TSDataType.TEXT]
# session.insert_record("root.sg_test_01.d_01", 1, measurements_, data_types_, values_)

# insert multiple records into database
testdata = xlrd.open_workbook('testdata.xlsx')
Hdata = testdata.sheet_by_name('Sheet1')
length_Hdata = Hdata.nrows
# print(length_Hdata)
# print(Hdata.col_values(0))#输出第一列
device_ids_ = ["root.turbine1.bently3500" for _ in range(length_Hdata)]
measurements_list_ = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6","sensor7",
                      "sensor8", "sensor9", "sensor10", "sensor11", "sensor12","sensor13", "sensor14",
                      "sensor15", "sensor16", "sensor17", "sensor18","sensor19", "sensor20", "sensor21",
                      "sensor22", "sensor23", "sensor24"]

measurements_lists_=[measurements_list_ for _ in range(length_Hdata)]
# print(measurements_lists_)

data_type_list_ = [TSDataType.DOUBLE for _ in range(number)]
data_type_lists_ = [data_type_list_ for _ in range(length_Hdata)]
print(len(data_type_lists_))
print(len(measurements_lists_))

values_list_ = []
for i in range(length_Hdata):
   values_list_.append([])
   for j in range(number):
      values_list_[i].append(Hdata.cell(i,0).value)


print(len(values_list_))
# print(data_type_list_)

timestamp = [get_time_stamp16() for _ in range(length_Hdata)]
session.insert_records(device_ids_, timestamp, measurements_lists_, data_type_lists_, values_list_)

# close session connection.
session.close()
print("All executions done!!")