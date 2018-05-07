#BirdScraper

import operator
import requests
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd

#Getting the list of birds:
page = requests.get('http://www.californiabirds.org/main_list.txt')
birds_text=page.text
birds_list=birds_text.split('\n')

#Cleaning the list of birds:
clean_birds=[]

for bird in birds_list:
    if bird.find('(')>-1:
        bird = bird[0:bird.find('(')].rstrip()
    if len(bird) - len(bird.lstrip()) == 2:
        clean_birds = clean_birds + [bird.lstrip().lower()]
sorted(set(clean_birds))
#print ('\n'.join(clean_birds))

#List of colors that appear in bird names
color_list = ('blue', 'yellow', 'green', 'red', 'black', 'gray', 'purple', 'orange', 'teal',
         'white', 'olive','pink')

#Makes a dictionary of birds by color in name (color : color count)
colored_birds = defaultdict(list)
for count, bird in enumerate (clean_birds):
    for color in color_list:
        if color in bird:
            if color in colored_birds:
                colored_birds[color] += 1
            else:
                colored_birds[color] = 1

sorted_colored_birds = sorted(colored_birds.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_colored_birds)

#Plot number of birds by color in name
labels, sizes = zip(*sorted_colored_birds)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=labels, autopct='%1.1f%%',
         shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
