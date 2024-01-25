
global total 
total = 0
guess = 0

class quiz():

	def __init__(self, question, ans1, ans2, ans3, ans4, correct_ans , score):
		self.question = question
		self.ans1 = ans1
		self.ans2 = ans2
		self.ans3 = ans3
		self.ans4 = ans4
		self.correct_ans = correct_ans
		self.score = score
		
	def askq(self):
		raise NotImplementedError("Subclass must implement this abstract class")
	
	def performance(self):
		print(f'TOTAL SCORE : {total}')
		
		if total>=70 :
			print('you have passed the quiz!')
		else:
			print('better luck next time')
			
		
class mcq(quiz):

	def __init__(self,question, ans1, ans2, ans3, ans4, correct_ans , score):
	
		quiz.__init__(self,question, ans1, ans2, ans3, ans4, correct_ans , score)

	def askq(self):		
		print(self.question)
		print('1. '+self.ans1)
		print('2. '+self.ans2)
		print('3. '+self.ans3)
		print('4. '+self.ans4)
		
		guess = int(input('give your ans in number: '))
		
		global total
		if guess == self.correct_ans:
			print('correct!')
			total += self.score
			
		else:
			print('wrong!')
			

class true_false(quiz):
	
	def __init__(self,question, ans1, ans2, ans3, ans4, correct_ans , score):
		
		quiz.__init__(self,question, ans1, ans2, ans3, ans4, correct_ans , score)
		
	def askq(self):
		print(self.question)
		print('1. '+self.ans1)
		print('2. '+self.ans2)
		
		guess = int(input('give your ans in number: '))
		
		global total
		if guess == self.correct_ans:
			print('correct!')
			total += self.score
			
		else:
			print('wrong!')
			
			
class user():
	
	def __init__(self, name):
		self.name = name


	def append_file(self):
		with open("scores.txt","a") as fp:
			global total
			line = self.name + ' has scored ' + str(total) + '\n'
			fp.write(line)
			total = 0

print('\n')
n = int(input('how many are going to take quiz? '))

for i in range(n):
	
	print('\n')
	name = input('enter your name :')
	print('\n')
	type = int(input('enter what type of quiz you want (1. mcq , 2. true/ false): '))
	if type == 1:
		question1 = mcq("Which one of the following river flows between Vindhyan and Satpura ranges? " , "Narmada" , "Mahanadi" , "Son" , "Netravati" , 1 , 50)
		
		question2 = mcq("The Central Rice Research Station is situated in? " , "Chennai" , " Cuttack" , "Bangalore" , "Quilon" , 2 , 50)
		
		
		
	else:
		question1 = true_false("Sharks are mammals. " , "True" , "False" , "T" , "f" , 2 , 50) 
		
		question2 = true_false("Sea otters have a favorite rock they use to break open food. " , "True" , "False" , "T" , "f" , 1 , 50) 
		
	question1.askq()
	print('\n')
	question2.askq()
	print('\n')
	
	question2.performance()
	my_user = user(name)
	my_user.append_file()
	





