

class Time():
	def __init__(self):
		self.game_time = "day"

	def isDay(self):
		if self.game_time == "day":
			return True
		else:
			return False