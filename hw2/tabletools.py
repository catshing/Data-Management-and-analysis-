import pdb
from functools import reduce

TABLE_STR_SPACING = 2

def longest_str(lst):
	lst_strings = map(str, lst)
	lengths = list(map(len, lst_strings))
	return reduce(max, lengths) if len(list(lengths)) > 0 else 0

'''
how many people have the last name, apple?
t[t['last'] == 'apple'].shape()[0]

what is the first name and number of fruits eaten / week of everyone that eats more than 10 fruits a week
t[t['weekly_fruits_eaten'] > 10][['first', 'weekly_fruits_eaten']]

# how many people have a first name less than 4 letters eat less than 10 fruit / week?
def length_less_than(n):
    def is_length_less_than_n(s):
        return len(s) < n
    return is_length_less_than_n
first_name_three = t[t['first'].map(length_less_than(4))]
first_name_three[first_name_three['weekly_fruits_eaten'] < 10]
'''
def is_boolean_list(lst):
	if (not isinstance(lst, list) or len(lst) == 0):
		return False
	non_bools = filter(lambda x: not isinstance(x, bool), lst)
	return len(list(non_bools)) == 0

def get_indices(lst, search_lst):
	return [i for i, v in enumerate(lst) if search_lst.count(v) > 0]

def get_values(lst, indices):
	return [v for i, v in enumerate(lst) if indices.count(i) > 0]

def get_indices_dup(lst, search_lst):
	return [lst.index(i) for i in search_lst if i in lst]

def get_values_dup(lst, indices):
	length = len(lst)
	return [lst[i] for i in indices if i < length]

def set_values(lst, indices, val):
	for i in indices:
		lst[i] = val

def lst_compare(lst, comparator):
	return [True if comparator(v) else False for v in lst]

'''
- Acts like a dictionary. Iter erturns values (not key)
- Comparison operator -- w/ scalar compares against each value returning 
new LabeledList of only bool values
- Duplicate keys allowed

ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
ll['A'] # gives back value at label 'A'
ll['BB'] # gives back new LabeledList composed of labels 'BB' and their values
ll[['A', 'D', 'BB', 'BB']] # gives back new LabeledList composed of the labels specified in list... along with their values
ll > 2 # gives back a new LabeledList composed of labels in original, along with boolean results of comparison
'''

STR_DEC = '"""'

class LabeledList:
	def __init__(self, data=None, index=None):
		self.values = data
		self.index = index if index != None else range(len(data))

	def __str__(self):
		length = len(self.index)
		out = [STR_DEC]
		max_idx_len = longest_str(self.index)
		max_val_len = longest_str(self.values)

		for i in range(length):
			val_str = str(self.values[i]).rjust(max_val_len)
			idx_str = str(self.index[i]).rjust(max_idx_len)
			out.append(' '.join([idx_str, val_str]))

		out.append(STR_DEC)

		return '\n'.join(out)

	'''
	Takes in 3 possible arguments:
		- string key 		: get all values with key
		- list of keys  	: get all values with keys
		- list of booleans 	: 
		- labeledlist   	: same as list keys but get from .values
	'''
	def __getitem__(self, key_list):
		'''
		1- get indices of keys in self.index
		2'- get keys of found indices in self.index
		2'- get values of found indices in self.values
		'''
		# pdb.set_trace()

		indices = []

		if isinstance(key_list, LabeledList):
			indices = get_indices(self.index, key_list.index)
		elif isinstance(key_list, list):
			if is_boolean_list(key_list):
				'''
				Get indices of True in argument s.t [False, True, True]
				return [1, 2]
				'''
				indices = get_indices(key_list, [True])
			else:
				indices = get_indices(self.index, key_list)
		else:
			indices = get_indices(self.index, [key_list])

		indexes2 = get_values(self.index, indices)
		values = get_values(self.values, indices)
		return LabeledList(values, indexes2)

	'''
	Setting BB to 100 will change all of its values to 100
	ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])

	ll['BB'] = 100
	"""
	  A   1
	 BB 100
	 BB 100
	CCC   4
	  D   5
	"""
	'''
	def __setitem__(self, key, value):
		key_indices = get_indices(self.index, [key])
		set_values(self.values, key_indices, value)

	def __iter__(self):
		return iter(self.values)

	def __eq__(self, scalar):
		values = lst_compare(self.values, lambda x: x == scalar)
		return LabeledList(values, self.index)

	def __ne__(self, scalar):
		values = lst_compare(self.values, lambda x: x != scalar)
		return LabeledList(values, self.index)

	def __gt__(self, scalar):
		values = lst_compare(self.values, lambda x: x > scalar)
		return LabeledList(values, self.index)

	def __lt__(self, scalar):
		values = lst_compare(self.values, lambda x: x < scalar)
		return LabeledList(values, self.index)

	def map(self, f):
		return LabeledList([f(v) for v in self.values], self.index)

	TABLE_STR_SPACING = 2

