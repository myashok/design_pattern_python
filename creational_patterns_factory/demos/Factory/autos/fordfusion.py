from .abs_auto import AbsAuto

class FordFusion(AbsAuto):

	def start(self):
		print('%s running cooly!' % self.name)

	def stop(self):
		print('%s shutting down.' % self.name)