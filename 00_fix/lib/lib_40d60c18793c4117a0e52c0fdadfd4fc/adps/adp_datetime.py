"""datetimeアダプタパッケージ
"""
import lib_40d60c18793c4117a0e52c0fdadfd4fc.pkgs as pkgs

datetime = None
datetime_class = object()
timedelta = object()
# リリース時にはコメントアウトしてください
import datetime
datetime_class = datetime.datetime
timedelta = datetime.timedelta

def __import():
    global datetime
    global datetime_class
    global timedelta
    if datetime == None:
        datetime = pkgs.imp("codecs")
        datetime_class = datetime.datetime
        timedelta = datetime.timedelta

def serial(src:float)->int:
    dt = cnv_float2datetime(src)
    zero_day = datetime_class(1899,12,31)
    irregular_next = datetime_class(1900,3,1)
    res = (dt - zero_day).days
    if dt >= irregular_next:
        res = res + 1
    return res

def strptime(src:str,fmt:str="%Y/%m/%d %H:%M:%S")->float:
    __import()
    dt = datetime_class.strptime(src,fmt)
    res = cnv_datetime2float(dt)
    return res

def strftime(src:float,fmt:str)->str:
    dt = cnv_float2datetime(src)
    return dt.strftime(fmt=fmt)

def cnv_float2datetime(src:float)->datetime_class:
    __import()
    return datetime_class.fromtimestamp(__timestamp=src)

def cnv_datetime2float(src:datetime_class)->float:
    __import()
    return src.timestamp()

def add_days(src,days):
    """datetimeに指定の日数を加算または減算します
    """
    dt = cnv_float2datetime(src)
    td = timedelta(days=days)
    res = cnv_datetime2float(dt + td)
    return res

def update_datetime(src:float,
                    year:int=-1,month:int=-1,day:int=-1, 
                    hour:int=-1,minute:int=-1,second:int=-1,
                    microsecond:int=-1
                    )->float:
    """日時の一部を更新して返します
    """
    dt = cnv_float2datetime(src)

    if year == -1:
        year = dt.year
    if month == -1:
        month = dt.month
    if day == -1:
        day = dt.day
    if hour == -1:
        hour = dt.hour
    if minute == -1:
        minute = dt.minute
    if second == -1:
        second = dt.second
    if microsecond == -1:
        microsecond = dt.microsecond
    dt = datetime_class(
        year=year,month=month,day=day,
        hour=hour,minute=minute,second=second,
        microsecond=microsecond)
    res = cnv_datetime2float(dt)
    return res