def get_cols(array_2d, indices):
	data = []
	for row in array_2d:
		sub_row = []
		for index in indices:
			sub_row.append(row[index])
		data.append(sub_row)
	return data

def get_rows(array_2d, indices):
	idx_set = set(indices)
	return [row for i, row in enumerate(array_2d) if i in idx_set]

def to_float(d):
	try:
		return float(d)
	except ValueError:
		return d

'''
self.values - contains the values in this Table as a list
t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])
.values # [[1, 2, 3],[4, 5, 6]]

self.index - contains the row labels in this Table as a list
t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])
t.index # ['a', 'b']

self.columns - contains the column names in this Tabled as a list
t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])
t.index # ['x', 'y', 'z']
'''
class Table:
	def __init__(self, values, index=None, columns=None):
		self.values = values 	# data
		self.index = index if index != None else list(range(len(values))) # row labels
		self.columns = columns if columns != None else list(range(len(values[0]))) # column labels

	def __str__(self):
		print_list = []
		print_list.append([''] + self.columns) # first row is just column labels

		for v_i in range(len(self.index)):
			print_list.append([self.index[v_i]] + self.values[v_i])

		max_col_lens = []

		for col_i in range(len(self.columns) + 1):
			col = [x[col_i] for x in print_list]
			max_col_lens.append(longest_str(col))

		col_strs = []
		for r_i in range(len(self.index) + 1):
			row_strs = []
			for c_i in range(len(self.columns) + 1):
				row_strs.append(str(print_list[r_i][c_i]).rjust(max_col_lens[c_i]))
			col_strs.append((' ' * TABLE_STR_SPACING).join(row_strs))

		return '"""\n%s\n"""' % ('\n'.join(col_strs))

	def __repr__(self):
		return self.__str__()

	def _getColumns(self, column_indices):
		sub_cols = get_values_dup(self.columns, column_indices)
		sub_data = get_cols(self.values, column_indices)
		return Table(sub_data, self.index.copy(), sub_cols)

	'''
	Lists will duplicate columns if duplicates in list. Single returns all columns
	with same key. 
	'''
	def __getitem__(self, key):
		if(is_boolean_list(key)):
			row_indices = get_indices(key, [True])
			sub_data = get_values(self.values, row_indices)
			sub_rows = get_values(self.index, row_indices)
			return Table(sub_data, sub_rows, self.columns)
		elif(isinstance(key, LabeledList)):
			column_indices = get_indices_dup(self.columns, key.values)
			return self._getColumns(column_indices)
		elif(isinstance(key, list)):
			column_indices = get_indices_dup(self.columns, key)
			return self._getColumns(column_indices)
		else:
			column_indices = get_indices(self.columns, [key])
			return self._getColumns(column_indices)

	def __eq__(self, other):
		return self.values == other.values and self.index == other.index and self.columns == other.columns 

	def __ne__(self, other):
		return not self.__eq__(other)

	def head(self, i):
		sub_data = self.values[:i]
		sub_index = self.index[:i]
		return Table(sub_data, sub_index, self.columns)

	def tail(self, i):
		num_rows = len(self.index)
		sub_data = self.values[num_rows - i:num_rows]
		sub_index = self.index[num_rows - i:num_rows]
		return Table(sub_data, sub_index, self.columns)

	def shape(self):
		return (len(self.values), len(self.values[0]))

def read_csv(filename):
	raw_datas = []
	with open(filename, 'r') as csv:
		raw_datas = csv.readlines()

	split_data = [r.strip().split(',') for r in raw_datas]
	columns = split_data[0][1:]
	row_labels =[r[0] for r in split_data[1:]]
	data = [list(map(to_float, r[1:])) for r in split_data[1:]]
	return Table(data, row_labels, columns)

# if __name__ == '__main__':
# 	import tabletoolstest as tt_test

