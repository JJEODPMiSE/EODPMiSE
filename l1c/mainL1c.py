
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = '/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/Code/test2/auxiliary'
# GM dir + L1B dir
indir = '/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-L1B/output'
outdir = '/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-L1C/myoutputs'

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
