# coding: utf-8
import csv

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


months = read_template('./localized/months_type1.csv')
templates = read_template('./localized/templates.csv')


def date_text_output(time_from_user_1, time_from_user_2, template_number, language):
    desired_string = (templates[template_number])[language]
    # 1 in templates stands for number in templates dict, language stands for the language in the value in the dict
    # take month num from time_from_user, find same num in months dict, find the right language by the language key

    time_formatted = {
        'MM_1_type1': (months[time_from_user_1['month']])[language],
        'MM_1_type2': (months[time_from_user_1['month']])[language],
        'DD_1': time_from_user_1['day'],
        'YYYY_1': time_from_user_1['year'],
        'hh_1': time_from_user_1['hour'],
        'mm_1': time_from_user_1['minute'],
        'MM_2_type1': (months[time_from_user_2['month']])[language],
        'MM_2_type2': (months[time_from_user_2['month']])[language],
        'DD_2': time_from_user_2['day'],
        'YYYY_2': time_from_user_2['year'],
        'hh_2': time_from_user_2['hour'],
        'mm_2': time_from_user_2['minute']
    }
    output = desired_string.format(**time_formatted)
    return output


temp_num = '10'
time_1 = {'year': '2017', 'month': '01', 'day': '30', 'hour': '13', 'minute': '00'}
time_2 = {'year': '2018', 'month': '02', 'day': '15', 'hour': '10', 'minute': '59'}
lang = 'RU'


print(date_text_output(time_1, time_2, temp_num, lang))