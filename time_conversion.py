import datetime
import pytz

#  receive in YYYY-MM-DD hh:mm format, return as a dict in the target time zone


def convert_date_time(date_source, timezone_source, timezone_target):
    tz1 = pytz.timezone(timezone_source)  # initial time zone
    tz2 = pytz.timezone(timezone_target)  # target timezone
    date_source = datetime.datetime.strptime(date_source, '%Y-%m-%d %H:%M')
    date_source = tz1.localize(date_source)
    date_source = date_source.astimezone(tz2)
    year = date_source.strftime('%Y')
    month = date_source.strftime('%m')
    day = date_source.strftime('%d')
    hour = date_source.strftime('%H')
    minute = date_source.strftime('%M')
    date_time_list = {'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute}
    return date_time_list

#  receive date in YYYY-MM-DD hh:mm format, return in the same format


def user_date(date_plain):
    date_plain = date_plain.rstrip()
    date_plain = date_plain.lstrip()
    year = date_plain[0:4]
    if int(year) > 2049 or int(year) < 2000:
        print('Error: Years should be between 2000 and 2049')
        return
    else:
        pass
    month = date_plain[5:7]
    if int(month) > 12 or int(month) < 1:
        print('Error: Months are between 1 and 12')
        return
    else:
        pass
    day = date_plain[8:10]
    if int(day) > 31 or int(day) < 1:
        print('Error: Days are between 1 and 30')
        return
    else:
        pass
    hour = date_plain[11:13]
    if int(hour) > 23 or int(hour) < 0:
        print('Error: Hours are between 0 and 23')
        return
    else:
        pass
    minute = date_plain[14:16]
    if int(minute) > 59 or int(day) < 0:
        print('Error: Minutes are betwee 0 and 59')
        return
    else:
        pass
    date_source = (year + '-' + month + '-' + day + ' ' + hour + ':' + minute)
    return date_source


timezone_source_default = 'Europe/Moscow'
timezone_target_default = 'Asia/Shanghai'

time = user_date(input('First date as YYYY-MM-DD hh:mm: '))
time_1 = convert_date_time(time, timezone_source_default, timezone_target_default)

time = user_date(input('Second date as YYYY-MM-DD hh:mm: '))
time_2 = convert_date_time(time, timezone_source_default, timezone_target_default)

print(time_1)
print(time_2)
