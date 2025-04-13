import numpy as np
from constants import G

def compute_gravitational_force(body1, body2):
    '''
    Compute the gravitational force exerted on body 1 by body 2.
    '''
    delta = body2.position - body1.position  # vector from body1 to body2
    distance = np.linalg.norm(delta)

    if distance == 0:
        return np.zeros(2)  # avoid division by zero

    force_magnitude = G * body1.mass * body2.mass / distance ** 2
    force_direction = delta / distance  # unit vector

    return force_magnitude * force_direction

def update_bodies(bodies, dt):
    """
    Update positions, velocities, and calculate forces for all bodies.
    """
    # Reset forces
    for body in bodies:
        body.force = np.zeros(2)

    # Calculate net forces on each body
    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if i != j:
                body1.force += compute_gravitational_force(body1, body2)

    # Update velocities and positions using Euler integration
    for body in bodies:
        acceleration = body.force / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt
        body.update_trajectory()  # Track the body’s trajectory