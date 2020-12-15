import matplotlib.pyplot as plt
import numpy as np

def hamiltonian( spins ) : 
  energy = 0
  # Your code to calculate the hamiltonian goes here
  avspins = sum(spins)/len(spins)
  for i in range(len(spins)) : energy = energy - 4*avspins*spins[i] 
  return energy
  
def ensemble_average( N, T ) :
  numerator, Z = 0, 0
  # Your code to calculate the partition function goes here
  spins = np.zeros(N)
  for index in range(2**N) :
      for i in range(N) :
          spins[i] = np.floor( index / 2**(N-1-i) )
          index = index - spins[i]*(2**(N-1-i))
          if spins[i]==0 : spins[i] = -1
      energy = hamiltonian(spins)
      bweight = np.exp( -energy / T )
      numerator = numerator + energy*bweight
      Z = Z + bweight
  return numerator / Z
  
energies = []
temperatures = np.linspace(0.1,3.1,15)
for temp in temperatures : energies.append( ensemble_average(8, temp) )
plt.plot( temperatures, energies, 'k-' )
plt.xlabel("temperature / au")
plt.ylabel("average energy / J")
plt.savefig("average_energy.png")
