
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/Code/test2/auxiliary'
indir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-ISM/input/gradient_alt100_act150" # small scene
outdir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-ISM/myoutput_new"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
