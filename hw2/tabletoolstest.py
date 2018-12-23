def assertEqual(actual, expect):
	passed = actual == expect
	if passed:
		global _passed
		_passed += 1
	else:
		global _failed
		_failed += 1

	print('pass' if passed else 'FAIL! Expected %s to equal %s' % (actual, expect))

def assertInstance(actual, expect):
	passed = isinstance(actual, expect)
	if passed:
		global _passed
		_passed += 1
	else:
		global _failed
		_failed += 1


	print('pass' if passed else 'FAIL! Expected %s to be instance of %s' % (actual, expect))

def test_print(testFunc):
	print('++ %s' % testFunc.__name__)
	testFunc()
	print('')


def test_LabeledList_get__single_key():
	foo = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	assertInstance(foo[1], LabeledList)

	expected = LabeledList([1], ['k1'])
	assertEqual(str(foo['k1']), str(expected))

	expected = LabeledList([2], ['k2'])
	assertEqual(str(foo['k2']), str(expected))

	expected = LabeledList([4], ['k4'])
	assertEqual(str(foo['k4']), str(expected))
	expected = LabeledList([])
	assertEqual(str(foo['k3']), str(expected))

def test_LabeledList_get__list_keys():
	foo = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	assertInstance(foo[[1, 2]], LabeledList)

	# 2 keys
	expected = LabeledList([1, 2], ['k1', 'k2'])
	assertEqual(str(foo[['k1', 'k2']]), str(expected))
	assertEqual(str(foo[['k2', 'k1']]), str(expected))

	# 2 keys
	expected = LabeledList([2, 4], ['k2', 'k4'])
	assertEqual(str(foo[['k2', 'k4']]), str(expected))
	assertEqual(str(foo[['k4', 'k2']]), str(expected))

	# 2 keys
	expected = LabeledList([1, 4], ['k1', 'k4'])
	assertEqual(str(foo[['k1', 'k4']]), str(expected))
	assertEqual(str(foo[['k4', 'k1']]), str(expected))

	# 1 key
	expected = LabeledList([1], ['k1'])
	assertEqual(str(foo[['k1']]), str(expected))

	# No key
	expected = LabeledList([])
	assertEqual(str(foo[['k3']]), str(expected))

	# 1 key, no key
	expected = LabeledList([1], ['k1'])
	assertEqual(str(foo[['k1', 'k3']]), str(expected))
	assertEqual(str(foo[['k3', 'k1']]), str(expected))


def test_LabeledList_get__LabeledList_key():
	foo = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	bar = LabeledList([1, 2], ['k1', 'k2'])

	assertInstance(foo[bar], LabeledList)

	# bar is subset
	expected = LabeledList([1, 2], ['k1', 'k2'])
	assertEqual(str(foo[bar]), str(expected))

	bar = LabeledList([2, 4], ['k2', 'k4'])
	expected = LabeledList([2, 4], ['k2', 'k4'])
	assertEqual(str(foo[bar]), str(expected))

	bar = LabeledList([1], ['k1'])
	expected = LabeledList([1], ['k1'])
	assertEqual(str(foo[bar]), str(expected))

	# bar not subset
	bar = LabeledList([1, 3], ['k1', 'k3'])
	expected = LabeledList([1], ['k1'])
	assertEqual(str(foo[bar]), str(expected))

	bar = LabeledList([1, 2, 4, 5], ['k1', 'k2', 'k4', 'k5'])
	expected = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	assertEqual(str(foo[bar]), str(expected))

	# empty output
	bar = LabeledList([3], ['k3'])
	expected = LabeledList([])
	assertEqual(str(foo[bar]), str(expected))

	bar = LabeledList([3, 5], ['k3', 'k5'])
	expected = LabeledList([])
	assertEqual(str(foo[bar]), str(expected))

def test_LabeledList_get__boolean():
	foo = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	assertInstance(foo[[False, False, True]], LabeledList)

	# subset
	expected = LabeledList([4], ['k4'])
	assertEqual(str(foo[[False, False, True]]), str(expected))

	expected = LabeledList([1, 4], ['k1', 'k4'])
	assertEqual(str(foo[[True, False, True]]), str(expected))

	expected = LabeledList([1, 2, 4], ['k1', 'k2', 'k4'])
	assertEqual(str(foo[[True, True, True]]), str(expected))

	# empty
	expected = LabeledList([])
	assertEqual(str(foo[[False, False, False]]), str(expected))
	assertEqual(str(foo[[False, False]]), str(expected))
	assertEqual(str(foo[[False, False, False, True]]), str(expected))

