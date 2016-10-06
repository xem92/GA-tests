#GA to find the quote "to be or not to be"

import numpy as np
import random

obj = "to be or not to be"

class Individual:

	def __init__(self):
		self.fenotip = []
		self.fit = 0
		self.mutationRate = 0.01

	def setFenotip(self,f):
		self.fenotip = f
		self.mutation()

	def generate(self):
		self.fenotip = np.random.randint(30, 125, size=len(obj))

	def fitness(self):
		count = 0
		for i in range(0, len(obj)):
			if self.fenotip[i] == ord(obj[i]):
				count += 1
		self.fit = count

	def showString(self):
		return ''.join(chr(x) for x in self.fenotip)

	def mutation(self):
		for x in xrange(0,len(obj)):
			r = random.random()
			if r <= self.mutationRate:
				self.fenotip[x] = random.randint(30,125)

class GA:

	def __init__(self):
		self.population = []
		self.auxPopulation = []
		self.strongest = 50

	def genPopulation(self):
		print "Generating population"

		for i in range(0, 100):
			ind = Individual()
			ind.generate()
			ind.fitness()
			self.population.append(ind)


	def showInfo(self):
		i = 0
		for x in self.population:
			i += 1
			string = ''.join(chr(x) for x in x.fenotip)
			print "%s. String: \'%s\' -- Fit: %d" % (i , string, x.fit)

	def addStrongest(self):
		for x in xrange(0,self.strongest):
			self.auxPopulation.append(self.population[x])

	def getSon(self,f,m):
		s = Individual()
		fenotip = np.zeros(18, dtype=int)
		for x in range(0,18):
			rf = random.random()
			rm = random.random()
			if rf > rm:
				fenotip[x] = f.fenotip[x]
			else:
				fenotip[x] = m.fenotip[x]
		s.setFenotip(fenotip)
		s.fitness()
		return s

	def reproduction(self):
		self.addStrongest()
		for x in xrange(0,100-self.strongest):
			r = random.randint(0,99)
			father = self.population[r]
			r = random.randint(0,99)
			mother = self.population[r]
			son = self.getSon(father, mother)
			self.auxPopulation.append(son)

	def fit(self):
		self.genPopulation()
		i = 0
		while self.population[0].fit < 18:
			i += 1
			self.population.sort(key=lambda x: x.fit, reverse=True)
			print "\nGen %s, fit: %s, best try: %s\n" % (i, self.population[0].fit, self.population[0].showString())
			self.auxPopulation = []
			self.reproduction()
			self.population = self.auxPopulation

ga = GA()
ga.fit()