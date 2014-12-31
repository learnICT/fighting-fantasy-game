""" Fighting fantasy game in which you are a prince charming
	tyring to deliver the princess.
"""

from scenes import * 


class Game(object):
	
	def __init__(self):
		self.artifacts = []  # contains the artifacts that the hero will collect

	def play(self):
		scene = OpeningScene() 
		# scene.play() returns the next scene and if the games continues.
		next_scene, game_on = scene.play(self.artifacts)   
		while game_on:
			scene = next_scene
			next_scene, game_on = scene.play(self.artifacts)


game = Game()
game.play()

