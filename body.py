import numpy as np 

class Body:
    def __init__(self, name, mass, position, velocity, color='white'):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.zeros(2)
        self.color = color
        self.trajectory = [self.position.copy()] # For path tracing

    def update_trajectory(self):
        self.trajectory.append(self.position.copy())