def test_LabeledList_set():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([1, 100, 100, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	foo['BB'] = 100
	assertEqual(str(foo), str(expected))

	# Change non existent key (super)
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	foo['BBB'] = 500
	assertEqual(str(foo), str(expected))

	# Change non existent key (sub)
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	foo['C'] = 500
	assertEqual(str(foo), str(expected))

	# Change single value
	foo = LabeledList([1], ['A'])
	expected = LabeledList(['bar'], ['A'])
	foo['A'] = 'bar'
	assertEqual(str(foo), str(expected))

def test_LabeledList_iter():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = [1, 2, 3, 4, 5]
	i = 0
	for val in foo:
		assertEqual(val, expected[i])
		i += 1

	# No keys
	foo = LabeledList([1, 2, 3, 4, 5])
	expected = [1, 2, 3, 4, 5]
	i = 0
	for val in foo:
		assertEqual(val, i + 1)
		i += 1

	# No values and keys
	foo = LabeledList([], [])
	i = 0
	for val in foo:
		i += 1
	assertEqual(i, 0)

def test_LabeledList_eq():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([False, True, False, False, False], ['A', 'BB', 'BB', 'CCC', 'D'])
	assertEqual(str(foo == 2), str(expected))

	foo = LabeledList([1, 2], ['x', 'y'])
	expected = LabeledList([True, False], ['x', 'y'])
	assertEqual(str(foo == 1), str(expected))

	foo = LabeledList([])
	expected = LabeledList([])
	assertEqual(str(foo == 1), str(expected))

def test_LabeledList_ne():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([True, False, True, True, True], ['A', 'BB', 'BB', 'CCC', 'D'])
	assertEqual(str(foo != 2), str(expected))

	foo = LabeledList([1, 2], ['x', 'y'])
	expected = LabeledList([False, True], ['x', 'y'])
	assertEqual(str(foo != 1), str(expected))

	foo = LabeledList([])
	expected = LabeledList([])
	assertEqual(str(foo != 1), str(expected))

def test_LabeledList_gt():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([False, False, True, True, True], ['A', 'BB', 'BB', 'CCC', 'D'])
	assertEqual(str(foo > 2), str(expected))

	foo = LabeledList([1, 2], ['x', 'y'])
	expected = LabeledList([False, True], ['x', 'y'])
	assertEqual(str(foo > 1), str(expected))

	foo = LabeledList([])
	expected = LabeledList([])
	assertEqual(str(foo > 1), str(expected))

def test_LabeledList_lt():
	foo = LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	expected = LabeledList([True, False, False, False, False], ['A', 'BB', 'BB', 'CCC', 'D'])
	assertEqual(str(foo < 2), str(expected))

	foo = LabeledList([-1, 2], ['x', 'y'])
	expected = LabeledList([True, False], ['x', 'y'])
	assertEqual(str(foo < 1), str(expected))

	foo = LabeledList([])
	expected = LabeledList([])
	assertEqual(str(foo < 1), str(expected))

def test_LabeledList_map():
	squared = lambda n: n**2
	foo = LabeledList([5, 6, 7]).map(squared)
	expected = LabeledList([25, 36, 49])
	assertEqual(str(foo), str(expected))

	foo = LabeledList([]).map(squared)
	expected = LabeledList([])
	assertEqual(str(foo), str(expected))

	iden = lambda n: n
	foo = LabeledList([5, 6, 7]).map(iden)
	expected = LabeledList([5, 6, 7])
	assertEqual(str(foo), str(expected))


LabeledList = None

def __init_counts():
	global _passed
	global _failed
	_passed = 0
	_failed = 0

def test_suite(*args):
	__init_counts()

	for test in args:
		test_print(test)

	if (_failed > 0):
		print('[-] Passed: %d, Failed: %d' % (_passed, _failed))
	else:
		print('[+] Passed: %d' % (_passed))

def test(ll):
	global LabeledList
	LabeledList = ll

	__init_counts()
	''' LabeledList '''
	test_print(test_LabeledList_get__single_key)
	test_print(test_LabeledList_get__list_keys)
	test_print(test_LabeledList_get__LabeledList_key)
	test_print(test_LabeledList_get__boolean)
	test_print(test_LabeledList_set)
	test_print(test_LabeledList_iter)
	test_print(test_LabeledList_eq)
	test_print(test_LabeledList_ne)
	test_print(test_LabeledList_gt)
	test_print(test_LabeledList_lt)
	test_print(test_LabeledList_map)

	if (_failed > 0):
		print('[-] Passed: %d, Failed: %d' % (_passed, _failed))
	else:
		print('[+] Passed: %d' % (_passed))
