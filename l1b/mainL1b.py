
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
from l1b.src.l1b import l1b

auxdir = r'/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/Code/test2/auxiliary'
# indir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-E2E/mysgmoutput"
# outdir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-E2E/myl1boutput"

indir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-L1B/input"
outdir = r"/Users/candis/Desktop/MasterUC3M/5 Earth Observation Data Processing/EODP_TER_2023/EODP-TS-L1B/myoutputs"


# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
