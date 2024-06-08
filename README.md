# This is my simple Project
This is just a simple project to show the use of a package

![Result](https://github.com/iris-mygh/PyPI_package_samples_pl/blob/main/logs/img3.JPG)

# Document
- See more at the [link](https://github.com/iris-mygh/PyPI_package_samples_pl/blob/main/NoteN.md)

```
import matplotlib.pyplot as plt
import numpy as np

def draw_circle_with_symbol(radius, symbol, resolution=100, filename="circle.png"):
    """
    Draw a circle with a given radius and fill it with the specified symbol, then save the image.

    Args:
        radius (int): The radius of the circle.
        symbol (str): The character to fill the circle.
        resolution (int): The resolution for the grid, determining the smoothness of the circle's outline.
        filename (str): The name of the file to save the image.
    """
    # Create an array of points (theta) from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, resolution)
    # Calculate the x and y coordinates of the circle's outline
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Create a new figure and axes
    fig, ax = plt.subplots()

    ax.plot(x, y, color='white')

    # Fill the circle's outline with the specified symbol
    for i in range(0, resolution):
        ax.text(x[i], y[i], symbol, fontsize=10, ha='center', va='center', color='blue')

    # Set the aspect ratio to be equal, so the circle isn't distorted
    ax.set_aspect('equal')

    # Remove the axes
    ax.axis('off')

    # Save the image to a file
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)

    # Print a message that the image has been saved
    print(f"Image saved to '{filename}'")

    # Close the figure to free up memory
    plt.close(fig)

```