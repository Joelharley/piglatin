sentance = 'try a salad for lunch, and dinner it is a nice treat '
cut = 0					# integer to cut at the ' ' positions
lastcut = 0				# integer to cut at the last ' ' position
translator = ' '		# the first letter is cut by this
translation = ' '		# end product of individual word
fullTranslate = ''		# final product


for i in sentance:
	cut += 1
	if i == ' ':
		word = sentance[lastcut:(cut)]
		lastcut = cut
		if word[len(word)-1] == ','\
							 or '.'\
							 or '?'\
							 or '!'\
							 or '"'\
							 or "'"\
							 or '/':	# catches punctuation silly business
			punctuation = word[-1]
			word = word[:-1]
			if word[0] == 'a'\
						or 'e'\
						or 'i'\
						or 'o'\
						or 'u':	#	-	- vowel proper pronounciation for punctuation
				translation = word + 'yay'
			else:
				translation = word[1:] + translator + 'ay ' + punctuation
		if word[0] == 'a' or 'e' or 'i' or 'o' or 'u':	#	-	-	-	-	-	-	-	- vowel proper pronounciation
			translation = word + 'yay'
		else:	#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	- all other cases
			translator = word[0:1]
			translation = (word[1:] + translator + 'ay ')
			fullTranslate = fullTranslate + translation + ' '
print(len(fullTranslate))
print(fullTranslate)
		