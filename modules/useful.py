from module import Module
import random

class Useful(Module):
	def __init__(self):
		self.modname = "Useful Bot"
		
	def parse(self, msg, cmd, user, arg):
		if self.nick in cmd and " o " in msg and "?" in msg:
			question = msg.replace(cmd, '')
			question = question.replace('?', '')
			
			possibilities = question.split(" o ")
			choice = possibilities[random.randint(0, len(possibilities) -1)]
			
			if choice:
				return self.send_message(user + ": " + choice)
			else:
				return self.ignore()
		else:
			return self.ignore()