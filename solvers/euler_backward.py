import numpy as np
from types import SimpleNamespace


def euler_backward(
    function,
    initial_condition,
    t_start=0,
    t_end=1,
    dt=0.01,
):
    # calculate stuffs
    no_iterations = int((t_end - t_start) / dt)
    times = np.linspace(t_start, t_end, no_iterations)
    solution = np.empty((np.size(initial_condition), no_iterations + 1))

    y = initial_condition

    solution[:, 0] = initial_condition
    y_plus = np.zeros(np.size(initial_condition))

    def residual(y_next, y_now):
        return y_next - y_now - function(y_next)*dt

    # iterate up to the last entry of times, not including it, and also start
    # walking index at 1
    # should technically evaulate at t_k+1, but doesn't matter here
    tol = 1e-4
    for index, time in enumerate(times[: -1], start=1):

        error = 2*tol
        y_plus = y
        while error > tol:
            y_plus = y + dt * function(time, y_plus)
            error = np.linalg.norm(y_plus - y - dt*function(time, y_plus))

        y = y_plus
        solution[:, index] = y

    print("")
    print("iterations: " + str(no_iterations))

    return SimpleNamespace(t=times, y=solution)
