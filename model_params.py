def load():
    # 2D fault model parameters     
    # # 1. Uniform prior (must be defined even if using a Gaussian prior!)
    # prior_mode      = 'uniform' # Type of prior to be used
    # top_dir         = 'Results'
    # v_mode          = 'elliptical'  # elliptical, elliptical_shift, or elliptical_shift_vert
    # fault_dip       = None
    # parallel        = 'swaths'
    # v0_lim          = [0, 10e-3]    # m/yr (positive is right-lateral)
    # D_lim           = [0, 15e3]     # m
    # dip_lim         = [0, 180]      # deg
    # priors_uniform  = {'v0':  v0_lim, 'D': D_lim , 'dip': dip_lim}
    # labels          = [r'$v_0$', 'D', r'$\theta$']
    # units           = ['mm/yr', 'km', 'deg']
    # scales          = [1e3, 1e-3, 1]

    # # 2. Gaussian prior From Run_008
    # prior_mode = 'Gaussian' # Type of prior to be used
    # top_dir    = 'Filter_50km/2_Constrained'
    # v0_val     = [ 3.12e-3,   3*0.10e-3] # m/yr (positive is right-lateral)
    # D_val      = [ 1.97e3,    3*0.13e3 ] # m
    # dip_val    = [83.14,      3*2.10   ] # deg
    # priors_gaussian = {'v0':  v0_val, 'D': D_val, 'dip': dip_val}

    # # 3. Vertical fixed geometry
    # prior_mode      = 'uniform' # Type of prior to be used
    # top_dir         = 'Results'
    # v_mode          = 'fixed_dip'  
    # fault_dip       = np.ones(44)*90
    # parallel        = None
    # v0_lim          = [0, 10e-3]    # m/yr (positive is right-lateral)
    # D_lim           = [0, 15e3]     # m
    # priors_uniform  = {'v0':  v0_lim, 'D': D_lim }
    # labels          = [r'$v_0$', 'D']
    # units           = ['mm/yr', 'km']
    # scales          = [1e3, 1e-3]

    # Uniform prior with shift (must be defined even if using a Gaussian prior!)
    prior_mode      = 'uniform'
    top_dir         = 'Results'
    v_mode          = 'elliptical_shift'  # elliptical, elliptical_shift, or elliptical_shift_vert
    fault_dip       = None
    parallel        = 'swaths'
    v0_lim          = [0, 10e-3]    # m/yr (positive is right-lateral)
    D_lim           = [0, 15e3]     # m
    dip_lim         = [0, 180]      # deg
    vc_lim          = [-2e-3, 2e-3] # m
    priors_uniform  = {'v0':  v0_lim, 'D': D_lim , 'dip': dip_lim, 'vc':  vc_lim}
    labels          = [r'$v_0$', 'D', r'$\theta$', r'$v_c$']
    units           = ['mm/yr', 'km', 'deg', 'mm/yr']
    scales          = [1e3, 1e-3, 1, 1e3]

    # # Gaussian prior with shift
    # # Using results from Run_001
    # v0_val    = [ 2.40e-3,   0.30e-3] # m/yr (positive is right-lateral)
    # D_val     = [ 3.30e3,    0.30e3 ] # m
    # dip_val   = [62.13,      4.03   ] # deg
    # vc_val    = [ 0.66e-3,   0.05e-3] # m

    # Include dip as free parameter with shift
    # priors_gaussian = {'v0':  v0_val, 'D': D_val , 'dip': dip_val, 'vc':  vc_val}
    # labels          = [r'$v_0$', 'D', r'$\theta$', r'$v_c$']
    # units           = ['mm/yr', 'km', 'deg', 'mm/yr']
    # scales          = [1e3, 1e-3, 1, 1e3]

    # # Fixed geometry with velocity shift
    # priors_uniform  = {'v0':  v0_lim, 'D': D_lim , 'vc':  vc_lim}
    # labels          = [r'$v_0$', 'D', r'$v_c$']
    # units           = ['mm/yr', 'km', 'mm/yr']
    # scales          = [1e3, 1e-3, 1e3]

    # # Shallow and deep slip
    # priors_uniform  = {'s_0':   [0,     10e-3], 
    #                    'D_s':   [0,     10e3], 
    #                    'dip_s': [0,       180], 
    #                    's_pl':  [10e-3, 30e-3], 
    #                    'D_d':   [10e3,   15e3], 
    #                    'dip_d': [0,       180], 
    #                   }
    # labels = [r'$s_s$', r'$D_s$', r'$\theta_s$', r'$s_d$', r'$D_d$', r'$\theta_d$']
    # units = ['mm/yr', 'km', 'deg', 'mm/yr', 'km', 'deg']
    # scales = np.array([1e3, 1e-3, 1, 1e3, 1e-3, 1])

    # With shift
    # priors_uniform  = {'s_0':   [0,     10e-3], 
    #                    'D_s':   [0,      5e3], 
    #                    'dip_s': [0,       180], 
    #                    's_pl':  [10e-3,     30e-3], 
    #                    'D_d':   [10e3,   15e3], 
    #                    'dip_d': [0,       180], 
    #                    'v_ref': [-1,        1], 
    #                   }
    # labels = [r'$s_s$', r'$D_s$', r'$\theta_s$', r'$s_d$', r'$D_d$', r'$\theta_d$', r'$v_{ref}$']
    # units = ['mm/yr', 'km', 'deg', 'mm/yr', 'km', 'deg', 'mm/yr']
    # scales = np.array([1e3, 1e-3, 1, 1e3, 1e-3, 1, 1e3])
    return prior_mode, top_dir, v_mode, fault_dip, parallel, priors_uniform, labels, units, scales


if __name__ == '__main__':
    main()