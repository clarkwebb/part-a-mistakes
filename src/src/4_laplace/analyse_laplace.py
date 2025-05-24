"""
Author: Mia Clark-Webb
Date: 2025-05-13
This module plots the results for both the overall solution for each alpha
case, as well as the history of a specific psi_i,j in the upper, middle, and
lower regions for each alpha value.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Makes matplotlib work on Wayland, which is necessary for my personal system
matplotlib.use("TkAgg")


def analyse_convergence(hist_values, alpha):
    """
    This function analyses the historical values of psi values for each alpha
    value, by plotting them on appropriate matplotlib graphs.

    Inputs:
    * hist_values: a 2D numpy array containing historical values of three
        values of psi, corresponding to one value of alpha
    * alpha: contains the value of alpha for the plot so that it can be put in
        the title of the graph

    Outputs:
    * (no returned values - this function just executes the process of
        exporting the graph to a png file)

    Constraints:
    * The array length of each value of psi may not be 30 if convergence was
        reached early
    """

    # This obtains the amount of iterations before convergence
    iters = np.shape(hist_values)[1]

    # x-axis values
    it = np.arange(1, iters + 1)

    # y-axis values
    psi_down = hist_values[0]
    psi_mid = hist_values[1]
    psi_up = hist_values[2]

    # Sets up figure with title and axis labels
    plt.figure(figsize=(10, 6))
    plt.title(f"psi_i,j against number of iterations for alpha = {alpha}")
    plt.xlabel("Number of iterations")
    plt.ylabel("psi_i,j")
    plt.xlim(0, 30)

    # Plots the three values of psi_i,j against the number of iterations
    plt.plot(it, psi_down, label="Value of psi in lower half")
    plt.plot(it, psi_mid, label="Value of psi in middle")
    plt.plot(it, psi_up, label="Value of psi in upper half")

    # Adds a legend
    plt.legend()

    # Exports to a png file and shows the figure when run
    figure_file = f"res/4_laplace_{alpha}_hist.png"
    plt.savefig(figure_file)
    print(f"Figure saved to {figure_file}.")
    plt.show()


def analyse_psi(psi_values, alpha):
    """
    This function analyses psi by plotting it on a colour-coded matplotlib
    contour graph.

    Inputs:
    * psi_values: a 2D numpy array containing the approximated values of psi
        at each grid position

    Outputs:
    * (no returned values - this function just executes the process of
        exporting the graph to a png file)

    Constraints:
    * This should be different for the psi_i,j corresponding to different
        values of alpha, as some may not have converged
    """

    # Sets up figure with title and axis labels
    plt.figure(figsize=(10, 6))
    plt.title(f"psi(x, y) for alpha = {alpha}")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    n_psi = len(psi_values)

    # This creates 1D numpy arrays for x and y corresponding to each psi value
    # in the psi list compacted to 1D
    x = np.asarray([(i % n_psi) / (n_psi - 1) for i in range(0, n_psi**2)])
    y = np.asarray([(i // n_psi) / (n_psi - 1) for i in range(0, n_psi**2)])
    psi_1d = np.ravel(psi_values)  # Compacts the psi list to 1D

    # Creates interpolated arrays for x, y, and psi, using a cubic
    # interpolation algorithm
    x_interp = np.linspace(0, 1, 100)
    y_interp = np.linspace(0, 1, 100)
    psi_interp = griddata(
        (x, y), psi_1d, (x_interp[None, :], y_interp[:, None]), method="cubic"
    )

    # Plots the contour diagram and the colour bar key
    plt.contour(x_interp, y_interp, psi_interp)
    plt.contourf(x_interp, y_interp, psi_interp)

    plt.colorbar()

    # Exports to a png file and shows the figure when run
    figure_file = f"res/4_laplace_{alpha}_psi.png"
    plt.savefig(figure_file)
    print(f"Figure saved to {figure_file}.")
    plt.show()
