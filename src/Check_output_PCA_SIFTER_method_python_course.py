# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:58:33 2025

@author: jalin005
"""
#%% IMPORT PACKAGES
import h5py
import matplotlib.pyplot as plt
from pathlib import Path

#%% IMPORT PCA FILE
# Path to the file
file_path_PCA_output = Path.cwd() / "results" /"pca_sahara_b_0326.hdf5"
assert file_path_PCA_output.is_file()


#%% INSPECT THE PCA FILE
# Open the file in read mode
with h5py.File(file_path_PCA_output, 'r') as f:
    # Check the contents of the file
    print("File Keys:", list(f.keys()))  # This will show you the top-level groups and datasets in the file

    # Access a specific dataset, in this case 'EOF'
    EOF_data = f['EOF'][:] # EOF is the same as PCA, so it will contain the generated principal components
    print("EOF data shape:", EOF_data.shape)
    
    # Save the EOF_score as a variable
    EOF_score = f['EOF_score'][:]
    print("EOF_score data shape:", EOF_score.shape)
    
    wavelength = f['wavelength'][:]
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