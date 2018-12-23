import mydate 

start_year = 2015
end_year = 2018

# input 2-tuples with no year
def find_duplicate_dates(month_days):
	duplicate_dates = []
	for d in month_days:
		if (d not in duplicate_dates and month_days.count(d) > 1):
			duplicate_dates.append(d)
	return duplicate_dates

def generate_birthdays(i):
	birthdays = [];
	for i in xrange(i):
		birthdays.append(mydate.generate_date(start_year, end_year))
	return birthdays

def process_birthdays(year_month_days):
	processed_birthdays = []
	month_days = mydate.remove_years(year_month_days)
	for birthday in month_days:
		birthday[0] = mydate.month_num_to_string(birthday[0])
		birthday[1] = str(birthday[1])
		processed_birthdays.append(birthday)
	return map(lambda x: ' '.join(x), processed_birthdays)
	
def run_trials(trials):
	count = 0
	for i in xrange(trials):
		birthdays = generate_birthdays(num_birthdays)
		processed_birthdays = process_birthdays(birthdays)
		duplicates = tuple(find_duplicate_dates(processed_birthdays))
		if len(duplicates) > 0:
			count += 1
			s = 's' if len(duplicates) > 1 else ''
			result = '%d date%s occur more than once! (%s)' % (len(duplicates), s, ', '.join(duplicates))
		else:
			result = 'No dates are the same.'

		print 'Trial #%d: %s' % (i + 1, result)
	return count

def calculcate_probability(num_trials, num_dups, num_birthdays):
	return (float(num_dups) / float(num_trials)) * 100

def print_results(dup_prob, num_trials, num_dups, num_birthdays):
	title = '\nResults:\n' + '=====\n'
	trials = 'Out of %d trials, %d had dates that were repeated\n' % (num_trials, num_dups)
	conclusion = 'We can conclude that you have a %0.2f%% chance of sharing a birthday with someone if you are in a group of %d people\n' % (dup_prob, num_birthdays)
	print title + trials + conclusion

if __name__ == '__main__':
	trials = int(input('How many times should I run the simulation?\n>'))
	num_birthdays = int(input('How many birthdays should I generate per trial?\n>'))
	duplicate_count = run_trials(trials)
	dup_prob = calculcate_probability(trials, duplicate_count, num_birthdays)
	print_results(dup_prob, trials, duplicate_count, num_birthdays)
