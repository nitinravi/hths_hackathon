import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style
from itertools import count
#from app import y_val
from matplotlib.animation import FuncAnimation
style.use('fivethirtyeight')
labels = ['A~2', 'A#~2', 'B~2', 'C~2', 'C#~2', 'D~2','D#~2', 'E~2', 'F~2', 'F#~2', 'G~2', 'G#~2', 'A~3', 'A#~3', 'B~3', 'C~3', 'C#~3', 'D~3', 'D#~3', 'E~3', 'F~3', 'F#~3', 'G~3', 'G#~3', 'A~4', 'A#~4', 'B~4', 'C~4', 'C#~4', 'D~4', 'D#~4', 'E~4', 'F~4', 'F#~4', 'G~4', 'G#~4']

ticks = [i for i in range(len(labels))]

plt.figure()

plt.yticks(ticks, labels)

y_vals=[]
graph_data = open('output.txt', 'r').read()
lines = graph_data.split('\n')
for line in lines:
    y_vals.append(line)
x_vals=[i for i in range(len(y_vals))]




plt.plot(x_vals,y_vals)

plt.show()