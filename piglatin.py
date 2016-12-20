import string
sentance = '''
This is my English to Pig Latin translator!
 It will do the proper translations for words beginning with vowels, 
 and will account for most punctuation and re-capitalize words at the start of sentances.
 It's pretty neat!
'''
sentance = sentance.split() #turns sentance into a list for easier translation
roughpig = ''				#will be the rough translation before punctuation sorting
pig = ''					#final translation
vowels = [
'a','A',
'e','E',
'i','I',
'o','O',
'u','U']
punctuation = [
'!',',','.','?',
'"',';',':','/']
consonantCaps = [
'B','C','D','F',
'G','H','J','K',
'L','M','N','P',
'Q','R','S','T',
'U','V','W','X',
'Y','Z']
def translator(word):
	global vowels
	global consonantCaps
	if word[0] in vowels:
		translatorProduct = word + 'yay'
	elif word[0] in consonantCaps:
		firstletter = string.lower(word[0])
		word = word[1:]
		translatorProduct = word + firstletter + 'ay'
		translatorProduct = string.capitalize(translatorProduct)
	else:
		firstletter = word[0]
		word = word[1:]
		translatorProduct = word + firstletter + 'ay'
	return translatorProduct
def punctuationcheck(word):
	position = 0
	for i in word:
		position = position + 1
		if i in punctuation:
			x = word[position-1:position]
			word = word[:position-1]+word[position:]+x		
	return word 
for i in sentance:
	roughpig = roughpig + translator(i) + ' '
roughpig = roughpig.split()
for i in roughpig:
	pig = pig + punctuationcheck(i) + ' '
print(pig)



