# 2d_bayesian_fault_inversion

## Description
Python code for inverting geodetic data for 2D fault models. 

## Requirements
In addition to default Python libraries, this code also uses [`matplotlib`](https://matplotlib.org/), [`numpy`](https://numpy.org/), [`pandas`](https://pandas.pydata.org/), [`scipy`](https://scipy.org/) (users familiar with Python will likely already have these installed).

Several packages you may need to install are:
- [`xarray`](https://docs.xarray.dev/en/stable/): reading NETCDF data files
- [`hyp5`](https://docs.h5py.org/en/stable/): reading/writing HDF5 output files
- [`emcee`](https://emcee.readthedocs.io/en/stable/): performing Markov Chain Monte Carlo (MCMC) sampling
- [`numba`](https://numba.pydata.org/): accelerating some basic numerical calculations (i.e. fault model predictions)
- [`corner`](https://corner.readthedocs.io/en/latest/): plotting MCMC sampling results
- [`pyproj`](https://pypi.org/project/pyproj/): handling geographic coordinate systems


# References
Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. (2013). EMCEE: The MCMC hammer. Publications of the Astronomical Society of the Pacific, 125(925), 306–312. [https://doi.org/10.1086/670067](https://doi.org/10.1086/670067)

Goodman, J., & Weare, J. (2010). Ensemble samplers with affine invariance. Communications in Applied Mathematics and Computational Science, 5(1), 65–80. [https://doi.org/10.2140/camcos.2010.5.65](https://doi.org/10.2140/camcos.2010.5.65)

Vavra, E. J., Qiu, H., Chi, B., Share, P.-E., Allam, A., Morzfeld, M., et al. (2023). Active dipping interface of the Southern San Andreas fault revealed by space geodetic and seismic imaging. Journal of Geophysical Research: Solid Earth, 128, e2023JB026811. [https://doi.org/10.1029/2023JB026811](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JB026811)
