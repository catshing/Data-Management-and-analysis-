import random

def is_valid_month_num(n): 
	return 1 <= n <= 12

months = [
'January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'
]

def month_num_to_string(month_num):
	return months[month_num - 1] if 1 <= month_num <= len(months) else None

def date_to_string(date_list):
	return month_num_to_string(date_list[1]) + ' ' + str(date_list[2]) + ', ' + str(date_list[0])

def dates_to_strings(list_of_date_lists):
	list = [] 
	for i in list_of_date_lists: 
		list.append(date_to_string(i))
	return list

def remove_years(list_of_date_lists):
	removed_years = []; 
	for date_list in list_of_date_lists:
		removed_years.append(date_list[1:3])
	return removed_years

def is_leap_year(year):
	 return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_num_days_in_month(month_num, year): 
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if is_leap_year(year) and month_num == 2: 
		return month_days[1] + 1
	elif not 1 <= month_num <= len(month_days): 
		return None
	else: 
		return month_days[month_num-1]

def generate_date(start_year, end_year):
	year = random.randint(start_year, end_year)
	month = random.randint(1, 12)
	day = get_num_days_in_month(month, year)
	return [year, month, day]