import pandas as pd
import numpy as np

class Progress():
	def __init__(self):
		# Medals
		self.easter_egg_count = 0
		self.nugget_clicks = 0
		self.star_wars_count = 0
		self.pan_orchestra = 0

		# Easter Eggs
		self.ufo_clicked = False
		self.duct_clicked = False
		self.xwing_clicked = False
		self.ywing_clicked = False
		self.tie_clicked = False
		self.mixer_clicked = False

		# Story progress
		self.data = pd.read_csv("../data/progress.csv",index_col="name")
		self.data.replace(0,False)
		self.data.replace(1,True)

		# Game Flags
		self.message = False
		self.message_read = False
		self.service_status = "None"
		self.made_coffee = (False,False) # (isMade, isGood)

		# Story counters
		self.message_no = 1
		self.rooms_visited = 0

	def updateTaskList(self):
		"""

		"""
		