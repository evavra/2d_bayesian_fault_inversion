# 2d_bayesian_fault_inversion

## Description
Hello! This code is for inverting geodetic data for simple 2D fault models based on elastic dislocations (Segall, 2010). It was originally used to investigate the shallow geometry of the southern San Andreas fault using InSAR measurements of fault creep and slow-slip (Vavra et al., 2023).

### Fault model
The "de-fault" model consists of $L$ finite screw dislocations to approximate an elliptical slip distribution, which is consistent with a constant stress drop (Fialko, 2007). The model parameters are the the slip rate $s_0$ (or displacement) at the surface, maximum depth of slip $d_L$ (i.e. "locking depth"), fault dip angle $\theta$, and a uniform velocity (or displacment) shift $v_c$ which is added to the model prediction to account for long-wavelength errors.

![alt text](https://github.com/evavra/2d_bayesian_fault_inversion/blob/main/fault_diagram.png "Scematic fault diagram")

### Inversion procedure
The code will automatically select profiles from the data based on the fault trace provided in `fault_file` at an increment specified by `swath_inc`. Fault parameters will be estimated at `param_inc` intervals; this can be the same or larger than `swath_inc`. For each individual inversion, all profiles within some distance (`max_reg_width`) of the specified fault node will be inverted simultaneously (if you only wish to invert single profiles, set `max_reg_width = 0`). Each sub-profile will be down-sampled and weighted prior to the inversion. 

### Bayesian inversion
The inversion utilizes a Bayesian (or stocahstic) framework to obtain an ensemble of plausible models and allow for uncertainty quantification of the model parameter estimates. It employs an Markov Chain Monte Carlo (MCMC) sampling algorithm (the `emcee` implementation of the MCMC Hammer) to explore the model parameter space in an efficient manner.

Full details of the 2D fault model and inversion prodedure are available in Vavra et al. (2023).
Additional information on the mathematical theory and practical implementation behind the specific MCMC algorithm used is available from Goodman and Weare (2010) and Foreman-Mackey et al. (2013).

## Requirements and Installation
In addition to default Python libraries, this code also uses [`matplotlib`](https://matplotlib.org/), [`numpy`](https://numpy.org/), [`pandas`](https://pandas.pydata.org/), [`scipy`](https://scipy.org/) (users familiar with Python will likely already have these installed). 

Several other packages you may need to install are:
- [`xarray`](https://docs.xarray.dev/en/stable/): reading NETCDF data files
- [`hyp5`](https://docs.h5py.org/en/stable/): reading/writing HDF5 output files
- [`emcee`](https://emcee.readthedocs.io/en/stable/): performing MCMC sampling
- [`numba`](https://numba.pydata.org/): accelerating some basic numerical calculations (i.e. fault model predictions)
- [`corner`](https://corner.readthedocs.io/en/latest/): plotting MCMC sampling results
- [`pyproj`](https://pypi.org/project/pyproj/): handling geographic coordinate systems

I would recommend using [Conda](https://conda.io/projects/conda/en/latest/index.html) to create a new Python environment to install and manage these packages. 

## Usage
There are four modes which can be used 
```
    python profile_inversion.py                 - perform entire inversion      
    python profile_inversion.py preview         - select and plot profiles only. 
    python profile_inversion.py reload          - remake all plots from most recent run
    python profile_inversion.py summary out_dir - remake summary plots for specified run
```

# References
Fialko, Y. (2007). Fracture and frictional mechanics - Theory. In G. Schubert (Ed.), Treatise on geophysics (Vol. 4, pp. 83–106). Elsevier Ltd.

Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. (2013). EMCEE: The MCMC hammer. Publications of the Astronomical Society of the Pacific, 125(925), 306–312. [https://doi.org/10.1086/670067](https://doi.org/10.1086/670067)

Goodman, J., & Weare, J. (2010). Ensemble samplers with affine invariance. Communications in Applied Mathematics and Computational Science, 5(1), 65–80. [https://doi.org/10.2140/camcos.2010.5.65](https://doi.org/10.2140/camcos.2010.5.65)

Segall, P. (2010). Earthquake and volcano deformation. Princeton University Press.

Vavra, E. J., Qiu, H., Chi, B., Share, P.-E., Allam, A., Morzfeld, M., et al. (2023). Active dipping interface of the Southern San Andreas fault revealed by space geodetic and seismic imaging. Journal of Geophysical Research: Solid Earth, 128, e2023JB026811. [https://doi.org/10.1029/2023JB026811](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JB026811)
