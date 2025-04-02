# check output PCA analysis SIFTER

The goal of this repository is to analyze the Principal Component's (PC's) from the PC Analysis (PCA) results from the first step of the SIFTER algorithm, where PC's are generated to simulate transmittance over the Sahara, for the TROPOMI satellite.

The script reads PCA results from an HDF5 file, extracts the principal components (EOFs), and plots them against wavelength. You can visualize different PCA modes using the plot_pca() function.

## Usage
Ensure you have installed the required dependencies (h5py, matplotlib, pathlib).
Run the script to inspect the PCA file structure and generate plots.
Modify the plot_pca() function call to view specific PCA modes.

## Project Structure

The project structure distinguishes three kinds of folders:
- read-only (RO): not edited by either code or researcher
- human-writeable (HW): edited by the researcher only.
- project-generated (PG): folders generated when running the code; these folders can be deleted or emptied and will be completely reconstituted as the project is run.

```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── data               <- All project data, ignored by git
├── docs               <- Documentation notebook for users (HW)
│   ├── manuscript     <- Manuscript source, e.g., LaTeX, Markdown, etc. (HW)
│   └── reports        <- Other project reports and notebooks (e.g. Jupyter, .Rmd) (HW)
├── results            <- results from previously run scripts
│   ├── figures        <- Figures for the manuscript or reports (PG)
│   └── output         <- Other output for the manuscript or reports (PG)
└── src                <- Source code for this project (HW)

```

## Add a citation file
Create a citation file for your repository using [cffinit](https://citation-file-format.github.io/cff-initializer-javascript/#/)

## License

This project is licensed under the terms of the [MIT License](/LICENSE).
