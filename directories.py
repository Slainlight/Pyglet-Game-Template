import os
import sys
base = os.getcwd()

statesFolder = base + "/States"
assetsFolder = base + "/Assets"

sys.path.insert(1, statesFolder)
sys.path.insert(1, assetsFolder)
