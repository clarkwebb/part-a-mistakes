"""
Author: Mia Clark-Webb
Date: 2025-05-19
This file is the main entry point to the Poisson equation program (section 5
in the lab sheet), which calls the relevant functions, including the Poisson
equation solver.
"""

import numpy as np
from analyse_poisson import analyse_poisson
from solve_poisson import solve_poisson


def main():
    """
    This function calls the Laplace equation solver with the relevant
    parameters specified in the lab script.
    """

    # Initialises 25x25 grid of zeros
    grid_size = 25
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[i][0] = 1
        fixed_psi[i][-1] = 1
        fixed_psi[0][i] = 1
        fixed_psi[-1][i] = 1

    # Sets line charge sources at 3 specific points
    # Sets q to be 100
    source_1 = np.zeros((grid_size, grid_size))
    source_1[12][18] = 100  # near right edge

    source_2 = np.zeros((grid_size, grid_size))
    source_2[12][12] = 100  # centre

    source_3 = np.zeros((grid_size, grid_size))
    source_3[18][18] = 100  # upper right corner

    # Calls the Poisson solver with the relevant parameters for line charges
    psi_1 = solve_poisson(init_psi, fixed_psi, source_1)
    psi_2 = solve_poisson(init_psi, fixed_psi, source_2)
    psi_3 = solve_poisson(init_psi, fixed_psi, source_3)

    # Plots the graph for the Poisson solutions for the line charges
    analyse_poisson(psi_1, "line_charge_18_12", "psi(x, y) for a line charge at (0.75, 0.5)")
    analyse_poisson(psi_2, "line_charge_12_12", "psi(x, y) for a line charge at (0.5, 0.5)")
    analyse_poisson(psi_3, "line_charge_18_18", "psi(x, y) for a line charge at (0.75, 0.75)")

    # Sets 6 sets of dipole sources
    # Sets q to be +/- 100
    source_4 = np.zeros((grid_size, grid_size))
    source_4[12][12] = -100
    source_4[12][18] = 100

    source_5 = np.zeros((grid_size, grid_size))
    source_5[12][12] = -100
    source_5[18][18] = 100

    source_6 = np.zeros((grid_size, grid_size))
    source_6[12][6] = -100
    source_6[12][18] = 100

    source_7 = np.zeros((grid_size, grid_size))
    source_7[18][6] = -100
    source_7[18][18] = 100

    source_8 = np.zeros((grid_size, grid_size))
    source_8[12][6] = -100
    source_8[18][18] = 100

    source_9 = np.zeros((grid_size, grid_size))
    source_9[6][6] = -100
    source_9[18][18] = 100

    # Calls the Poisson solver with the relevant parameters for dipoles
    psi_4 = solve_poisson(init_psi, fixed_psi, source_4)
    psi_5 = solve_poisson(init_psi, fixed_psi, source_5)
    psi_6 = solve_poisson(init_psi, fixed_psi, source_6)
    psi_7 = solve_poisson(init_psi, fixed_psi, source_7)
    psi_8 = solve_poisson(init_psi, fixed_psi, source_8)
    psi_9 = solve_poisson(init_psi, fixed_psi, source_9)

    # Plots the graphs for the Poisson solutions for the dipoles
    analyse_poisson(
        psi_4, "dipole_c_r", "psi(x, y) for a dipole from (0.5, 0.5) to (0.75, 0.5)"
    )
    analyse_poisson(
        psi_5, "dipole_c_ur", "psi(x, y) for a dipole from (0.5, 0.5) to (0.75, 0.75)"
    )
    analyse_poisson(
        psi_6, "dipole_l_r", "psi(x, y) for a dipole from (0.25, 0.5) to (0.75, 0.5)"
    )
    analyse_poisson(
        psi_7,
        "dipole_ul_ur",
        "psi(x, y) for a dipole from (0.25, 0.75) to (0.75, 0.75)",
    )
    analyse_poisson(
        psi_8,
        "dipole_l_ur",
        "psi(x, y) for a dipole from (0.25, 0.5) to (0.75, 0.75)",
    )
    analyse_poisson(
        psi_9,
        "dipole_dl_ur",
        "psi(x, y) for a dipole from (0.25, 0.25) to (0.75, 0.75)",
    )


if __name__ == "__main__":
    main()
