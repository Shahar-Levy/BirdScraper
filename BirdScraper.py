#BirdScrapper V2.0
import requests
from collections import defaultdict
import matplotlib.pyplot as plt

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
list(set(clean_birds))
#print ('\n'.join(clean_birds))

#Sorting the list of birds:
alphabet = dict()
for bird in clean_birds:
    character = bird[0].upper()
    if character not in alphabet:
        alphabet[character] = list()
    alphabet[character].append(bird)

#Number of birds starting with each letter
#{k:sum(1 for x in v if x) for k,v in alphabet.items()}
#for key,value in sorted(alphabet.items()):
#    print(key, sum(1 for v in value if v))

#List of colors that appear in bird names
color_list = {'blue', 'yellow', 'green', 'red', 'black', 'gray', 'purple', 'orange', 'teal',
         'white', 'olive'}

#Makes a dictionary of birds by color in name
colored_birds = defaultdict(list)
for count, bird in enumerate (clean_birds):
    for color in color_list:
        if bird.find(color) > -1:
            if not color in colored_birds:
                clean_birds[count] = list()
            colored_birds[color].append(bird)

#Counts how many birds with a color in their name
color_counter = []
for color in color_list:
    color_counter.append(len(colored_birds[color]))


#Plot number of birds by color in name
labels = color_list
sizes = color_counter
# colors = ['olive','purple','orange','yellow','teal','green','white','black','gray',
#           'blue','red']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=color_list, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.show()

