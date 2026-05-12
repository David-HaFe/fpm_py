# code for the solution function
#                       -y²           -x²
# T(t, x, y) = cos(at) e   + sin(bt) e

import numpy as np
from itertools import product

from config import heat_alpha
from config import (
    sim_result,
    t0,
    t1,
    no_steps,
    no_particles,
    x_positions,
    y_positions,
    heat_alpha,
)

a = 1
b = 2


def main():
    times = np.linspace(t0, t1, no_steps)

    x_sol = np.zeros((no_steps, no_particles))
    y_sol = np.zeros((no_steps, no_particles))
    T_sol = np.zeros((no_steps, no_particles))

    for t_index, t in enumerate(times):
        for particle_index, (x, y) in enumerate(product(x_positions, y_positions)):
            x_sol[t_index][particle_index] = float(x)
            y_sol[t_index][particle_index] = float(y)
            T_sol[t_index][particle_index] = float(solution(x, y, t))

    data_2_dummy = np.zeros((no_steps, no_particles))
    is_border_particle = np.full(no_particles, False)

    result = sim_result(
        t=times,
        x=x_sol,
        y=y_sol,
        data_1=T_sol,
        data_2=data_2_dummy,
        is_border_particle=is_border_particle,
    )
    return result


def solution(x: float, y: float, t: float = 0):
    return np.cos(a * t) * np.exp(-(y**2)) + np.sin(b * t) * np.exp(-(x**2))


def source_term_heat_equation(t: float, x: float, y: float):
    term_1 = -a * np.sin(a * t) * np.exp(-(y**2))
    term_2 = b * np.cos(b * t) * np.exp(-(x**2))
    term_3 = (4 * y**2 - 2) * np.exp(-(y**2)) * np.cos(a * t)
    term_4 = (4 * x**2 - 2) * np.exp(-(x**2)) * np.sin(b * t)

    return term_1 + term_2 - heat_alpha * (term_3 + term_4)
