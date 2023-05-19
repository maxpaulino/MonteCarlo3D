# Monte Carlo Pi Estimation Animation

This code generates an animation using the Monte Carlo method to estimate the value of π (pi). 
The animation progressively adds more random points inside a sphere and calculates the ratio of 
points inside the sphere to the total number of points generated. This ratio is then multiplied 
by 6 to approximate the value of π.

### Requirements

- Python 3.x
- Matplotlib library

### Instructions

1. Install the required dependencies by running the following command:

```shell
pip install matplotlib
```

2. Copy and paste the provided code into a Python script file (e.g., `monte_carlo_pi_estimation.py`).

3. Run the script using the following command:

```shell
python monte_carlo_pi_estimation.py
```

4. The animation will be generated and saved as a sequence of images in the `./pics/` directory.

5. Once the script has finished running, you can convert the sequence of images into a video using third-party software or libraries.

Note: Make sure you have write permissions for the directory where the script is located and for the `./pics/` directory to save the animation frames.

### Customize the Animation

- You can adjust the `numAngles`, `totalFrames`, `startFrame`, and `p` variables to modify the animation's parameters, such as the number of angles in the sphere, the total number of frames, the starting frame, and the number of random points generated.
- The animation can be customized further by modifying the graph properties, such as colors, labels, or viewing angles, within the code.
