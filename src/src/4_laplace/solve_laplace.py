"""
Author: Mia Clark-Webb
Date: 2025-05-12
This file contains the module to solve Laplace's equation
"""

import numpy as np


def solve_laplace(init_psi, alpha, n_iter):
    """
    This function solves Laplace's equation using the over-relaxation method

    Inputs:
    * init_psi: 2D matrix containing the initial psi, including boundaries
    * alpha: the coefficient of over-relaxation
    * n_iter: maximum number of iterations performed

    Outputs:
    * psi: 2D matrix of the value of psi after (up to) n_iter iterations
    * hist_values: (N-iter x 3) matrix that contains historical values of 3
        points during the iteration (1 in the upper half, 1 in the middle, and
        1 in the lower half)

    Constraints:
    * The boundaries of psi are kept constant during the iterations
    """

    # Copies the initial psi to a new list, psi
    psi = np.copy(init_psi)

    # Initialises hist_values, the list that contains historical values for
    # three values of psi_i_j
    hist_values = [[], [], []]
    j_up = len(psi) - 2
    j_mid = len(psi) // 2
    j_down = 1

    # Initialises residuals grid—we can make it smaller by not considering the
    # boundaries' residuals as they are always zero by definition
    res = np.zeros((len(psi) - 2, len(psi) - 2))

    # Sets the convergence condition—if the residual for all i, j are less
    # than this value, convergence will be deemed to have been reached
    convergence_condition = 1e-6

    # Sets up iteration
    for _ in range(n_iter):

        # Assumes convergence has been reached; will be changed to not be so
        # if convergence hasn't been reached
        convergence_reached = True

        # Iterates backwards (from 5 to 1) through i and j values
        for j in range(5, 0, -1):
            for i in range(5, 0, -1):
                # Finds new value of the residual at position (i, j) in the
                # grid
                res[i - 1][j - 1] = (
                    psi[i][j + 1]
                    + psi[i][j - 1]
                    + psi[i + 1][j]
                    + psi[i - 1][j]
                    - 4 * psi[i][j]
                )

                # Sets the convergence variable to be False if it has not yet
                # converged
                if np.abs(res[i - 1][j - 1]) > convergence_condition:
                    convergence_reached = False

                # Finds new value of psi at positiion (i, j) in the grid
                psi[i][j] += (alpha * res[i - 1][j - 1]) / 4

        # Sets new values in hist_values
        hist_values[0].append(psi[j_mid][j_down])
        hist_values[1].append(psi[j_mid][j_mid])
        hist_values[2].append(psi[j_mid][j_up])

        # Exits the loop as psi has converged
        if convergence_reached:
            break

    # Converts hist_values to a numpy array
    hist_values = np.asarray(hist_values)

    return psi, hist_values
