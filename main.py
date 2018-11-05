# coding: utf-8
import csv
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

#  function to read required info from CSV files with language related data
def read_template(filename):
    csv_delim = '\t'
    # getting the first cell content and using it as ID column
    reader = csv.reader(open(filename, 'r', encoding="utf-8"), delimiter=csv_delim)
    for row in reader:
        id_column_name = row[0]
        break
    all_rows = [] # read all rows from CSV into this list
    reader = csv.DictReader(open(filename, 'r', encoding="utf-8"), delimiter=csv_delim)  # read CSV with TAB as delimit
    for row in reader:
        all_rows.append(dict(row))
    sorted_templates = {}  # dict with all templates
    for content in all_rows:
        newdict_name = content[id_column_name]  # read type number from the line
        content.pop(id_column_name)    # remove the type column
        output = {newdict_name: content}  # create a dict with type as a key and dict as a content
        sorted_templates = {**sorted_templates, **output}
    return sorted_templates


months_1 = read_template('./localized/months_type1.csv')
months_2 = read_template('./localized/months_type2.csv')
templates = read_template('./localized/templates.csv')


def date_text_output(time_from_user_1, time_from_user_2, template_number, language):
    desired_string = (templates[template_number])[language]
    # 1 in templates stands for number in templates dict, language stands for the language in the value in the dict
    # take month num from time_from_user, find same num in months dict, find the right language by the language key

    time_formatted = {
        'MM_1_type1': (months_1[time_from_user_1['month']])[language],
        'MM_1_type2': (months_2[time_from_user_1['month']])[language],
        'DD_1': time_from_user_1['day'],
        'YYYY_1': time_from_user_1['year'],
        'hh_1': time_from_user_1['hour'],
        'mm_1': time_from_user_1['minute'],
        'MM_2_type1': (months_1[time_from_user_2['month']])[language],
        'MM_2_type2': (months_2[time_from_user_2['month']])[language],
        'DD_2': time_from_user_2['day'],
        'YYYY_2': time_from_user_2['year'],
        'hh_2': time_from_user_2['hour'],
        'mm_2': time_from_user_2['minute']
    }
    output = desired_string.format(**time_formatted)
    return output


timezone_source_default = 'Asia/Shanghai'
timezone_target_default = 'Europe/Moscow'
temp_num = '12'

# time = user_date(input('First date as YYYY-MM-DD hh:mm: '))
time = '2018-10-25 16:00'
time_1 = convert_date_time(time, timezone_source_default, timezone_target_default)

# time = user_date(input('Second date as YYYY-MM-DD hh:mm: '))
time = '2018-11-11 16:00'
time_2 = convert_date_time(time, timezone_source_default, timezone_target_default)

# lang = input('Input language')


# print(date_text_output(time_1, time_2, temp_num, lang))
print(date_text_output(time_1, time_2, temp_num, 'EN'))

