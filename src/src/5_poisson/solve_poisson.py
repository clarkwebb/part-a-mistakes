"""
Author: Mia Clark-Webb
Date: 2025-05-19
This file contains the function to solve Poisson's equation
"""

import matplotlib
import numpy as np

# Makes matplotlib work on Wayland, which is necessary for my personal system
matplotlib.use("TkAgg")


def solve_poisson(init_psi, fixed_psi, source):
    """
    This function solves Poisson's equation using the over-relaxation method

    Inputs:
    * init_psi: 2D matrix containing the initial psi, including boundaries
    * fixed_psi: 2D matrix representing all values of psi that will stay
        constant throughout the iterations (1 if they stay constant and 0
        otherwise)
    * source: the inhomogeneity in Poisson's equation
        (the "f" in del^2 psi = f)

    Outputs:
    * psi: 2D matrix of the value of psi after the solution

    Constraints:
    * alpha and the number of iterations must be determined by the function
    * init_psi, fixed_psi, and source are assumed to have the same size and
        the function does not need to check this
    """

    # Copies the initial psi to a new list, psi
    psi = np.copy(init_psi)
    psi_size = len(psi)

    # Finds the optimum alpha value and uses this as the relaxation parameter
    alpha = 2 / (1 + np.sin(np.pi / (psi_size - 1)))

    # Initialises residuals grid
    res = np.zeros((psi_size, psi_size))

    # Sets the convergence condition—if the residual for all i, j are less
    # than this value, convergence will be deemed to have been reached
    convergence_condition = 1e-12

    # Sets up iteration
    for _ in range(100):

        # Assumes convergence has been reached; will be changed to not be so
        # if convergence hasn't been reached
        convergence_reached = True

        # Iterates backwards (from 5 to 1) through i and j values
        for j in range(psi_size):
            for i in range(psi_size):

                # Finds new value of the residual at position (i, j) in the
                # grid iff that specific psi_i,j is not fixed
                if not fixed_psi[i][j]:
                    res[i][j] = (
                        psi[i][j + 1]
                        + psi[i][j - 1]
                        + psi[i + 1][j]
                        + psi[i - 1][j]
                        - 4 * psi[i][j]
                        - source[i][j] / ((psi_size - 1) ** 2)
                    )

                # Sets the convergence variable to be False if it has not yet
                # converged
                if np.abs(res[i][j]) > convergence_condition:
                    convergence_reached = False

                # Finds new value of psi at position (i, j) in the grid
                psi[i][j] += (alpha * res[i][j]) / 4

        # Exits the loop as psi has converged
        if convergence_reached:
            break

    return psi
