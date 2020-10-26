import pypsdier
from matplotlib import pyplot as plt
import numpy as np

SIM = pypsdier.SimulationInterface()
SIM.load("pycon.rde")

#from IPython import embed; embed()

# Get the data
t = SIM.outputs["pde"]["t"]
C = SIM.outputs["pde"]["C"]
C_bulk = C[0][0][:,-1]
Nc = len(C)
Nr = C[0][0].shape[1]
R = []
R_Nc = [0.7, 0.85, 1.0]
for R_nc in R_Nc:
    R.append(np.linspace(0,R_nc, Nr))

# Other option
for i, t_i in enumerate(t):
    print("Step:", i)
    # Repack the info    
    C_plot = []
    # Plots
    fig = plt.figure(figsize=(12, 8))
    left_axes_list = []
    for nc in range(Nc):
        if nc==0:
           axes = fig.add_subplot(Nc,2,2*nc+1)
        else:
           axes = fig.add_subplot(Nc,2,2*nc+1, sharey=left_axes_list[0])
        left_axes_list.append(axes)
    right_axes = fig.add_subplot(1,2,2)
    # left plots
    for nc in range(Nc):
        C_plot = C[nc][0][i,:]
        caxes = left_axes_list[nc] 
        caxes.plot(R[nc], C_plot, 'b-o', ms=2)
        caxes.set_xlim([-0.1, 1.1])
        caxes.set_ylim([-0.1, 1.5])
        caxes.plot(R[nc][-1], C_plot[-1], 'ro')
        caxes.set_xticks([0, R_Nc[nc]])
        caxes.set_xticklabels(["0", "$R_{}$".format(nc+1)])
        caxes.set_ylabel("Concentración dentro de la partícula [mM]")
    caxes.set_xlabel("Radio [m]")
    # right plot
    right_axes.plot(t[:(i+1)], C_bulk[:(i+1)], "r")
    right_axes.plot(t[i], C_bulk[i], "ro")
    right_axes.set_xlim(-10, max(t)+10)
    right_axes.set_ylim(-0.1, max(C_bulk)+.2)
    right_axes.set_xlabel("Tiempo [seg]")
    right_axes.set_ylabel("Concentración en fase líquida [mM]")
    # Some legends and texts
    fig.suptitle('Concentracion at t={} segundos'.format(int(t_i)))
    # Save fig
    plt.savefig(f"images/plot_{i:03}")
    plt.close()