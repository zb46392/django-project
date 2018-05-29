def bmi_calc(weigth, heigth):
	return weigth / (heigth * heigth)

class BmiManager:
	def __init__(self, weigth, heigth):#interne metode sa u Pythonu je konstruktor sa init
		self.weigth = weigth #svojstva u Pythonu - self
		self.heigth = heigth

	def calculate(self):
		return self.weigth / (self.heigth * self.heigth)

