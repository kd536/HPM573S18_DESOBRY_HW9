
# simulation settings
POP_SIZE = 1000     # cohort population size
SIM_LENGTH = 100    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years


PSA_ON = True      # if probabilistic sensitivity analysis is on

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,    0.0,    0.1],   # first column Well
    [0.0,   0.0,     1.0,    0.0],   # second column and row Stroke
    [0.0,   0.25,    0.55,   0.2],   # third column Post-Stroke
    [0.0,   0.0,     0.0,    1.0],   # last column death
    ]



# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,   # Well costs nothing
    5000.0,   # Stroke costs $5000
    0.0,    # Post-Stroke costs nothing
    0.0,         # Death costs nothing
    ]
