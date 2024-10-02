import numpy as np
import matplotlib.pyplot as plt

thermal_diffusivity = 110  
plate_length = 50         
simulation_time = 4       
num_points = 40           

point_spacing_x = plate_length / (num_points - 1)
point_spacing_y = plate_length / (num_points - 1)

time_step = min(point_spacing_x**2 / (4 * thermal_diffusivity), 
                point_spacing_y**2 / (4 * thermal_diffusivity))

num_time_steps = int(simulation_time / time_step) + 1 
temperature_grid = np.zeros((num_points, num_points)) + 20

temperature_grid[0, :] = np.linspace(0, 100, num_points)
temperature_grid[-1, :] = np.linspace(0, 100, num_points)
temperature_grid[:, 0] = np.linspace(0, 100, num_points)
temperature_grid[:, -1] = np.linspace(0, 100, num_points)

fig, axis = plt.subplots()
heat_map = axis.pcolormesh(temperature_grid, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(heat_map, ax=axis)

current_time = 0

while current_time < simulation_time:
    
    temp_previous = temperature_grid.copy() 

    for i in range(1, num_points - 1):
        for j in range(1, num_points - 1):

            d2T_dx2 = (temp_previous[i-1, j] - 2*temp_previous[i, j] + temp_previous[i+1, j]) / point_spacing_x**2
            d2T_dy2 = (temp_previous[i, j-1] - 2*temp_previous[i, j] + temp_previous[i, j+1]) / point_spacing_y**2

            temperature_grid[i, j] = time_step * thermal_diffusivity * (d2T_dx2 + d2T_dy2) + temp_previous[i, j]

    current_time += time_step

    print(f"t: {current_time:.3f} [s], Average temperature: {np.average(temperature_grid):.2f} °C")

    heat_map.set_array(temperature_grid.ravel())
    axis.set_title(f"Temperature distribution at t: {current_time:.3f} [s]")
    plt.pause(0.01)

plt.show()
