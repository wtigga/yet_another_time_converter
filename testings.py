def user_input_time(default_date='2018-01-01', default_time='00:00', first_second=1):
    message_date_first = 'Start date in YYYY-MM-DD format, ENTER to use default: '
    message_date_second = 'End date in YYYY-MM-DD format, ENTER to use default: '
    message_time_first = 'Start time in hh:mm format, ENTER to use default: '
    message_time_second = 'End time in hh:mm format, ENTER to use default: '
    if first_second == 1:
        message_date = message_date_first
        message_time = message_time_first
    else:
        message_date = message_date_second
        message_time = message_time_second
    date = input(message_date)
    if date == '':
        date = default_date
    else:
        pass

    time = input(message_time)
    if time == '':
        time = default_time
    else:
        pass

    output = str(date + ' ' + time)
    return output


print(user_input_time(default_date='2018-01-01', first_second=2))

