'''
Author: Krutika Bapat
Purpose: This file generates the loss while training the model
'''

import sys
import matplotlib.pyplot as plt

lines = []
for line in open(sys.argv[1]):
    if "avg" in line:
        lines.append(line)

iterations = []
avg_loss = []

for j in range(len(lines)):
    lineParts = lines[j].split(',')
    iterations.append(int(lineParts[0].split(':')[0]))
    avg_loss.append(float(lineParts[1].split()[0]))

## To plot the graph for various iterations
fig = plt.figure()
for i in range(0, len(lines)):
    plt.plot(iterations[i:i+2], avg_loss[i:i+2], 'r.-')

## a and y labels for the plot
plt.xlabel('Batch Number')
plt.ylabel('Avg Loss')
fig.savefig('loss_plot.png', dpi=2000)

print('Saving plot')
