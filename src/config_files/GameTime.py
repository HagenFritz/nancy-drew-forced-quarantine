

class Time():
	def __init__(self):
		self.game_time = "day"

	def setTime(self, time):
		self.game_time = time

	def isDay(self):
		if self.game_time == "day":
			return True
		else:
			return False