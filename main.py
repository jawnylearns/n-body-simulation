import numpy as np
import matplotlib.pyplot as plt
from engine import getEnergy, getAcc

# Define Constants and Helper Functions as before...

def main():
    """ N-body simulation """
    
    # Simulation parameters
    N         = 10      # Number of particles
    t         = 0      # current time of the simulation
    tEnd      = 10.0   # time at which simulation ends
    dt        = 0.01   # timestep
    softening = 0.1    # softening length
    G         = 1.0    # Newton's Gravitational Constant
    plotRealTime = True # switch on for plotting as the simulation goes along
    
    # Generate Initial Conditions
    np.random.seed(17)            # set the random number generator seed
    
    mass = 20.0*np.ones((N,1))/N  # total mass of particles is 20

    # Generate equidistant positions in a circle around the center (0,0)
    radius = 1.5  # distance of bodies from the center
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    pos = np.column_stack((radius * np.cos(angles), radius * np.sin(angles), np.zeros(N)))
    
    # Initial velocities pointing towards the center of the chart
    vel = -np.column_stack((np.sin(angles), -np.cos(angles), np.zeros(N)))
    
    # Random colors for each body
    colors = np.random.rand(N, 3)
    
    # Convert to Center-of-Mass frame
    vel -= np.mean(mass * vel,0) / np.mean(mass)
    
    # calculate initial gravitational accelerations
    acc = getAcc( pos, mass, G, softening )
    
    # calculate initial energy of system
    KE, PE  = getEnergy( pos, vel, mass, G )
    
    # number of timesteps
    Nt = int(np.ceil(tEnd/dt))
    
    # save energies, particle orbits for plotting trails
    pos_save = np.zeros((N,3,Nt+1))
    pos_save[:,:,0] = pos
    KE_save = np.zeros(Nt+1)
    KE_save[0] = KE
    PE_save = np.zeros(Nt+1)
    PE_save[0] = PE
    t_all = np.arange(Nt+1)*dt
    
    # prep figure
    fig = plt.figure(figsize=(4,5), dpi=80)
    ax1 = fig.add_subplot(111)
    
    # Simulation Main Loop
    for i in range(Nt):
        # (1/2) kick
        vel += acc * dt/2.0
        
        # drift
        pos += vel * dt
        
        # update accelerations
        acc = getAcc( pos, mass, G, softening )
        
        # (1/2) kick
        vel += acc * dt/2.0
        
        # update time
        t += dt
        
        # get energy of system
        KE, PE  = getEnergy( pos, vel, mass, G )
        
        # save positions for plotting trail
        pos_save[:,:,i+1] = pos
        KE_save[i+1] = KE
        PE_save[i+1] = PE
        
        # plot in real time
        if plotRealTime or (i == Nt-1):
            plt.sca(ax1)
            plt.cla()
        
            # Plot the solid tracer lines (using lines instead of scatter points)
            for j in range(N):
                # Use ax.plot for each body to create solid tracers
                ax1.plot(pos_save[j, 0, :i+1], pos_save[j, 1, :i+1], color=colors[j], lw=2)
            
            # Plot the bodies with their assigned random color
            for j in range(N):
                plt.scatter(pos[j,0], pos[j,1], s=50, color=colors[j])  # Increase size of bodies
            
            ax1.set(xlim=(-2, 2), ylim=(-2, 2))
            ax1.set_aspect('equal', 'box')
            ax1.set_xticks([-2,-1,0,1,2])
            ax1.set_yticks([-2,-1,0,1,2])
            
            plt.pause(0.001)
    
    # Save figure
    plt.show()

    return 0

if __name__== "__main__":
    main()

