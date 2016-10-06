#GA MAXONE problem

import numpy as np
import random

def genPopulation():
	print "Generating population"
	popu = []
	for individuals in range(0, 20):
		individual = np.random.randint(2, size=10)
		fit = np.sum(individual)
		popu.append([individual, fit])
	return popu

def newGeneration(popu):
	#Generate 5 new individuals by Creossover
	for i in range(0,9):
		newIn = []
		for j in range(0,7):
			newIn.append(popu[i*2][0][j])
		for j in range(7,10):
			newIn.append(popu[(i*2)+1][0][j])
		indi = np.array(newIn)
		fit = np.sum(indi)
		popu.append([indi,fit])
	#Random mutation
	for i in range(0,20):
		randMut = random.randint(0,10)
		if randMut < 10:
			if popu[i][0][randMut] == 0:
				popu[i][0][randMut] = 1
				popu[i][1] += 1
			else:
				popu[i][0][randMut] = 0
				popu[i][1] -= 1

	return popu

def selection(popu):
	for i in range(0,9):
		popu.pop(-1)
	popu.sort(key=lambda x: x[1], reverse=True)
	return popu

if __name__ == "__main__":
	gen = 0
	#Generating population
	popu = genPopulation()
	
	#Sonting population
	popu.sort(key=lambda x: x[1], reverse=True)

	while popu[0][1] < 10:
		print gen
		#Kill the weakest individuals
		popu = selection(popu)
		#Generating new generation
		popu = newGeneration(popu)
		gen += 1
	print popu[0]
