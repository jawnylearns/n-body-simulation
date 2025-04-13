import numpy as np
import matplotlib.pyplot as plt

def init_plot():
    """
    Initialize the plot with labels and limits.
    """
    fig, ax = plt.subplots()
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_aspect('equal')
    ax.set_xlim(-2e11, 2e11)  # Adjust depending on your system's scale
    ax.set_ylim(-2e11, 2e11)
    return fig, ax

def plot_bodies(ax, bodies):
    """
    Plot all bodies and their trajectories.
    """
    ax.clear()  # Clear the previous frame
    for body in bodies:
        # Plot the current position
        ax.plot(body.position[0], body.position[1], 'o', color=body.color)

        # Plot the trajectory (previous positions)
        trajectory = np.array(body.trajectory)
        ax.plot(trajectory[:, 0], trajectory[:, 1], color=body.color, alpha=0.5)
    
    # Redraw the plot
    plt.draw()
    plt.pause(0.01)  # Pause to allow the plot to update
