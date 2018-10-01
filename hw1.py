#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
	count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	with open(filename) as file:
		csv_reader = csv.reader(file, delimiter = ',')
		reader = list(csv_reader)
	for i in range(1, len(reader)):
		if reader[i][1] != None and ":" in reader[i][1]:
			#print(reader[i][1])
			time = reader[i][1]
			timehr = time[:2]
			if timehr != '':
				hour = int(timehr)
				#print(hour)
				count[hour] = count[hour] + 1
	pass

def weigh_pokemons(filename, weight):
	pokes = []
    with open(filename, 'r') as f:
        datastore = json.load(f)
    f.close()
    searchFor = str(weight) + " kg"
    for pok in datastore["pokemon"]:
    	if pok[weight] == searchFor:
    		pokes.append(pok["name"])
	return pokes
	pass

def single_type_candy_count(filename):
	candyCount = 0
	with ope(filename, "r") as file:
		datastore = json.load(file)
	f.close()
	for pok in datastore["pokemon"]:
		if "candyCount" in pok:
			if len(pok["type"]) == 1:
				candyCount = candyCount + pok["candy_count"]
    return candy_count
    pass

def reflections_and_projections(points):
	arr = np.copy(points)
	for i in range(0, len(arr)):
		store = arr[i][1]
		storeRef = (arr[i][1] - 1.0) * 2.0
		arr[i][1] = store - storeRef
	arr2 = np.copy(arr)
	for i in range(0, len(arr2)):
		arr[i][0] = -(arr2[i][1] * 1.0)
		arr[i][1] = arr2[i][0]
	for i in arr:
		num = 0
		if len(i) != len([1.0, 3.0]):
        	num = 0.0
    	else:
    		num = sum(i[0] * i[1] for i in zip(i, [1.0, 3.0]))
    	i[0] = num
    	i[1] = num * 3.0
    return arr
    pass

def normalize(image):
	maxPix = image.max()
	minPix = image.min()
	finalImg = np.copy(image)
	for i in range(0, len(image)):
		for j in range(0, len(image[i])):
			pVal = image[i][j]
			finalImg[i][j] = (255*(pVal - minPix) / (maxPix-minPix))
    return finalImg
    pass
