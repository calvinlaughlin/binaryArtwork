# generator.py
# By Calvin Laughlin, December 2021
# This algorithm generates binary artwork (with or without a grid).
# The finished products are placed in a folder with a desired name.

import csv
import random
from PIL import Image, ImageDraw
from alive_progress import alive_bar
import time

# makeSingleArt
# Creates a single grid binary artwork from an input word and saves it to the 'singles' folder
def makeSingleArt(word, color="random"):
    height = 200 + (len(word) * 100)
    bin = ' '.join(format(ord(i), '08b') for i in word)
    converted = bin.split()
    img = Image.new("RGB", (800, height))
    x = 0
    y = 100
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    if (color != "random"):
        rgb = color
    makeLine(0, 0, img, rgb)
    for element in converted:
        for i in element:
            if i == "1":
                one = ImageDraw.Draw(img)
                one.rectangle([(x, y), (x + 100, y + 100)], fill=rgb)
            else:
                zero = ImageDraw.Draw(img)
                zero.rectangle([(x, y), (x + 100, y + 100)], fill="white", outline=rgb)
            x += 100
        x = 0
        y += 100
    makeLine(0, y, img, rgb)
    img.save('/Users/calvinlaughlin/PycharmProjects/binaryArtwork/singles/' + word + '.png', 'PNG')

# makeline
# This function creates a blank grid line.
def makeLine(x, y, img, rgb):
    for z in range(8):
        line = ImageDraw.Draw(img)
        line.rectangle([(x, y), (x + 100, y + 100)], fill="white", outline=rgb)
        x += 100

# generateArt
# This function generates binary art from a csv fileName and downloads them to folder.
# It is in the style of the classic binary art, i.e. no grid lines.
def generateArt(fileName, folder):
    file = open(fileName)
    csvReader = csv.reader(file)
    next(csvReader)
    rows = []
    for row in csvReader:
        rows.append(row[1])
    for word in rows:
        height = 200 + (len(word) * 100)
        bin = ' '.join(format(ord(i), '08b') for i in word)
        converted = bin.split()
        img = Image.new("RGB", (800, height))
        top = ImageDraw.Draw(img)
        top.rectangle([(0, 0), (800, 100)], fill="white")
        x = 0
        y = 100
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        for element in converted:
            for i in element:
                if i == "1":
                    one = ImageDraw.Draw(img)
                    one.rectangle([(x, y), (x + 100, y + 100)], fill=rgb)
                else:
                    zero = ImageDraw.Draw(img)
                    zero.rectangle([(x, y), (x + 100, y + 100)], fill="white")
                x += 100
            x = 0
            y += 100
        bottom = ImageDraw.Draw(img)
        bottom.rectangle([(0, y), (800, y + 100)], fill="white")
        img.save('/Users/calvinlaughlin/PycharmProjects/binaryArtwork/' + folder + '/' + word + '.png', 'PNG')

# generateGridArt
# This function creates binary art from a csv fileName and downloads them into folder.
# It does so with the new grid style of binary art.
def generateGridArt(fileName, folder):
    file = open(fileName)
    csvReader = csv.reader(file)
    next(csvReader)
    rows = []
    for row in csvReader:
        rows.append(row[1])
    for word in rows:
        height = 200 + (len(word) * 100)
        bin = ' '.join(format(ord(i), '08b') for i in word)
        converted = bin.split()
        img = Image.new("RGB", (800, height))
        x = 0
        y = 100
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        makeLine(0, 0, img, rgb)
        for element in converted:
            for i in element:
                if i == "1":
                    one = ImageDraw.Draw(img)
                    one.rectangle([(x, y), (x + 100, y + 100)], fill=rgb)
                else:
                    zero = ImageDraw.Draw(img)
                    zero.rectangle([(x, y), (x + 100, y + 100)], fill="white", outline=rgb)
                x += 100
            x = 0
            y += 100
        makeLine(0, y, img, rgb)
        img.save('/Users/calvinlaughlin/PycharmProjects/binaryArtwork/' + folder + '/' + word + '.png', 'PNG')