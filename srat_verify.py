A = ord('A')

def qs_with_ans(qs, num, ans):
	"""Whether the requisite number of answers match the given answer."""
	c = 0
	for q in qs:
		if q in ans:
			c += 1

		if c > num:
			return False

	return c == num

def works_01(ans):
	x = ans[0]
	foo = ord(x) - A

	return 'B' == ans[foo] and 'B' not in ans[:foo]

assert not works_01('ABC')
assert not works_01('BBC')
assert not works_01('CBB')
assert works_01('CAB')

def works_02(ans):
	x = ans[1]
	foo = ord(x) - A + 5

	for i in range(len(ans) - 1):
		if ans[i] == ans[i + 1]:
			if i != foo:
				return False
		else:
			if i == foo:
				return False

	return True

assert works_02('BACDEBBA')
assert not works_02('ABCDEBBA')
assert not works_02('ACBDEABBB')
assert not works_02('ADCDEABCDDD')

def works_03(ans):
	x = ans[2]
	foo = ord(x) - A

	return qs_with_ans(ans, foo, 'E')

assert works_03('ABABA')
assert not works_03('EEAEE')
assert works_03('EEDE')
assert works_03('EEEE')

def works_04(ans):
	x = ans[3]
	foo = ord(x) - A + 4

	return qs_with_ans(ans, foo, 'A')

assert works_04('ABAAA')
assert not works_04('AAABA')
assert works_04('AAACAAA')
assert works_04('ABAEAAAAAA')

def works_05(ans):
	x = ans[4]
	foo = ord(x) - A

	return x == ans[foo]

assert works_05('AAAAE')
assert works_05('AAADD')
assert not works_05('CCACC')

def works_06(ans):
	x = ans[5]
	foo = ans[16]

	if x == 'A':
		return foo == 'C'
	elif x == 'B':
		return foo == 'D'
	elif x == 'C':
		return foo == 'E'
	elif x == 'D':
		return foo == 'A' or foo == 'B'
	else:
		return False

assert works_06('AAAAABAAAAAAAAAAD')
assert not works_06('AAAAADAAAAAAAAAAC')

def works_07(ans):
	x = ans[6]
	foo = 4 - (ord(x) - A)

	return abs(ord(x) - ord(ans[7])) == foo

assert works_07('AAAAAAAE')
assert works_07('AAAAAAEE')
assert not works_07('AAAAAAACD')

def works_08(ans):
	x = ans[7]
	foo = ord(x) - A + 4

	return qs_with_ans(ans, foo, 'AE')

assert works_08('BBBBAAAA')
assert works_08('BBAEAEABC')
assert not works_08('AAAAAAAAA')

def works_09(ans):
	x = ans[8]
	foo = ord(x) - A + 9

	return x == ans[foo] and x not in ans[9:foo]

assert works_09('EEEEEEEEAAB')
assert works_09('EEEEEEEEBAB')
assert works_09('EEEEEEEECABC')
assert not works_09('EEEEEEEEDADAD')

def works_10(ans):
	x = ans[9]
	foo = ans[15]

	if x == 'A':
		return foo == 'D'
	elif x == 'B':
		return foo == 'A'
	elif x == 'C':
		return foo == 'E'
	elif x == 'D':
		return foo == 'B'
	elif x == 'E':
		return foo == 'C'

assert works_10('AAAAAAAAABEEEEEA')
assert not works_10('AAAAAAAAADEEEEEC')

def works_11(ans):
	x = ans[10]
	foo = ord(x) - A

	return foo == ans[:10].count('B')

assert works_11('AAAAAAAAAAA')
assert not works_11('AAAAAAAAAAB')
assert works_11('BBBAAAAAABE')

def works_12(ans):
	x = ans[11]
	foo = ord(x) - A

	if foo > 1:
		return False

	return (ans.count('B') + ans.count('C') + ans.count('D')) % 2 == foo

assert not works_12('BBBBBBBBBBBB')
assert works_12('AAAAAAAAAAAB')
assert works_12('AAAAAAAAAAAA')

def works_13(ans):
	x = ans[12]
	foo = (ord(x) - A + 4) * 2

	for i in range(len(ans)):
		if i % 2 != 0: continue

		if ans[i] == 'A':
			if i != foo:
				return False
		else:
			if i == foo:
				return False

	return True

assert not works_13('BBBBBBBBBBBBA')
assert not works_13('BABBBBBBBBBBA')
assert works_13('BBBBBBBBBBABB')

def works_14(ans):
	x = ans[13]
	foo = ord(x) - A + 6

	return foo == ans.count('D')

assert works_14('ADADADADADADAABBBB')
assert not works_14('AAAAAAAAAAAAABBBBB')
assert not works_14('AAAAAAADDAAAACBBBB')
assert not works_14('DDDDDDDDDDDDDDBBBB')
assert works_14('DDADDADDADDADEDBBB')

def works_15(ans):
	x = ans[14]

	return x == ans[11]

assert works_15('AAAAAAAAAAADAAD')
assert works_15('AAAAAAAAAAABAAB')
assert not works_15('AAAAAAAAAAADAAE')

def works_16(ans):
	x = ans[15]
	foo = ans[9]

	if x == 'A':
		return foo == 'D'
	elif x == 'B':
		return foo == 'C'
	elif x == 'C':
		return foo == 'B'
	elif x == 'D':
		return foo == 'A'
	elif x == 'E':
		return foo == 'E'

assert works_16('AAAAAAAAACEEEEEB')
assert not works_16('AAAAAAAAADEEEEEE')

def works_17(ans):
	x = ans[5]
	foo = ans[:5] + ans[16] + ans[6:16] + x + ans[17:]

	return works_06(foo)

assert works_06('AAAAADAAAAAAAAAAB')
assert not works_06('AAAAACAAAAAAAAAAD')

def works_18(ans):
	x = ans[17]
	foo = ans.count('A')

	if x == 'E':
		for a in 'BCDE':
			if foo == ans.count(a):
				return False

		return True
	else:
		return foo == ans.count(chr(ord(x) + 1))

assert works_18('AAAAAAAAACCCCCCCCBC')
assert not works_18('AAAAAAAAACCCCCCCCCC')
assert works_18('AAAAAAAAACCCCCCCCED')

def works_19(ans):
	return True

assert works_19('ABCDEABCDEABCDEABCDE')

def works_20(ans):
	return ans[19] == 'E'

assert works_20('ABCDEABCDEABCDEABCDE')
assert not works_20('EDCBAEDCBAEDCBAEDCBA')

works = [eval("works_%02d" % (x + 1)) for x in range(20)]