# 	''' utils '''
# 	def test_longest_str():
# 		tt_test.assertEqual(longest_str(['a', 'bbbb', 'cc']), 4)
# 		tt_test.assertEqual(longest_str(['aaaaaa', 'bbbb', 'cc']), 6)
# 		tt_test.assertEqual(longest_str(['a', 'b', 'c']), 1)
# 		tt_test.assertEqual(longest_str(['aaa']), 3)
# 		tt_test.assertEqual(longest_str([]), 0)

# 		tt_test.assertEqual(longest_str([1, 1111, 11]), 4)
# 		tt_test.assertEqual(longest_str([222222, 1001, 33]), 6)
# 		tt_test.assertEqual(longest_str([0, 1, 2]), 1)
# 		tt_test.assertEqual(longest_str([456]), 3)
# 		tt_test.assertEqual(longest_str([]), 0)

# 	def test_is_boolean_list():
# 		tt_test.assertEqual(is_boolean_list([True]), True)
# 		tt_test.assertEqual(is_boolean_list([False]), True)
# 		tt_test.assertEqual(is_boolean_list([True, True, False]), True)
# 		tt_test.assertEqual(is_boolean_list([False, False, False]), True)

# 	def test_is_boolean_list_neg():
# 		tt_test.assertEqual(is_boolean_list([]), False)
# 		tt_test.assertEqual(is_boolean_list([1]), False)
# 		tt_test.assertEqual(is_boolean_list([0]), False)
# 		tt_test.assertEqual(is_boolean_list([1, 0, 2]), False)
# 		tt_test.assertEqual(is_boolean_list(['true']), False)

# 	def test_get_indices():
# 		tt_test.assertEqual(get_indices(['A','B','C','B'], ['B']), [1,3])
# 		tt_test.assertEqual(get_indices(['A','A','A','B'], ['A']), [0,1,2])
# 		tt_test.assertEqual(get_indices(['C','B','C','B'], ['B']), [1,3])
# 		tt_test.assertEqual(get_indices(['A','A','A','A','B'], ['A']), [0,1,2,3])

# 	def test_get_indices_neg(): 
# 		tt_test.assertEqual(get_indices(['A','B','C','B'], ['D']), [])
# 		tt_test.assertEqual(get_indices([], 'A'), [])

# 	def test_get_values():
# 		tt_test.assertEqual(get_indices(['C','B','C','B'], ['B']), [1,3])
# 		tt_test.assertEqual(get_indices(['A','B','C','B'], ['A']), [0])
# 		tt_test.assertEqual(get_indices(['A','A','A','B'], ['A']), [0,1,2])

# 	def test_get_values_neg(): 
# 		tt_test.assertEqual(get_indices(['A','A','A','A','B'], [-9]), [])
# 		tt_test.assertEqual(get_indices(['A','A','A','A','B'], []), [])
# 		tt_test.assertEqual(get_indices(['A','A','A','A','B'], [100]), [])

# 	def test_lst_compare():
# 		equals = lambda x: x == 2
# 		tt_test.assertEqual(lst_compare([1,2,3], equals), [False, True, False])
# 		tt_test.assertEqual(lst_compare([2,2,3], equals), [True, True, False])
# 		tt_test.assertEqual(lst_compare([1,2,3], equals), [False, True, False])
# 		tt_test.assertEqual(lst_compare([], equals), [])

# 		n_equals = lambda x: x != 2
# 		tt_test.assertEqual(lst_compare([1,2,3], n_equals), [True, False, True])
# 		tt_test.assertEqual(lst_compare([2,2,3], n_equals), [False, False, True])
		
# 		less = lambda x: x < 2
# 		tt_test.assertEqual(lst_compare([1,2,3], less), [True, False, False])
# 		tt_test.assertEqual(lst_compare([-2,2,3], less), [True, False, False])
		
# 		greater = lambda x: x > 2
# 		tt_test.assertEqual(lst_compare([1,2,3], greater), [False, False, True])
# 		tt_test.assertEqual(lst_compare([-2,2,3], greater), [False, False, True])

# 	tt_test.test_suite(
# 		test_longest_str,
# 		test_is_boolean_list,
# 		test_is_boolean_list_neg,
# 		test_get_indices,
# 		test_get_indices_neg,
# 		test_get_values,
# 		test_get_values_neg,
# 		test_lst_compare
# 	)

# 	tt_test.test(LabeledList) 

