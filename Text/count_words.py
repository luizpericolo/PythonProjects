# Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

string = ''
while string.upper() != 'QUIT':
	string = raw_input("Enter a text to get a summary of strings or 'quit' to exit: ")
	if string.upper() != 'QUIT':
		words = {}
		symbols = [',', '.', '!', '?', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+', '/', '\\', '{', '}']
		for word in string.split(' '):
			if word != ' ':
				for symbol in symbols:
					if word.find(symbol):
						word = word.replace(symbol, '')
				if word not in words:
					words[word] = 1
				else:
					words[word] += 1

		for word, count in words.iteritems():
			print "Word '{0}' appeared {1} time(s) in the text.".format(word, count)

print 'Bbye!'