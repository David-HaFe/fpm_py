# this file should be used to save any type of file,
# and the global naming convention can be edited here

from pathlib import Path

from config import (
    no_particles_x,
    no_particles_y,
    kernel_scaling,
    steps_per_sec,
)


# file prefix -> defined by example you are running
# file suffix -> depends on what you want to save
# file type   -> write out file type ending
# example name = get_file_name("heat_equation", "heat_map", "mp4")
def get_file_name(file_prefix, file_suffix, file_type):
    kernel_support = str(kernel_scaling).replace(".", "_")
    step_size = str(float(1 / steps_per_sec)).replace(".", "_")
    directory_name = f"{file_prefix}/{file_suffix}s"
    name = f"{directory_name}/{file_suffix}_{no_particles_x}x{no_particles_y}_r{kernel_support}_dt{step_size}.{file_type}"
    Path(name).parent.mkdir(parents=True, exist_ok=True)
    return name
