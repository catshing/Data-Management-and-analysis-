import pdb
import tabletools as tt;


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
			max_col_lens.append(tt.longest_str(col))

		col_strs = []
		for r_i in range(len(self.index) + 1):
			row_strs = []
			for c_i in range(len(self.columns) + 1):
				row_strs.append(str(print_list[r_i][c_i]).rjust(max_col_lens[c_i]))
			col_strs.append((' ' * TABLE_STR_SPACING).join(row_strs))

		return '\n'.join(col_strs)

	def __repr__(self):
		return self.__str__()

	def _getColumns(self, column_indices):
		sub_cols = tt.get_values_dup(self.columns, column_indices)
		sub_data = get_cols(self.values, column_indices)
		return Table(sub_data, self.index.copy(), sub_cols)

	def __getitem__(self, key):
		if(tt.is_boolean_list(key)):
			row_indices = tt.get_indices(key, [True])
			sub_data = tt.get_values(self.values, row_indices)
			sub_rows = tt.get_values(self.index, row_indices)
			return Table(sub_data, sub_rows, self.columns)
		elif(isinstance(key, tt.LabeledList)):
			column_indices = tt.get_indices_dup(self.columns, key.values)
			return self._getColumns(column_indices)
		elif(isinstance(key, list)):
			column_indices = tt.get_indices_dup(self.columns, key)
			return self._getColumns(column_indices)


# TODO: write proper assert test cases
if __name__ == '__main__':
	d = [
			[1000, 10, 100, 1, 1.0],
			[200, 2, 2.0, 2000, 20],
			[3, 300, 3000, 3.0, 30],
			[40, 4000, 4.0, 400, 4],
			[7, 8, 6, 3, 41]
		]

	print('Test __str__')
	t = Table(d, ['a', 'b', 'c', 'd', 'e'], ['foo', 'bar', 'bazzy', 'qux', 'quxx'])
	print(t)
	print()

	print('Test no index and columns')
	t = Table([['foo', 'bar', 'baz'], ['qux', 'quxx', 'corge']])
	print(t)

	print('Test __repr__')
	print(t.__repr__())
	print()

	print('Test getitem w/ LabeledList')
	t = Table(d, ['foo', 'bar', 'bazzy', 'qux', 'quxx'], ['a', 'b', 'c', 'd', 'e'])
	print(t[tt.LabeledList(['a', 'b'])])
	print()

	print('Test getitem w/ list containing duplicate columns')
	t = Table([[15, 17, 19], [14, 16, 18]], columns=['x', 'y', 'z'])
	print(t[['x', 'x', 'y']])
	print()

	print('Test get item w/ boolean list')
	t = Table([[1, 2, 3], [4, 5, 6], [7, 8 , 9]], columns=['x', 'y', 'z'])
	print(t[[True, False, True]])
	print()

	print('Test get w/ dup column definition')
	pdb.set_trace()
	t = Table([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'a'])
	print(t['a'])
	print()


