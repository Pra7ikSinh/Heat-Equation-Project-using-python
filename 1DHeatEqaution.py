import numpy as np
import matplotlib.pyplot as plt

thermal_diffusivity = 110 
rod_length = 50          
simulation_time = 4      
num_points = 20          

point_spacing = rod_length / (num_points - 1)
time_step = 0.5 * point_spacing**2 / thermal_diffusivity
num_time_steps = int(simulation_time / time_step) + 1 

temperature_profile = np.zeros(num_points) + 20

temperature_profile[0] = 100
temperature_profile[-1] = 100

fig, axis = plt.subplots()
heat_map = axis.pcolormesh([temperature_profile], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(heat_map, ax=axis)
axis.set_ylim([-2, 3])

current_time = 0

while current_time < simulation_time:
    
    temp_previous = temperature_profile.copy()

    for i in range(1, num_points - 1):
        temperature_profile[i] = (
            time_step * thermal_diffusivity * (temp_previous[i - 1] - 2 * temp_previous[i] + temp_previous[i + 1]) / point_spacing ** 2
            + temp_previous[i]
        )

    current_time += time_step

    print("t: {:.3f} [s], Average temperature: {:.2f} °C".format(current_time, np.average(temperature_profile)))

    heat_map.set_array([temperature_profile])
    axis.set_title(f"Temperature distribution at t: {current_time:.3f} [s]")
    plt.pause(0.01)

plt.show()
