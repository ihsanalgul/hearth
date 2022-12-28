import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import csv
import pandas as pd

"""
def update_graph(num):
    plt.cla() # Clear the previous graph
    plt.plot(data[:num]) # Plot the new data
    return line,

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Heart Rate')
ax.set_xlabel('Time')
ax.set_ylabel('BPM')

file = open('data.csv')

type(file)

csvreader = csv.reader(file)

data = []
for row in csvreader:
        data.append(row)
data

ani = animation.FuncAnimation(fig, update_graph, frames=range(len(data)), interval=200)

# plt.show()

ani.save('heart_rate.gif', writer='imagemagick')
"""

df = pd.read_csv('data.csv')
# type(df)
print(df.head())
df.info()
print(df.describe())

df.plot(x='time', y='bpm')

# plt.show(df.plot(x='time', y='bpm'))
