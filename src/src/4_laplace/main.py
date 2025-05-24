"""
Author: Mia Clark-Webb
Date: 2025-05-11
This file is the main entry point to the Laplace equation program (section 4
in the lab sheet), which calls the relevant functions, including the Laplace
equation solver.
"""

import numpy as np
from analyse_laplace import analyse_convergence, analyse_psi
from solve_laplace import solve_laplace


def main():
    """
    This function calls the Laplace equation solver with the relevant
    parameters specified in the lab script.
    """

    # Initialises 7x7 grid of zeros
    grid_size = 7
    init_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi_init
    for i in range(grid_size):
        init_psi[-1][i] = np.sin(i / 6) * np.sinh(1)  # y=1 condition
        init_psi[i][-1] = np.sin(1) * np.sinh(i / 6)  # x=1 condition

    # Calculates the final values of psi for labelled alpha values
    psi_110, hist_110 = solve_laplace(init_psi, alpha=1.10, n_iter=30)
    psi_125, hist_125 = solve_laplace(init_psi, alpha=1.25, n_iter=30)
    psi_135, hist_135 = solve_laplace(init_psi, alpha=1.35, n_iter=30)
    psi_145, hist_145 = solve_laplace(init_psi, alpha=1.45, n_iter=30)
    psi_210, hist_210 = solve_laplace(init_psi, alpha=2.10, n_iter=30)

    # Analyses convergence for each case
    analyse_convergence(hist_110, 1.10)
    analyse_convergence(hist_125, 1.25)
    analyse_convergence(hist_135, 1.35)
    analyse_convergence(hist_145, 1.45)
    analyse_convergence(hist_210, 2.10)

    # Analyses final psi values for a convergent case and a non-convergent case
    analyse_psi(psi_135, 1.35)
    analyse_psi(psi_210, 2.1)

    # Prints output string for alpha = 1.10
    output_string = (
        "Final values of psi for alpha = 1.10 (x increasing "
        + "left to right, y increasing bottom to top):\n\n"
    )
    for j in range(grid_size - 1, -1, -1):
        for i in range(0, grid_size):
            output_string += str(psi_110[j][i]) + ", "
        output_string += "\n\n"

    print(output_string)

    # Prints output string for alpha = 1.25
    output_string = (
        "Final values of psi for alpha = 1.25 (x increasing "
        + "left to right, y increasing bottom to top):\n\n"
    )
    for j in range(grid_size - 1, -1, -1):
        for i in range(0, grid_size):
            output_string += str(psi_125[j][i]) + ", "
        output_string += "\n\n"

    print(output_string)

    # Prints output string for alpha = 1.35
    output_string = (
        "Final values of psi for alpha = 1.35 (x increasing "
        + "left to right, y increasing bottom to top):\n\n"
    )
    for j in range(grid_size - 1, -1, -1):
        for i in range(0, grid_size):
            output_string += str(psi_135[j][i]) + ", "
        output_string += "\n\n"

    print(output_string)

    # Prints output string for alpha = 1.45
    output_string = (
        "Final values of psi for alpha = 1.45 (x increasing "
        + "left to right, y increasing bottom to top):\n\n"
    )
    for j in range(grid_size - 1, -1, -1):
        for i in range(0, grid_size):
            output_string += str(psi_145[j][i]) + ", "
        output_string += "\n\n"

    print(output_string)

    # Prints output string for alpha = 2.10
    output_string = (
        "Final values of psi for alpha = 2.10 (x increasing "
        + "left to right, y increasing bottom to top):\n\n"
    )
    for j in range(grid_size - 1, -1, -1):
        for i in range(0, grid_size):
            output_string += str(psi_210[j][i]) + ", "
        output_string += "\n\n"

    print(output_string)


if __name__ == "__main__":
    main()
