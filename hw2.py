 #
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due October 1st, 2018
#

import json
import csv
import numpy as np
import os
import random
import math


def histogram_times(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    returnArr = [0] * 24
    for i in range(1, len(airplane_data)):
        if airplane_data[i][1] != None and ":" in airplane_data[i][1]:
            tempArr = airplane_data[i][1].split(":")
            if tempArr[0] == "c":
                tempArr = tempArr[1:]
            tempArr[0] = tempArr[0].replace("c", "")
            print(i)
            if int(tempArr[0]) < 24:
                returnArr[int(tempArr[0])] += 1
    return returnArr


def weigh_pokemons(filename, weight):
    returnArr = []
    with open(filename, "r") as f:
        pokedex = json.load(f)
    f.close()
    for pokemon in pokedex["pokemon"]:
        if pokemon["weight"] == str(weight) + " kg":
            returnArr.append(pokemon["name"])
    return returnArr


def single_type_candy_count(filename):
    total_candy = 0
    with open(filename, "r") as f:
        pokedex = json.load(f)
    f.close()
    for pokemon in pokedex["pokemon"]:
        if len(pokemon["type"]) == 1 and "candy_count" in pokemon:
            total_candy += pokemon["candy_count"]
    return total_candy


def reflections_and_projections(points):
    meme_points = np.copy(points)
    # reflect on y = 1
    for coord in range(0, len(meme_points)):
        meme_points[coord][1] -= 2.0 * (meme_points[coord][1] - 1.0)
    temp = np.copy(meme_points)
    # rotate pi/2
    for coord in range(0, len(temp)):
        meme_points[coord][0] = temp[coord][1] * -1.0
        meme_points[coord][1] = temp[coord][0]
    # project onto y = 3x
    for coord in meme_points:
        meme = dot(coord, [1.0, 3.0]) / 10.0
        coord[0] = meme
        coord[1] = 3.0 * meme
    return meme_points


def dot(K, L):
    if len(K) != len(L):
        return 0.0
    return sum(i[0] * i[1] for i in zip(K, L))


def normalize(image):
    p_min = image.min()
    p_max = image.max()
    return_image = np.copy(image)
    for arr in range(0, len(image)):
        for i in range(0, len(image[arr])):
            pixel = image[arr][i]
            return_image[arr][i] = ((pixel - p_min) * 255) / (p_max - p_min)
    return(return_image)


def sigmoid_normalize(image, a):
    return_image = np.copy(image)
    for arr in range(0, len(image)):
        for i in range(0, len(image[arr])):
            pixel = image[arr][i]
            pixel -= 128.0
            pixel *= (-a ** -1.0)
            pixel = 255 * ((1 + math.exp(pixel)) ** -1.0)
            return_image[arr][i] = pixel
    return return_image