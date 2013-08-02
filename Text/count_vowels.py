# Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

string = ""
while string.upper() != 'QUIT':
	string = raw_input("Enter a string to have it vowelized or 'quit' to exit: ")

	if string.upper() != 'QUIT':
		vowels = ['a', 'e', 'i', 'o', 'u']
		vowels_count = 0
		for vowel in vowels:
			print "{0} appeared {1} time(s).".format(vowel, string.lower().count(vowel))
			vowels_count += string.lower().count(vowel)

		print "{0} vowels appeared in total.".format(vowels_count)

print 'Bbye!'