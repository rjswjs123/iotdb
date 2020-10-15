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

if __name__ == '__main__':
    a1 = get_time_stamp16()
    print(a1)
    print(stampToTime(a1))
    a2 = get_time_stamp13()
    print(a2)
    print(stampToTime(a2))