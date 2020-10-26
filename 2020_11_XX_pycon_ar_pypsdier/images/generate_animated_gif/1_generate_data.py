def MichaelisMenten(S, E0, k, K):
  """Definition for Michaelis Menten reaction with inputs E0 [mM], k [1/s] and K [mM]"""
  return (-k*E0*S[0]/(K+S[0]), )

inputs = {}
inputs["SimulationTime"] = 120. # [s]
inputs["SavingTimeStep"] = 1. # [s]
inputs["CatalystVolume"] = 0.5 # [mL]
inputs["BulkVolume"]  = 100.0  # [mL]
inputs["Names"] = ('Substrat',)  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (1.3,)   # [mM]
inputs["EffectiveDiffusionCoefficients"] = (5.3E-9,)  # [m2/s]
inputs["CatalystParticleRadius"] = [70.0E-6, 85.0E-6, 100.0E-6] # [m]
inputs["CatalystParticleRadiusFrequency"] = [0.3, 0.5, 0.2] # []
inputs["ReactionFunction"] = MichaelisMenten # function 
inputs["ReactionParameters"] = (41 , 0.13)   # [1/s], [mM/s], parameters
inputs["CatalystEnzymeConcentration"] = 0.10 # [mM]

plot_options = {}
plot_options["label_x"] = "Tiempo de reacción [s]"
plot_options["label_y"] = "Concentración [mM]"
plot_options["title"] = "Simulación de Michaelis Menten para la PyconAr"
plot_options["data_x"] = [0.0, 30, 60, 90, 120]
plot_options["data_y"] = [1.3, 0.65, 0.25, 0.10, 0.0]
plot_options["data_kwargs"] = {'label':'exp', 'color':'red', 
                         'marker':'s', 'markersize':6, 
                         'linestyle':'none','linewidth':2}
plot_options["sim_kwargs"] = {'label':'sim', 'color':'black', 
                         'marker':'o', 'markersize':6, 
                         'linestyle':'dashed','linewidth':2}

# import pypsdier
import pypsdier
SIM1 = pypsdier.SimulationInterface()
SIM1.new(inputs, plot_options)

SIM1.simulate("ode")

SIM1.simulate("pde")

SIM1.save("pycon.rde")