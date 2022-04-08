
# read in the sowpods dictionary and remove endline characters

def checker(original_fragment, played_fragment):

	# print(f'original fragment is {original_fragment} and played_fragment is {played_fragment}')

	with open('play/scrab_dict.txt', 'r') as f:
	  lines = f.readlines()

	scrabble_list = [l.strip() for l in lines]

	# check word fragment against sowpods dictionary and print out list of words that the fragment shows up in

	my_frag = original_fragment


	# print(f'The original word shows up in {len(match_list)} words.')

	# if match_list:
	# 	print(f'the list of words that fragment shows up in is: {match_list}')
	# else:
	# 	print('that fragment does not show up in any words in the sowpods dictionary')

	# now check if player's next play is a valid one -- player has to add exactly one letter wherever they want in the word (and leave the rest of the word untouched).  They can add a letter at the beginning, end, or in the middle.

	my_new_frag = played_fragment

	if len(my_new_frag) == len(my_frag) + 1:
		# print('cool, you added one letter')

		added_letter = ''

		temp_word_checker = list(my_new_frag)
		original_word_to_check = list(my_frag)
			
		for i in range(0,len(original_word_to_check)):
			if temp_word_checker[i] != original_word_to_check[i] and added_letter == '':
				added_letter = temp_word_checker.pop(i)

		if added_letter == '':
			added_letter = temp_word_checker.pop(-1)  # pop last letter if one hasn't popped yet

		# print(f'original word is: {my_frag}')
		# print(f'played word is: {my_new_frag}')	
		
		# print(f'added letter is {added_letter}')
		# print(f'word minus added letter (for testing) is: {"".join(temp_word_checker)}')

		if ''.join(temp_word_checker) == my_frag and added_letter.isalpha():
			# print('nice, that is a valid play for ragment')
			match_list = []

			for word in scrabble_list:
				if my_new_frag == word.lower():
					return 'word_match' # exact match, end of round
				if my_new_frag in word.lower():
					match_list.append(word)

			if len(match_list) > 0:
				# print(match_list)
				return 'valid_fragment'

			else:
				return 'invalid_fragment'



		else:
			print('sorry that is not a valid play for ragment')
			return 'invalid_fragment'


	else:
		return 'invalid_fragment'
		# print('whoops, you need to add exactly one letter')


def point_getter(n):
	if not isinstance(n, int):
		return 0
	elif n < 1:
		return 0
	elif n == 1:
		return 1
	else:
		return point_getter(n-1) + n

