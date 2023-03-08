import string
from random import randint, choice
import os

hidden_colors = ['BlueGreen','Cyan','Green']
red_colors = ['Orange', 'Magenta', 'Red']

alphabet = string.ascii_uppercase
hidden_message = "VINGTDEUXHEURES"
message = ""
counter = 0
for l in hidden_message:
    for i in range(randint(1,3)):
        message += f"\\color{{{choice(hidden_colors)}}}{choice(alphabet)}\n"
        counter += 1
    message += f"\\color{{{choice(red_colors)}}}{l}\n"
    counter+=1

while counter%12 != 0:
    message += f"\\color{{{choice(hidden_colors)}}}{choice(alphabet)}\n"
    counter += 1

with open('template.tex','r') as f:
    doc = f.read()
    doc = doc.replace('!INPUT!', message)

with open('red.tex','w') as f:
    f.write(doc)

os.system('pdflatex red.tex')