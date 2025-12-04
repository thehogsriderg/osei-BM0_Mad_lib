import random
noun = str(input('enter person place or thing / noun'))
verb = str(input('enter action / verb'))
adjective = str(input('enter feeling / adj'))

story = 0

story1 = (f'one day, {noun} decided to meet Mr o for the date they planned. They were realy exited because they planned to {verb}. they were {adjective} after they finished {verb}ing and planed to do it again')
story2 = (f'once apon a time {noun} wanted to eat out, so he decided to {verb} to the store to get some chips. the chips made him feel so {adjective} that he {verb}ed by himself')
story3 = (f'today I went to {noun} to get some food. it was so good I {verb} to {noun} but to my {adjective} it was gone')

while story == 0:
	story = random.randint(0,3)
	if story == 1:
		print (story1)
	if story == 2:
		print(story2)
	if story == 3:
		print(story3)





