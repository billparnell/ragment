from django.shortcuts import render
from django.http import HttpResponse
from .word_checker import checker
from .word_checker import point_getter

# Create your views here.

def index(request):

	user_input = False

	if request.method == 'GET':
		request.session.flush()
		request.session.clear_expired()
	
	if request.session.has_key('current_player'):
		current_player = request.session['current_player']
	else:
		current_player = 1

	if request.session.has_key('player_one_score'):
		player_one_score = request.session['player_one_score']
	else:
		player_one_score = 0

	if request.session.has_key('player_two_score'):
		player_two_score = request.session['player_two_score']
	else:
		player_two_score = 0

	if not request.session.has_key('my_word'):
		request.session['my_word'] = ''

	current_word = request.session['my_word']
	
	context = {}

	if request.POST.get('my_input_box'):
		user_input = request.POST.get('my_input_box').strip()

	if user_input:
		
		played_word = user_input
		turn_result = checker(current_word,played_word)

		if turn_result == 'valid_fragment' or turn_result == 'word_match':
			context['hello_world'] = played_word
			context['point_value'] = point_getter(len(played_word))
			request.session['my_word'] = played_word

			if current_player == 1:
				current_player = 2
			else:
				current_player = 1
			
		else:
			context['hello_world'] =  current_word
			context['point_value'] = point_getter(len(current_word))

		request.session['current_player'] = current_player
		context['current_player'] = current_player
		context['word_status'] = turn_result

		if turn_result == 'word_match':
			context['game_over'] = 'Round Finished!'

			# give points to player
			if current_player == 1:
				player_one_score += context['point_value']
			else:
				player_two_score += context['point_value']

			request.session.flush()
			request.session.clear_expired()

			request.session['player_one_score'] = player_one_score
			request.session['player_two_score'] = player_two_score

			context['player_one_score'] = player_one_score
			context['player_two_score'] = player_two_score

	return render(request, 'play/index.html', context)
