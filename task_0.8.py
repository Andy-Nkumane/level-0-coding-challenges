def number_to_hour_min(number):
    hour = number // 60
    minute = number % 60
    if hour == 1 and minute == 1:
        print(f'{hour} hour, {minute} minute')
    elif hour == 1:
        print(f'{hour} hour, {minute} minutes')
    elif minute == 1:
        print(f'{hour} hours, {minute} minute')
    else:
        print(f'{hour} hours, {minute} minutes')