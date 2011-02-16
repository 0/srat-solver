"""Functions for verifying a potential SRAT solution."""

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
	"""1. The first question whose answer is B is question
	(A) 1 (B) 2 (C) 3 (D) 4 (E) 5

	>>> works_01('ABC')
	False
	>>> works_01('BBC')
	False
	>>> works_01('CBB')
	False
	>>> works_01('CAB')
	True
	"""
	x = ans[0]
	foo = ord(x) - A

	return 'B' == ans[foo] and 'B' not in ans[:foo]

def works_02(ans):
	"""2. The only two consecutive questions with identical answers are questions
	(A) 6 and 7 (B) 7 and 8 (C) 8 and 9 (D) 9 and 10 (E) 10 and 11

	>>> works_02('BACDEBBA')
	True
	>>> works_02('ABCDEBBA')
	False
	>>> works_02('ACBDEABBB')
	False
	>>> works_02('ADCDEABCDDD')
	False
	"""
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


def works_03(ans):
	"""3. The number of questions with the answer E is
	(A) 0 (B) 1 (C) 2 (D) 3 (E) 4

	>>> works_03('ABABA')
	True
	>>> works_03('EEAEE')
	False
	>>> works_03('EEDE')
	True
	>>> works_03('EEEE')
	True
	"""
	x = ans[2]
	foo = ord(x) - A

	return qs_with_ans(ans, foo, 'E')

def works_04(ans):
	"""4. The number of questions with the answer A is
	(A) 4 (B) 5 (C) 6 (D) 7 (E) 8

	>>> works_04('ABAAA')
	True
	>>> works_04('AAABA')
	False
	>>> works_04('AAACAAA')
	True
	>>> works_04('ABAEAAAAAA')
	True
	"""
	x = ans[3]
	foo = ord(x) - A + 4

	return qs_with_ans(ans, foo, 'A')

def works_05(ans):
	"""5. The answer to this question is the same as the answer to question
	(A) 1 (B) 2 (C) 3 (D) 4 (E) 5

	>>> works_05('AAAAE')
	True
	>>> works_05('AAADD')
	True
	>>> works_05('CCACC')
	False
	"""
	x = ans[4]
	foo = ord(x) - A

	return x == ans[foo]

def works_06(ans):
	"""6. The answer to question 17 is
	(A) C (B) D (C) E (D) none of the above (E) all of the above

	>>> works_06('AAAAABAAAAAAAAAAD')
	True
	>>> works_06('AAAAADAAAAAAAAAAC')
	False
	"""
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

def works_07(ans):
	"""7. Alphabetically, the answer to this question and the answer to the following question are
	(A) 4 apart (B) 3 apart (C) 2 apart (D) 1 apart (E) the same

	>>> works_07('AAAAAAAE')
	True
	>>> works_07('AAAAAAEE')
	True
	>>> works_07('AAAAAAACD')
	False
	"""
	x = ans[6]
	foo = 4 - (ord(x) - A)

	return abs(ord(x) - ord(ans[7])) == foo

def works_08(ans):
	"""8. The number of questions whose answers are vowels is
	(A) 4 (B) 5 (C) 6 (D) 7 (E) 8

	>>> works_08('BBBBAAAA')
	True
	>>> works_08('BBAEAEABC')
	True
	>>> works_08('AAAAAAAAA')
	False
	"""
	x = ans[7]
	foo = ord(x) - A + 4

	return qs_with_ans(ans, foo, 'AE')

def works_09(ans):
	""" 9. The next question with the same answer as this one is question
	(A) 10 (B) 11 (C) 12 (D) 13 (E) 14

	>>> works_09('EEEEEEEEAAB')
	True
	>>> works_09('EEEEEEEEBAB')
	True
	>>> works_09('EEEEEEEECABC')
	True
	>>> works_09('EEEEEEEEDADAD')
	False
	"""
	x = ans[8]
	foo = ord(x) - A + 9

	return x == ans[foo] and x not in ans[9:foo]

def works_10(ans):
	"""10. The answer to question 16 is
	(A) D (B) A (C) E (D) B (E) C

	>>> works_10('AAAAAAAAABEEEEEA')
	True
	>>> works_10('AAAAAAAAADEEEEEC')
	False
	"""
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

