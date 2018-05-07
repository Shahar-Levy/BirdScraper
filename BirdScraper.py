# BirdScraper

import operator
import requests
from collections import defaultdict
import matplotlib.pyplot as plt

# Getting the list of birds:
page = requests.get('http://www.californiabirds.org/main_list.txt')
birds_text = page.text
birds_list = birds_text.split('\n')

# Cleaning the list of birds:
clean_birds = []

for bird in birds_list:
    if bird.find('(') > -1:
        bird = bird[0:bird.find('(')].rstrip()
    if len(bird) - len(bird.lstrip()) == 2:
        clean_birds = clean_birds + [bird.lstrip().lower()]
sorted(set(clean_birds))
# print ('\n'.join(clean_birds))

# List of colors that appear in bird names
color_list = ('blue', 'yellow', 'green', 'red', 'black', 'gray', 'purple', 'teal',
              'white', 'olive',)

# Makes a dictionary of birds by color in name (color : color count)
colored_birds = defaultdict(list)
for count, bird in enumerate(clean_birds):
    for color in color_list:
        if color in bird:
            if color in colored_birds:
                colored_birds[color] += 1
            else:
                colored_birds[color] = 1

sorted_colored_birds = sorted(colored_birds.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_colored_birds)  # Sort in descending order

# Plot number of birds by color in name
labels, sizes = zip(*sorted_colored_birds)
colors = labels # The labels are the colors in bird's names
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black', 'linewidth':1.25}, shadow=False)
# Inner circle is a white circle overlayed on the pie chart to make a donut plot
inner_circle = plt.Circle((0, 0), 0.70, color='black', fc='white', linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(inner_circle)
plt.axis('equal')
plt.title("Percentage of each color used in birds' names")
caption = "Source: http://www.californiabirds.org/main_list.txt"
fig.text(0.5, 0.05, caption, ha='center')
plt.show()
