import random
noun = str(input('enter person place or thing'))
verb = str(input('enter action'))
adjective = str(input('enter feeling'))
story = 0

story1 = (f'one day a {noun} decided to meet Mr o for the date they planned. They were realy exited because they planned to {verb}. they were {adjective} after they finished {verb}ing and planed to do it again')
#story2
#story3

while story == 0:
	story = random.randint(0,3)
	if story == 1:
		print (story1)
	if story == 2:
		print('no')

	if story == 3:
		print('no')




