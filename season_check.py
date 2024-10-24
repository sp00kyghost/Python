#A simple if/elif check using lists 

input_month = input()
input_day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


if input_month not in months:
    print(f'Invalid')
elif input_day < 1 or input_day > 31:
    print(f'Invalid')
elif (input_month in ['April', 'June', 'September', 'November'] and input_day > 30):
    print(f'Invalid')
else:
 if (input_month == 'March' and input_day >= 20) or (input_month == 'April') or (input_month == 'May') or (input_month == 'June' and input_day < 21):
     print(f'Spring')
 elif (input_month == 'June' and input_day >= 21) or (input_month == 'July') or (input_month == 'August') or (input_month == 'September' and input_day < 22):
     print(f'Summer')
 elif (input_month == 'September' and input_day >= 22) or (input_month == 'October') or (input_month == 'November') or (input_month == 'December' and input_day < 21):
     print(f'Autumn')
 elif (input_month == 'December' and input_day >= 21) or (input_month == 'January') or (input_month == 'February') or (input_month == 'March' and input_day < 20):
     print(f'Winter')
