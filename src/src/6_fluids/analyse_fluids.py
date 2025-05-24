"""
Author: Mia Clark-Webb
Date: 2025-05-19
This module plots the results of the fluids solver
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Makes matplotlib work on Wayland, which is necessary for my personal system
matplotlib.use("TkAgg")


def analyse_fluids(psi_values, name, title):
    """
    This function analyses psi by plotting it on a colour-coded matplotlib
    colour map.

    Inputs:
    * psi_values: a 2D numpy array containing the approximated values of psi
        at each grid position

    Outputs:
    * (no returned values - this function just executes the process of
        exporting the graph to a png file)
    """

    # Sets up figure with title and axis labels
    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    n_psi = len(psi_values)

    # Sets up x and y values for plotting psi against
    x = np.asarray([i / (n_psi - 1) for i in range(n_psi)])
    y = np.asarray([i / (n_psi - 1) for i in range(n_psi)])

    # Sets up gradients
    u, v = np.gradient(psi_values)
    v *= -1  # flips v to the correct direction

    # Plots the graph, with every tenth (u, v) vector in each direction shown
    plt.pcolor(x, y, psi_values)
    plt.quiver(x[::5], y[::5], u[::5,::5], v[::5,::5])
    plt.colorbar()

    # Exports to a png file and shows the figure when run
    figure_file = f"res/6_fluids_{name}_psi.png"
    plt.savefig(figure_file)
    print(f"Figure saved to {figure_file}.")
    plt.show()
