# -x- coding: utf-8 -x-
# Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

palindrome = ''
while palindrome.upper() != 'QUIT':
	palindrome = raw_input("Enter a string to be checked for palindromicity or 'quit' to exit: ")

	if palindrome.upper() != 'QUIT':
		print palindrome == palindrome[::-1]
