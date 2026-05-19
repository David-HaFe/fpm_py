import numpy as np
from types import SimpleNamespace
from utils.diagnostics import diagnostics


def chorin(
    forward_equation,
    projection_equation,
    border_update,
    initial_condition,
    t_start,
    t_end,
    dt=0.01,
):
    # set up solution array
    no_iterations = int((t_end - t_start) / dt)
    times = np.linspace(t_start, t_end, no_iterations)
    solution = np.zeros((np.size(initial_condition), np.size(times)))

    # write initial condition to state
    y = initial_condition
    solution[:, 0] = initial_condition

    try:
        for index, time in enumerate(times[:-1], start=1):
            # intermediate step
            y = y + dt * forward_equation(time, y)

            # apply this until the rate of change is sufficiently small
            # initialize error to something meaningless since python doesn't have a
            # do while loop apparently
            # poisson pressure equation
            y = y + dt * projection_equation(time, y)

            solution[:, index] = y
    except np.linalg.LinAlgError:
        print("\nLINALG ERROR - exiting now")
        pass

    return SimpleNamespace(t=times, y=solution)
