time_1 = {'year': '2018', 'month': '01', 'day': '30', 'hour': '13', 'minute': '00'}
time_2 = {'year': '2018', 'month': '02', 'day': '15', 'hour': '10', 'minute': '59'}
language = 'ru'
chosen_template = '10'


def time_string_output(time_1, time_2, language, template_number):
    pass


months_ru = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

months_en = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

templates_ru = {
    '1': '{DD_1} {MM_1_type1} {YYYY_1} г.',
    '2': '{DD_1} {MM_1_type1}',
    '3': '{DD_1} {MM_1_type1}',
    '4': 'С {DD_1} по {DD_2} {MM_1_type1} {YYYY_1} г.',
    '5': 'С {DD_1} {MM_1_type1} по {DD_2} {MM_2_type1} {YYYY_1} г.',
    '6': 'С {DD_1} по {DD_2} {MM_1_type1} {YYYY_1} г.',
    '7': 'С {DD_1} {MM_1_type1} по {DD_2} {MM_2_type1} {YYYY_1} г.',
    '8': '{DD_1} {MM_1_type2} — {DD_2} {MM_2_type2}',
    '9': '{DD_1}-{DD_2} {MM_1_type2}',
    '10': 'С {DD_1} {MM_1_type1} {YYYY_1} г. по {DD_2} {MM_2_type1} {YYYY_2} г.',
    '11': '{DD_1} {MM_1_type2} {YYYY_1} — {DD_2} {MM_2_type2} {YYYY_2}',
    '12': '{DD_1} {MM_1_type1} в {hh}:{mm}',
    '13': '{DD_1} {MM_1_type1} с {hh_1}:{mm_2} до {hh_2}:{mm_2}',
    '14': 'С {DD_1} {MM_1_type1} {hh_1}:{mm_1} по {DD_1} {MM_1_type1} {hh_2}:{mm_2}',
    '15': 'С {DD_1} {MM_1_type1} {hh_1}:{mm_1} по {DD_2} {MM_2_type1} {hh_2}:{mm_2}',
    '16': '{DD_1}.{MM_1_type3} в {hh_1}:{mm_1}',
    '17': 'С {DD_1}.{MM_1} {hh_1}:{mm_1} по {DD_2}.{MM_2} {hh_2}:{mm_2}'
}

templates_en = {
    '1': '{MM_1_type1} {DD_1}, {YYYY_1}',
    '2': '{DD_1}th of {MM_1_type1}',
    '3': '{MM_1_type2} {DD_1}',
    '4': '{MM_1_type1} {DD_1} to {DD_2}, {YYYY_1}',
    '5': 'From {MM_1_type1} {DD_1} to {MM_2_type1} {DD_2}, {YYYY_1}',
    '6': '{MM_1_type1} {DD_1} to {DD_2}, {YYYY_1}',
    '7': 'From {MM_1_type1} {DD_1} to {MM_2_type1} {DD_2}',
    '8': '{MM_1_type2}. {DD_1} — {MM_2_type2}. {DD_2}',
    '9': '{DD_1}-{DD_2} {MM_1_type2}',
    '10': 'From {MM_1_type1} {DD_1}, {YYYY_1} to {MM_2_type1} {DD_2}, {YYYY_2}',
    '11': '{DD_1} {MM_1_type2} {YYYY_1} — {DD_2} {MM_2_type2} {YYYY_2}',
    '12': '{MM_1_type1} {DD_1} at {hh_1}:{mm_1}',
    '13': '{MM_1_type1} {DD_1} from {hh_1}:{mm_1} to {hh_2}:{mm_2}',
    '14': 'From {MM_1_type1} {DD_1}, {hh_1}:{mm_1} to {MM_2_type1} {DD_2}, {hh_2}:{mm_2}',
    '15': 'From {MM_1_type1} {DD_1}, {hh_1}:{mm_1} to {MM_2_type1} {DD_2}, {hh_2}:{mm_2}',
    '16': '{DD_1}.{MM_1_type3} at {hh_1}:{mm_1}',
    '17': 'From {MM_1_type3}/{DD_1} {hh_1}:{mm_1} to {MM_1_type3}/{DD_2} {hh_2}:{mm_2}'
}

time_1_dict = {
    'MM_1_type1': 'XXXX',
    'MM_1_type2': 'XXXX',
    'MM_1_type3': 'XXXX',
    'MM_1_type4': 'XXXX',
    'MM_1_type5': 'XXXX',
    'DD_1': 'XXXX',
    'YYYY_1': 'XXXX',
    'hh_1': 'XXXX',
    'mm_1': 'XXXX'
}

time_2_dict = {
    'MM_2_type1': 'XXXX',
    'MM_2_type2': 'XXXX',
    'MM_2_type3': 'XXXX',
    'MM_2_type4': 'XXXX',
    'MM_2_type5': 'XXXX',
    'DD_2': 'XXXX',
    'YYYY_2': 'XXXX',
    'hh_2': 'XXXX',
    'mm_2': 'XXXX'
}

months = {'ru': months_ru, 'en': months_en}
templates = {'ru': templates_ru, 'en': templates_en}


time_1_final = {
    'MM_1_type1': months.get(language).get(time_1.get('month')),
    'MM_1_type2': months.get(language).get(time_1.get('month')),
    'MM_1_type3': months.get(language).get(time_1.get('month')),
    'MM_1_type4': months.get(language).get(time_1.get('month')),
    'MM_1_type5': months.get(language).get(time_1.get('month')),
    'DD_1': time_1.get('day'),
    'YYYY_1': time_1.get('year'),
    'hh_1': time_1.get('hour'),
    'mm_1': time_1.get('minute')
}

time_2_final = {
    'MM_2_type1': months.get(language).get(time_2.get('month')),
    'MM_2_type2': months.get(language).get(time_2.get('month')),
    'MM_2_type3': months.get(language).get(time_2.get('month')),
    'MM_2_type4': months.get(language).get(time_2.get('month')),
    'MM_2_type5': months.get(language).get(time_2.get('month')),
    'DD_2': time_2.get('day'),
    'YYYY_2': time_2.get('year'),
    'hh_2': time_2.get('hour'),
    'mm_2': time_2.get('minute')
}

time_both_final = {**time_1_final, **time_2_final}

output = templates.get(language).get(chosen_template).format(**time_both_final)
print(output)



'''
date = {'YYYY_1': '2018', 'MM_1_type1': '03', 'DD_1': '16', 'hh_1': '02', 'mm_1': '59'}
template = '{DD_1} {MM_1_type1} {YYYY_1} г.'
month_words = {'MM_1_type1':(months_ru.get(date.get('MM_1_type1')))}
final = {**date, **month_words}
output = template.format(**final)
print(output)
'''


