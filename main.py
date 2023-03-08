# Imports
import matplotlib.pyplot as plt
import numpy as np

# Init variables
numAngles = 180
totalFrames = 600
startFrame = 1
numInCircle = 0

xs = []
ys = []
zs = []

# Init graph
box = dict(boxstyle='round', facecolor='#f0f9e8', alpha=0.5)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection='3d')

p = 10000
ep = np.log(p)
iterations = np.linspace(start=5, stop=ep, num=totalFrames)
iterations = np.exp(iterations)
angles = np.linspace(start=1, stop=numAngles, num=totalFrames)


# Set all the random dot arrays
def set_randoms():
    i = 0
    while i < p:
        xs.append(np.random.uniform(0, 1))
        ys.append(np.random.uniform(0, 1))
        zs.append(np.random.uniform(0, 1))
        i += 1

# Calculates whether a point is inside the sphere or not
def calc_circle(i):
    global numInCircle
    for x in range(0, i):
        if 1 / 4 > np.square(xs[x] - 1 / 2) + np.square(ys[x] - 1 / 2) + np.square(zs[x] - 1 / 2): # This HAS to be correct, work on the equation
            numInCircle += 1
    # increments numInCircle  if the point lies inside the circle


# Displays the sphere onto the graph
def create_circle():
    u = np.linspace(0, 2*np.pi, 500)
    v = np.linspace(0, np.pi, 250)
    x = (np.outer(np.cos(u), np.sin(v))*0.5)+.5
    y = (np.outer(np.sin(u), np.sin(v))*0.5)+.5
    z = (np.outer(np.ones(np.size(u)), np.cos(v))*0.5)+.5
    ax.plot_surface(x, y, z, alpha=0.2, color='#43a2ca')

# Initialize the graph
def init_graph():
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))
    ax.set_zlim((0, 1))

# creates a frame for each iteration
def create_frame(iteration):
    global startFrame
    global numInCircle

    set_randoms()
    calc_circle(iteration)
    init_graph()
    create_circle()

    picalc = (numInCircle/iteration) * 6

    # Create the box
    text = '\n'.join((
        r'$\pi = {}$'.format(picalc),
        r'no. of points = {}'.format(int(np.round(iteration)))))
    for txt in ax.texts:
        txt.set_visible(False)
    ax.text2D(0.05, 1.2, text, transform=ax.transAxes, fontsize=14,
              verticalalignment='top', bbox=box)
    # Plot iteration and savefig
    ax.view_init(45, angles[startFrame - 1])
    ax.scatter(xs[0:int(iteration)], ys[0:int(iteration)], zs[0:int(iteration)], color="#0868ac")
    fig.savefig('./pics/{}.png'.format(startFrame), bbox_inches='tight')
    print(str(startFrame) + "/" + str(totalFrames))
    plt.cla()
    startFrame += 1
    numInCircle = 0


# Main method
if __name__ == '__main__':
    j = 0
    while j < totalFrames:
        create_frame(int(iterations[j]))
        j += 1




