"""
Author: Mia Clark-Webb
Date: 2025-05-19
This module plots the results of the Poisson solver
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Makes matplotlib work on Wayland, which is necessary for my personal system
matplotlib.use("TkAgg")


def analyse_poisson(psi_values, name, title):
    """
    This function analyses psi by plotting it on a colour-coded matplotlib
    contour graph.

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
    x = np.asarray([i/(n_psi-1) for i in range(n_psi)])
    y = np.asarray([i/(n_psi-1) for i in range(n_psi)])

    # Plots the graph
    plt.contourf(x, y, psi_values)
    plt.colorbar()

    # Exports to a png file and shows the figure when run
    figure_file = f"res/5_poisson_{name}_psi.png"
    plt.savefig(figure_file)
    print(f"Figure saved to {figure_file}.")
    plt.show()
