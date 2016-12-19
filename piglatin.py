sentance = 'try '
cut = 0		# integer to cut at the ' ' positions
lastcut = 0	# integer to cut at the last ' ' position
translator = ' '
translation = ' '
for i in sentance:
	cut += 1
	if i == ' ':
		word = sentance[lastcut:(cut-1)]
		lastcut = cut
			if word[0] == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
				translation = word + yay
			else:
				translator = word[0:1]
				translation = (word[1:] + translator + 'ay')
			print(translation)
		