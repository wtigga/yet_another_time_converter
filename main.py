import datetime
import pytz

timezone_source_default = 'Europe/Moscow'
timezone_target_default = 'Asia/Shanghai'

def user_date():
    user_input = input('Please input current date as YYYY-MM-DD hh:mm: ')
    user_input = user_input.rstrip()
    user_input = user_input.lstrip()
    year = user_input[0:4]
    if int(year) > 2049 or int(year) < 2000:
        print('Error: Years should be between 2000 and 2049')
    else:
        pass
    month = user_input[5:7]
    if int(month) > 12 or int(month) < 1:
        print('Error: Months are between 1 and 12')
    else:
        pass
    day = user_input[8:10]
    if int(day) > 31 or int(day) < 1:
        print('Error: Days are between 1 and 30')
    else:
        pass
    hour = user_input[11:13]
    if int(hour) > 23 or int(hour) < 0:
        print('Error: Hours are between 0 and 23')
    else:
        pass
    minute = user_input[14:16]
    if int(minute) > 59 or int(day) < 0:
        print('Error: Minutes are betwee 0 and 59')
    else:
        pass
    date_source = (year + '-' + month + '-' + day + ' ' + hour + ':' + minute)
    return(date_source)

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
    date_time_list = {'YYYY': year, 'MM': month, 'DD': day, 'HH': hour, 'mm': minute}
    return date_time_list

'''
date_from_user = input('Please input current date as YYYY-MM-DD hh:mm: ')
print(convert_date_time(date_from_user, timezone_source_default, timezone_target_default))
'''

print(convert_date_time(user_date(), timezone_source_default, timezone_target_default))

months_ru_type1 = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября',  '11': 'ноября', '12': 'декабря'}



# template_ru_1 = (f'{DD_1} {MM_1_type1} {YYYY_1} г.')

# print(template_ru_1)

