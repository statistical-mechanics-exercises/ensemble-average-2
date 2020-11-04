import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  
  return energy
  
def ensemble_average( N, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  
  return numerator / Z
  
energies = []
temperatures = np.linspace(0.1,3.1,15)
for temp in temperatures : energies.append( ensemble_average(8, temp) )
plt.plot( temperatures, energies, 'k-' )
plt.xlabel("temperature / au")
plt.ylabel("average energy / J")
plt.savefig("average_energy.png")