def works_11(ans):
	"""11. The number of questions preceding this one with the answer B is
	(A) 0 (B) 1 (C) 2 (D) 3 (E) 4

	>>> works_11('AAAAAAAAAAA')
	True
	>>> works_11('AAAAAAAAAAB')
	False
	>>> works_11('BBBAAAAAABE')
	True
	"""
	x = ans[10]
	foo = ord(x) - A

	return foo == ans[:10].count('B')

def works_12(ans):
	"""12. The number of questions whose answer is a consonant is
	(A) an even number
	(B) an odd number
	(C) a perfect square
	(D) a prime
	(E) divisible by 5

	>>> works_12('BBBBBBBBBBBB')
	False
	>>> works_12('AAAAAAAAAAAB')
	True
	>>> works_12('AAAAAAAAAAAA')
	True
	"""
	x = ans[11]
	foo = ord(x) - A

	if foo > 1:
		return False

	return (ans.count('B') + ans.count('C') + ans.count('D')) % 2 == foo

def works_13(ans):
	"""13. The only odd-numbered problem with answer A is
	(A) 9 (B) 11 (C) 13 (D) 15 (E) 17

	>>> works_13('BBBBBBBBBBBBA')
	False
	>>> works_13('BABBBBBBBBBBA')
	False
	>>> works_13('BBBBBBBBBBABB')
	True
	"""
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

def works_14(ans):
	"""14. The number of questions with answer D is
	(A) 6 (B) 7 (C) 8 (D) 9 (E) 10

	>>> works_14('ADADADADADADAABBBB')
	True
	>>> works_14('AAAAAAAAAAAAABBBBB')
	False
	>>> works_14('AAAAAAADDAAAACBBBB')
	False
	>>> works_14('DDDDDDDDDDDDDDBBBB')
	False
	>>> works_14('DDADDADDADDADEDBBB')
	True
	"""
	x = ans[13]
	foo = ord(x) - A + 6

	return foo == ans.count('D')

def works_15(ans):
	"""15. The answer to question 12 is
	(A) A (B) B (C) C (D) D (E) E

	>>> works_15('AAAAAAAAAAADAAD')
	True
	>>> works_15('AAAAAAAAAAABAAB')
	True
	>>> works_15('AAAAAAAAAAADAAE')
	False
	"""
	x = ans[14]

	return x == ans[11]

def works_16(ans):
	"""16. The answer to question 10 is
	(A) D (B) C (C) B (D) A (E) E

	>>> works_16('AAAAAAAAACEEEEEB')
	True
	>>> works_16('AAAAAAAAADEEEEEE')
	False
	"""
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

def works_17(ans):
	"""17. The answer to question 6 is
	(A) C (B) D (C) E (D) none of the above (E) all of the above

	>>> works_06('AAAAADAAAAAAAAAAB')
	True
	>>> works_06('AAAAACAAAAAAAAAAD')
	False
	"""
	x = ans[5]
	foo = ans[:5] + ans[16] + ans[6:16] + x + ans[17:]

	return works_06(foo)

def works_18(ans):
	"""18. The number of questions with answer A equals the number of questions with answer
	(A) B (B) C (C) D (D) E (E) none of the above

	>>> works_18('AAAAAAAAACCCCCCCCBC')
	True
	>>> works_18('AAAAAAAAACCCCCCCCCC')
	False
	>>> works_18('AAAAAAAAACCCCCCCCED')
	True
	"""
	x = ans[17]
	foo = ans.count('A')

	if x == 'E':
		for a in 'BCDE':
			if foo == ans.count(a):
				return False

		return True
	else:
		return foo == ans.count(chr(ord(x) + 1))

def works_19(ans):
	"""19. The answer to this question is:
	(A) A (B) B (C) C (D) D (E) E

	>>> works_19('ABCDEABCDEABCDEABCDE')
	True
	"""
	return True

def works_20(ans):
	"""20. Standardized test is to intelligence as barometer is to
	(A) temperature (only)
	(B) wind-velocity (only)
	(C) latitude (only)
	(D) longitude (only)
	(E) temperature, wind-velocity, latitude, and longitude

	>>> works_20('ABCDEABCDEABCDEABCDE')
	True
	>>> works_20('EDCBAEDCBAEDCBAEDCBA')
	False
	"""
	return ans[19] == 'E'

works = [eval("works_%02d" % (x + 1)) for x in range(20)]
