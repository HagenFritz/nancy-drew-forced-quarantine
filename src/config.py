import sys
sys.path.append("./config_files/")
from Character import Nancy, Ingman
from GameTime import Time
from GameProgress import Progress

# create characters
nancy = Nancy()
ingman = Ingman()
# create game clock
game_time = Time()
# create progress check
progress = Progress()

# need to allow the user to update this
save_file = "test"