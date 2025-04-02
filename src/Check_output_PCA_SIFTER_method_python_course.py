# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:58:33 2025

@author: jalin005

In this script, you can explore the PCA's that were generated for transmittence
in the Principal Component Analysis part of the SIFTER algoritm.

"""
#%% IMPORT PACKAGES
import h5py
import matplotlib.pyplot as plt
from pathlib import Path

#%% IMPORT PCA FILE
file_path_PCA_output = Path.cwd() / "results" /"pca_sahara_b_0326.hdf5"
assert file_path_PCA_output.is_file()


#%% INSPECT THE PCA FILE
# Open the file in read mode
with h5py.File(file_path_PCA_output, 'r') as PCA_output:
    # Check the contents of the file
    print("File Keys:", list(PCA_output.keys()))  

    # Access a specific dataset, in this case 'EOF'
    EOF_data = PCA_output['EOF'][:] # EOF is the same as PCA, so it will contain the generated principal components
    print("EOF data shape:", EOF_data.shape)
    
    EOF_score = PCA_output['EOF_score'][:]
    print("EOF_score data shape:", EOF_score.shape)
    
    wavelength = PCA_output['wavelength'][:]
    print("wavelength shape:", wavelength.shape)
    
#%% PLOT THE FIRST TWO PCA'S

# Plot the first PCA
plt.plot(wavelength, EOF_data[0], label="PCA 1", color='b')
plt.xlabel("Wavelength (nm)")
plt.ylabel("PCA Amplitude")
plt.legend()
plt.show() # Show the plot

# Plot the second PCA 
plt.plot(wavelength, EOF_data[1], label="PCA 2", color='r')
plt.xlabel("Wavelength (nm)")
plt.ylabel("PCA Amplitude")
plt.legend()
plt.show() # Show the plot


#%% FUNCTION TO PLOT PCA'S

"""

"""
def plot_pca(wavelength, EOF_data, pca_index):
    """
    This function can be used to plot the PCA's against wavelength.
    
    Parameters:
    wavelength:Array of wavelength values.
    EOF_data: Array containing 10 generated PCA's.
    pca_index (int): Index of the PCA to plot (starting from 0).
    """
    plt.plot(wavelength, EOF_data[pca_index], label=f"PCA {pca_index + 1}")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("PCA Amplitude")
    plt.legend()
    plt.show()

# Example usage
plot_pca(wavelength, EOF_data, 0)  
plot_pca(wavelength, EOF_data, 3)  

