"""
Author: Mia Clark-Webb
Date: 2025-05-19
This file is the main entry point to the fluid motion program (section 6 in
the lab sheet), which calls the relevant functions, including the Laplace
equation solver.
"""

import numpy as np
from analyse_fluids import analyse_fluids
from solve_fluids import solve_laplace


def main():
    """
    This function calls the Laplace equation solver with the relevant
    parameters specified in the lab script.
    """

    # Parallel plates:

    # Initialises 100x100 grid of zeros
    grid_size = 100
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Calls the Laplace solver with relevant parameters for parallel plates
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the parallel plates
    analyse_fluids(
        psi, "parallel_plates", "psi(x, y) for parallel plates at y = 0 and y = 1"
    )

    # Box:

    # Initialises 100x100 grids of zeros for the box obstacle
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Sets box so that the values on the outside of the middle third in each
    # direction are fixed
    box_lbound = np.floor(grid_size / 3).astype(int)
    box_ubound = np.ceil(2 * grid_size / 3).astype(int)

    for i in range(box_lbound, box_ubound + 1):
        fixed_psi[i][box_lbound] = 1
        fixed_psi[i][box_ubound] = 1
        fixed_psi[box_lbound][i] = 1
        fixed_psi[box_ubound][i] = 1

    # Calls the Laplace solver with relevant parameters for box scenario
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the box scenario
    analyse_fluids(
        psi,
        "box",
        "psi(x, y) for parallel plates at y = 0 and y = 1 with a box in the middle",
    )

    # Cylinder:

    # Initialises 100x100 grids of zeros for the cylinder obstacle
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Sets cylinder so that it has a reasonable size to see fluid flow around it
    radius = np.floor(grid_size * 4).astype(int)
    centre = np.floor(grid_size / 2).astype(int)

    for i in range(grid_size):
        for j in range(grid_size):
            if (centre - i) ** 2 + (centre - j) ** 2 <= radius ^ 2:
                fixed_psi[i][j] = 1

    # Calls the Laplace solver with relevant parameters for cylinder scenario
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the cylinder scenario
    analyse_fluids(
        psi,
        "cylinder",
        "psi(x, y) for parallel plates at y = 0 and y = 1 with a cylinder in the middle",
    )

    # Narrowed boundary (half width):

    # Initialises 100x100 grids of zeros for the reduced width of outflow
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Sets outflow parameters
    out_width = np.floor(grid_size / 2).astype(int)
    out_blockage = np.floor((grid_size - out_width) / 2).astype(int)
    out_pos = np.ceil(2 * grid_size / 3).astype(int)

    # Sets boundary conditions for the outflow
    for i in range(out_blockage):
        fixed_psi[i][out_pos] = 1
        fixed_psi[grid_size - i - 1][out_pos] = 1
        init_psi[i][out_pos] = -10
        init_psi[grid_size - i - 1][out_pos] = 10

    for i in range(out_pos, grid_size):
        fixed_psi[out_blockage][i] = 1
        fixed_psi[grid_size - out_blockage][i] = 1
        init_psi[out_blockage][i] = -10
        init_psi[grid_size - out_blockage][i] = 10

    for i in range(out_pos, grid_size):
        for j in range(out_blockage):
            fixed_psi[j][i] = 1
        for k in range((grid_size - out_blockage), grid_size):
            fixed_psi[k][i] = 1

    # Calls the Laplace solver with relevant parameters for narrowed outflow
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the narrowed outflow
    analyse_fluids(
        psi,
        "outflow_half",
        "psi(x, y) for parallel plates at y = 0 and y = 1 with the outflow narrowed to half",
    )

    # Narrowed boundary (third width):

    # Initialises 100x100 grids of zeros for the reduced width of outflow
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Sets outflow parameters
    out_width = np.floor(grid_size / 3).astype(int)
    out_blockage = np.floor((grid_size - out_width) / 2).astype(int)
    out_pos = np.ceil(2 * grid_size / 3).astype(int)

    # Sets boundary conditions for the outflow
    for i in range(out_blockage):
        fixed_psi[i][out_pos] = 1
        fixed_psi[grid_size - i - 1][out_pos] = 1
        init_psi[i][out_pos] = -10
        init_psi[grid_size - i - 1][out_pos] = 10

    for i in range(out_pos, grid_size):
        fixed_psi[out_blockage][i] = 1
        fixed_psi[grid_size - out_blockage][i] = 1
        init_psi[out_blockage][i] = -10
        init_psi[grid_size - out_blockage][i] = 10

    for i in range(out_pos, grid_size):
        for j in range(out_blockage):
            fixed_psi[j][i] = 1
        for k in range((grid_size - out_blockage), grid_size):
            fixed_psi[k][i] = 1

    # Calls the Laplace solver with relevant parameters for narrowed outflow
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the narrowed outflow
    analyse_fluids(
        psi,
        "outflow_third",
        "psi(x, y) for parallel plates at y = 0 and y = 1 with the outflow narrowed to third",
    )

    # Narrowed boundary (quarter width):

    # Initialises 100x100 grids of zeros for the reduced width of outflow
    init_psi = np.zeros((grid_size, grid_size))
    fixed_psi = np.zeros((grid_size, grid_size))

    # Sets boundary conditions for psi
    for i in range(grid_size):
        fixed_psi[0][i] = 1
        init_psi[0][i] = -10

        fixed_psi[-1][i] = 1
        init_psi[-1][i] = 10

    # Sets outflow parameters
    out_width = np.floor(grid_size / 4).astype(int)
    out_blockage = np.floor((grid_size - out_width) / 2).astype(int)
    out_pos = np.ceil(2 * grid_size / 3).astype(int)

    # Sets boundary conditions for the outflow
    for i in range(out_blockage):
        fixed_psi[i][out_pos] = 1
        fixed_psi[grid_size - i - 1][out_pos] = 1
        init_psi[i][out_pos] = -10
        init_psi[grid_size - i - 1][out_pos] = 10

    for i in range(out_pos, grid_size):
        fixed_psi[out_blockage][i] = 1
        fixed_psi[grid_size - out_blockage][i] = 1
        init_psi[out_blockage][i] = -10
        init_psi[grid_size - out_blockage][i] = 10

    for i in range(out_pos, grid_size):
        for j in range(out_blockage):
            fixed_psi[j][i] = 1
        for k in range((grid_size - out_blockage), grid_size):
            fixed_psi[k][i] = 1

    # Calls the Laplace solver with relevant parameters for narrowed outflow
    psi = solve_laplace(init_psi, fixed_psi)

    # Plots the graph for the Laplace solutions for the narrowed outflow
    analyse_fluids(
        psi,
        "outflow_quarter",
        "psi(x, y) for parallel plates at y = 0 and y = 1 with the outflow narrowed to quarter",
    )


if __name__ == "__main__":
    main()
