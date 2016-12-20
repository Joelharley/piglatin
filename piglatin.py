import string
sentance = 'try a salad for lunch, and dinner it is a nice treat ' #what we're translating
cut = 0					# integer to cut at the ' ' positions
lastcut = 0				# integer to cut at the last ' ' position			
firstLetterSlice = ''	# the first letter is cut by this
finalProduct = ''		# final product
word = ''
vowels = [
'a','A',
'e','E',
'i','I',
'o','O',
'u','U']
punctuation = [
'!',',','.','?','/',
'"',"'",';',':']
consonantCaps = [
'B','C','D','F',
'G','H','J','K',
'L','M','N','P',
'Q','R','S','T',
'U','V','W','X',
'Y','Z']

def sentanceCutter(sentance):
	'slices input sentance into individual words'
	for i in sentance:
		global cut
		global lastcut
		cut += 1
		if i == ' ':
			word = sentance[lastcut:cut]
	return word

def translator(word):
	global vowels
	global consonantCaps
	if word[0] in vowels:
		wordProduct = word + 'yay'
	elif word[0] in consonantCaps:
		firstletter = lower(word[0])
		word = word[:0]
		wordProduct = word + firstletter + 'ay'
		wordProduct = capitalize(wordProduct)
	else:
		firstletter = word[0]
		word = word[:0]
		wordProduct = word + firstletter = 'ay'
	return wordProduct

def punctuationcheck(word):
	position = 0
	for i in word:
		position = position + 1
		if i in punctuation:
			x = word[position-1:position]
			word = word[position-1:]+word[:position]+x
	return word  



sentanceCutter(sentance)