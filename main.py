from body import Body
from engine import update_bodies
from visualize import init_plot, plot_bodies
import time

# Function to create bodies dynamically
def create_bodies(num_bodies):
    bodies = []
    
    # Create the Sun (always in the center)
    sun = Body(
        name="Sun", 
        mass=1.9885e30,  # kg
        position=[0, 0],  # m
        velocity=[0, 0],  # m/s
        color='yellow'
    )
    bodies.append(sun)

    # Create other bodies (planets or random bodies)
    for i in range(1, num_bodies):
        body = Body(
            name=f"Body_{i}", 
            mass=5.972e24 * (i+1),  # increasing mass for variety
            position=[(i+1) * 1.496e11, 0],  # place them at increasing distances
            velocity=[0, 29.78e3 * (i+1)],  # arbitrary speed
            color='blue'
        )
        bodies.append(body)
    
    return bodies

# Create bodies (customize the number here)
num_bodies = 5  # Change this number to simulate more bodies
bodies = create_bodies(num_bodies)

# Set time step (in seconds)
dt = 60 * 60  # 1 hour per step

# Set up plot
fig, ax = init_plot()

# Run Simulation
for step in range(1000):  # simulate 1000 steps
    update_bodies(bodies, dt)
    plot_bodies(ax, bodies)
    time.sleep(0.01)  # slow down to visualize
